import yt_dlp
import os

os.chdir('C:/Users/micro/IA')

# URL de la playlist YouTube
playlist_url = 'https://www.youtube.com/@Antoine_Peytavin_Officiel/videos'

# Utiliser yt-dlp pour obtenir les informations sur la playlist
with yt_dlp.YoutubeDL() as ydl:
    playlist_info = ydl.extract_info(playlist_url, download=False)

# Ecrit la liste dans le fichier qui poste son nom
open(f"{playlist_info['title']}.txt", "w", encoding="utf-8") as file:
 file.write(f"{playlist_info['entries']]}")
