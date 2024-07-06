import pandas as pd
import numpy as np

# Definir las columnas
columns = ["index", "user_id", "fullname", "whatsapp", "points", "timestamp", "market_id", "market_point", "market_name", "option_id", "option_name", "event_id", "event_name", "host_id"]

# Datos de ejemplo proporcionados
data = [
    [0, 8083, "Gabriel Pabon", "573016197438", 80, 1720222747, 436, 10, "Pregunta 1", 1063, "test 1", 124, "Evento Prueba SQS 2", 188545074335628],
    [1, 8083, "Gabriel Pabon", "573016197438", 80, 1720222752, 437, 20, "Pregunta 2", 1065, "test 3", 124, "Evento Prueba SQS 2", 188545074335628],
    [2, 8083, "Gabriel Pabon", "573016197438", 80, 1720222756, 438, 50, "Pregunta 3", 1067, "Test 5", 124, "Evento Prueba SQS 2", 188545074335628],
    [3, 2878, "JORGE AMAYA", "573004669165", 50, 1720222774, 436, 0, "Pregunta 1", 1064, "test 2", 124, "Evento Prueba SQS 2", 188545074335628],
    [4, 2878, "JORGE AMAYA", "573004669165", 50, 1720222777, 437, 0, "Pregunta 2", 1066, "test 4", 124, "Evento Prueba SQS 2", 188545074335628],
    [5, 2878, "JORGE AMAYA", "573004669165", 50, 1720222780, 438, 50, "Pregunta 3", 1067, "Test 5", 124, "Evento Prueba SQS 2", 188545074335628],
    [6, 2877, "El Jugador2.0", "573005561204", 10, 1720222869, 436, 10, "Pregunta 1", 1063, "test 1", 124, "Evento Prueba SQS 2", 188545074335628],
    [7, 2877, "El Jugador2.0", "573005561204", 10, 1720222873, 437, 0, "Pregunta 2", 1066, "test 4", 124, "Evento Prueba SQS 2", 188545074335628],
    [8, 2877, "El Jugador2.0", "573005561204", 10, 1720222876, 438, 0, "Pregunta 3", 1068, "test 6", 124, "Evento Prueba SQS 2", 188545074335628]
]

# Función para generar datos ficticios
def generate_user_data(start_index, num_users, user_id_start):
    data = []
    user_ids = np.arange(user_id_start, user_id_start + num_users)
    timestamps = np.arange(1720222747 + start_index, 1720222747 + start_index + num_users * 3)
    
    for i in range(num_users * 3):
        user_id = user_ids[i // 3]
        fullname = f"User {user_id}"
        whatsapp = f"57300{user_id % 1000000:06d}"
        points = np.random.choice([10, 50, 80])
        timestamp = timestamps[i]
        market_id = np.random.choice([436, 437, 438])
        market_point = np.random.choice([10, 20, 50, 0])
        market_name = ["Pregunta 1", "Pregunta 2", "Pregunta 3"][market_id % 3]
        option_id = np.random.choice([1063, 1065, 1067, 1068])
        option_name = np.random.choice(["test 1", "test 3", "Test 5", "test 2", "test 4", "test 6"])
        event_id = 124
        event_name = "Evento Prueba SQS 2"
        host_id = 188545074335628
        
        row = [start_index + i, user_id, fullname, whatsapp, points, timestamp, market_id, market_point, market_name, option_id, option_name, event_id, event_name, host_id]
        data.append(row)
    
    return pd.DataFrame(data, columns=columns)

# Generar y guardar el archivo CSV
def create_csv(num_users, filename):
    start_index = 0
    user_id_start = 10000
    df = pd.DataFrame(data, columns=columns)
    df = pd.concat([df, generate_user_data(start_index, num_users, user_id_start)])
    df.to_csv(filename, index=False)
    print(f"Archivo generado: {filename}")


def run():
    # Ejemplo de uso
    num_users = 6000  # Cambia esto al número de usuarios que desees generar
    filename = "market_bets.csv"
    create_csv(num_users, filename)


if __name__ == "__main__":
    run()
