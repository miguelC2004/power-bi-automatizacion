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

    # Crear un nuevo informe
    new_report = Report()
    new_report.pages.append(models.Page(displayName="Página 1"))

    # Publicar el informe
    dataset_id = "ID_DEL_DATASET_EXISTENTE"
    dataset = client.datasets.get_dataset(dataset_id)
    report = client.reports.create_report(new_report, dataset_id=dataset.id)

    print(f"El informe '{report.name}' ha sido creado y publicado exitosamente.")

if __name__ == "__main__":
    main()
