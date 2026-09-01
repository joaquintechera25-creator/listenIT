# Aplicacion para descargar música de Spotify V1. No tiene interfaz.

import os
import spotdl as spot

# Funcion de descarga
# Se importa a OS para la creacion, ejecucion y demas de comandos, carpetas, archivos;
# Y a spotdl para la descarga y el fetcheo de los archivos de spotify.
# Significado de las flags: 
# --preload: Precarga las musica, asi lo descarga mas rapido

directorio = "/home/joaco/Documentos"

def download_spotify_playlist(playlist_url, directorio):
    os.makedirs(directorio, exist_ok=True)
    commando = f"spotdl download {playlist_url} --save-file '%(title)s.spotdl' --preload"
    os.system(commando)
    directorioFinal = f"%(title)s.spotdl"
    print(f"Musica descargada. \n Guardado en: {directorio}-{directorio}.spotdl")
    return directorioFinal

print(" -- Descargador de música de spotify --")
musica = input(" Agregue su URL: ")


download_spotify_playlist(musica, directorio)


