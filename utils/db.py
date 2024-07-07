import sqlite3

def init_db():
    conn = sqlite3.connect('data/hotel_reservas_basica.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS habitaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo_habitacion TEXT,
        estado TEXT,
        camas INTEGER,
        camas_ocupadas INTEGER
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero_identificacion FLOAT,
        nombre TEXT,
        id_habitacion INTEGER,
        check_in DATE,
        check_out DATE,
        estado TEXT,
        numero_contacto FLOAT,
        email TEXT
    )
    ''')
    
    # Insertar datos iniciales de las habitaciones (4 ordinarias y 2 compartidas)
    cursor.execute('SELECT COUNT(*) FROM habitaciones')
    if cursor.fetchone()[0] == 0:
        habitaciones_data = [
            ('King', 'disponible', 1, 0),
            ('King', 'disponible', 1, 0),
            ('Individual', 'disponible', 1, 0),
            ('Individual', 'disponible', 1, 0),
            ('Compartida', 'disponible', 4, 0),
            ('Compartida', 'disponible', 4, 0)
        ]
        cursor.executemany('INSERT INTO habitaciones (tipo_habitacion, estado, camas, camas_ocupadas) VALUES (?, ?, ?, ?)', habitaciones_data)
    
    conn.commit()
    conn.close()

def get_available_rooms(check_in, check_out, tipo_habitacion):
    conn = sqlite3.connect('data/hotel_reservas_basica.db')
    cursor = conn.cursor()
    if tipo_habitacion == 'Compartida':
        cursor.execute('''
        SELECT * FROM habitaciones WHERE tipo_habitacion = ? AND camas_ocupadas < camas
        ''', (tipo_habitacion,))
    else:
        cursor.execute('''
        SELECT * FROM habitaciones WHERE tipo_habitacion = ? AND estado = 'disponible'
        ''', (tipo_habitacion,))
    habitaciones = cursor.fetchall()
    conn.close()
    return habitaciones

def make_reservation(numero_identificacion, nombre, id_habitacion, check_in, check_out, numero_contacto, email):
    conn = sqlite3.connect('data/hotel_reservas_basica.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO reservas (numero_identificacion, nombre, id_habitacion, check_in, check_out, estado, numero_contacto, email)
    VALUES (?, ?, ?, ?, ?, 'confirmada', ?, ?)
    ''', (numero_identificacion, nombre, id_habitacion, check_in, check_out, numero_contacto, email))
    
    # Actualizar el estado de la habitación
    cursor.execute('SELECT tipo_habitacion FROM habitaciones WHERE id = ?', (id_habitacion,))
    tipo_habitacion = cursor.fetchone()[0]
    
    if tipo_habitacion == 'Compartida':
        cursor.execute('''
        UPDATE habitaciones SET camas_ocupadas = camas_ocupadas + 1 WHERE id = ?
        ''', (id_habitacion,))
    else:
        cursor.execute('''
        UPDATE habitaciones SET estado = 'ocupada' WHERE id = ?
        ''', (id_habitacion,))
    
    conn.commit()
    conn.close()