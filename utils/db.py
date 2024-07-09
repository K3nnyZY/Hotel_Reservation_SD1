import sqlite3

def init_db():
    conn = sqlite3.connect('data/hotel_reservas_basica.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS habitaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo_habitacion TEXT,
        camas INTEGER,
        camas_ocupadas INTEGER
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero_identificacion INTEGER,
        nombre TEXT,
        id_habitacion INTEGER,
        check_in DATE,
        check_out DATE,
        estado TEXT,
        numero_contacto INTEGER,
        email TEXT
    )
    ''')
    
    cursor.execute('SELECT COUNT(*) FROM habitaciones')
    if cursor.fetchone()[0] == 0:
        habitaciones_data = [
            (101 + i, 'Individual', 1, 0) for i in range(3)
        ] + [
            (201 + i, 'King', 1, 0) for i in range(3)
        ] + [
            (301 + i, 'Compartida', 4, 0) for i in range(3)
        ]
        cursor.executemany('INSERT INTO habitaciones (id, tipo_habitacion, camas, camas_ocupadas) VALUES (?, ?, ?, ?)', habitaciones_data)
    
    conn.commit()
    conn.close()

def get_available_rooms(check_in, check_out, tipo_habitacion):
    conn = sqlite3.connect('data/hotel_reservas_basica.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT h.id, h.tipo_habitacion, h.camas, h.camas_ocupadas, 
           (SELECT COUNT(*) FROM reservas r 
            WHERE r.id_habitacion = h.id 
              AND ((r.check_in <= ? AND r.check_out >= ?) 
                   OR (r.check_in >= ? AND r.check_out <= ?)
                   OR (? BETWEEN r.check_in AND r.check_out)
                   OR (? BETWEEN r.check_in AND r.check_out))) as camas_ocupadas_periodo 
    FROM habitaciones h 
    WHERE h.tipo_habitacion = ? 
    GROUP BY h.id, h.tipo_habitacion, h.camas, h.camas_ocupadas 
    HAVING h.camas - camas_ocupadas_periodo > 0
    ''', (check_out, check_in, check_in, check_out, check_in, check_out, tipo_habitacion))
    
    habitaciones_disponibles = cursor.fetchall()
    conn.close()
    return habitaciones_disponibles

def make_reservation(numero_identificacion, nombre, id_habitacion, check_in, check_out, numero_contacto, email):
    conn = sqlite3.connect('data/hotel_reservas_basica.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO reservas (numero_identificacion, nombre, id_habitacion, check_in, check_out, estado, numero_contacto, email)
    VALUES (?, ?, ?, ?, ?, 'confirmada', ?, ?)
    ''', (numero_identificacion, nombre, id_habitacion, check_in, check_out, numero_contacto, email))
    
    # Actualizar el número de camas ocupadas durante el periodo de reserva
    cursor.execute('''
    UPDATE habitaciones SET camas_ocupadas = camas_ocupadas + 1 WHERE id = ?
    ''', (id_habitacion,))
    
    conn.commit()
    conn.close()

def end_reservation():
    conn = sqlite3.connect('data/hotel_reservas_basica.db')
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE habitaciones SET camas_ocupadas = camas_ocupadas - 1 
    WHERE id IN (
        SELECT id_habitacion FROM reservas 
        WHERE check_out < date('now') AND estado = 'confirmada'
    )
    ''')
    cursor.execute('''
    UPDATE reservas SET estado = 'finalizada' 
    WHERE check_out < date('now') AND estado = 'confirmada'
    ''')
    conn.commit()
    conn.close()