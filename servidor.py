import requests
import os

def download_latest_release(repo_owner, repo_name, download_path="."):
    # Hacer una solicitud a la API de GitHub para obtener información sobre el último lanzamiento
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
    response = requests.get(url)
    filename = ""
    # Comprobar si la solicitud fue exitosa
    if response.status_code == 200:
        # Obtener la URL del archivo de lanzamiento
        release_info = response.json()
        assets = release_info.get("assets")
        if assets:
            asset = assets[0]  # Tomar el primer archivo de la lista de activos
            download_url = asset.get("browser_download_url")
            if download_url:
                # Descargar el archivo
                filename = os.path.join(download_path, asset.get("name"))
                with open(filename, "wb") as f:
                    f.write(requests.get(download_url).content)
                print(f"¡Descarga completa! Archivo guardado como: {filename}")
            else:
                print("No se encontraron archivos para descargar en el último lanzamiento.")
        else:
            print("No se encontraron activos en el último lanzamiento.")
    else:
        print("Error al obtener información sobre el último lanzamiento.")
    return filename

# Ejemplo de uso
repo_owner = "yos-rg"
repo_name = "elyx-server"
flnm = download_latest_release(repo_owner, repo_name)
os.system(f"python3 {flnm}")