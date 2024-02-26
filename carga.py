from powerbiclient import models
import pandas as pd
import getpass

def cargar_datos_a_power_bi(username, password, dataset_id, datos_a_cargar):
    # Autenticación
    token = models.TokenCredentials(username, password)
    
    # Crear una instancia del cliente de Power BI
    client = models.PowerBIClient(token)

    # Obtener el conjunto de datos existente
    dataset = client.datasets.get_dataset(dataset_id)

    # Convertir los datos a un DataFrame de Pandas
    df = pd.DataFrame(datos_a_cargar)

    # Crear una tabla en el conjunto de datos y cargar los datos
    client.datasets.create_table(dataset_id, table_name="NuevaTabla", dataframe=df, if_table_exists="replace")

    print("Datos cargados exitosamente a Power BI.")

def main():
    # Obtener credenciales de usuario
    username = input("Ingrese su nombre de usuario de Power BI: ")
    password = getpass.getpass("Ingrese su contraseña de Power BI: ")

    # Obtener el ID del conjunto de datos al que deseas cargar los datos
    dataset_id = "ID_DEL_DATASET_EXISTENTE"

    # Datos a cargar (ejemplo)
    datos_a_cargar = {
        "Columna1": [1, 2, 3],
        "Columna2": ["A", "B", "C"]
    }

    try:
        # Cargar datos a Power BI
        cargar_datos_a_power_bi(username, password, dataset_id, datos_a_cargar)

    except Exception as e:
        print(f"Error al cargar datos a Power BI: {str(e)}")

if __name__ == "__main__":
    main()
