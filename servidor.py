




# Versiones custom
# mohist / catserver   Instala forge   primero
# purpur               Instala fabric  primero
# snapshot             Instala vanilla primero

# Regiones ngrok
# Código      Lugar
#----------- ---------------------------
# ap	      Asia/Pacific (Singapore)
# au		  Australia (Sydney)
# eu		  Europe (Frankfurt)
# in		  India (Mumbai)
# jp		  Japan (Tokyo)
# sa		  South America (São Paulo)
# us		  United States (Ohio)
# us-cal-1	  United States (California)















B=print
import requests as C,os
def D(repo_owner,repo_name,download_path='.'):
	H=f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest";D=C.get(H);A=''
	if D.status_code==200:
		I=D.json();E=I.get('assets')
		if E:
			F=E[0];G=F.get('browser_download_url')
			if G:
				A=os.path.join(download_path,F.get('name'))
				with open(A,'wb')as J:J.write(C.get(G).content)
				B(f"¡Descarga completa! Archivo guardado como: {A}")
			else:B('No se encontraron archivos para descargar en el último lanzamiento.')
		else:B('No se encontraron activos en el último lanzamiento.')
	else:B('Error al obtener información sobre el último lanzamiento.')
	return A
E='elyxdev'
F='elyx-server'
A=D(E,F)
if A.split('.')[2]=='pyc':os.system(f"python3 {A}")
else:os.system(f"chmod +x {A}");os.system(f"{A}")
