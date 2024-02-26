from powerbiclient import Report, models
import getpass

def main():
    # Obtener credenciales de usuario
    username = input("Ingrese su nombre de usuario de Power BI: ")
    password = getpass.getpass("Ingrese su contraseña de Power BI: ")

    # Autenticación
    token = models.TokenCredentials(username, password)
    
    # Crear una instancia del cliente de Power BI
    client = models.PowerBIClient(token)

    # Obtener el ID del informe que deseas automatizar (puedes obtenerlo desde la URL del informe)
    report_id = "ID_DEL_INFORME"

    # Obtener el informe
    report = client.reports.get_report(report_id)

    # Actualizar el informe
    client.reports.refresh_dataset(report_id)

    print("El informe ha sido actualizado exitosamente.")

if __name__ == "__main__":
    main()
