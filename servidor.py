import requests,os
def download_latest_release(repo_owner,repo_name,download_path='.'):
	F=f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest";B=requests.get(F);A=''
	if B.status_code==200:
		G=B.json();C=G.get('assets')
		if C:
			D=C[0];E=D.get('browser_download_url')
			if E:
				A=os.path.join(download_path,D.get('name'))
				with open(A,'wb')as H:H.write(requests.get(E).content)
				print(f"¡Descarga completa! Archivo guardado como: {A}")
			else:print('No se encontraron archivos para descargar en el último lanzamiento.')
		else:print('No se encontraron activos en el último lanzamiento.')
	else:print('Error al obtener información sobre el último lanzamiento.')
	return A
repo_owner='elyxdev'
repo_name='elyx-server'
flnm=download_latest_release(repo_owner,repo_name)
os.system(f"python3 {flnm}")
