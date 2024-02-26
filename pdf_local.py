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

    # Obtener el ID del informe que deseas exportar (puedes obtenerlo desde la URL del informe)
    report_id = "ID_DEL_INFORME"

    # Obtener el informe
    report = client.reports.get_report(report_id)

    # Exportar el informe a PDF
    report_bytes = client.reports.get_report_pdf(report_id)
    file_name = "Informe_PowerBI.pdf"

    # Guardar el PDF localmente
    with open(file_name, "wb") as pdf_file:
        pdf_file.write(report_bytes)

    print(f"El informe ha sido exportado a '{file_name}' exitosamente.")

if __name__ == "__main__":
    main()
