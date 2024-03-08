import yt_dlp
import os
import json

os.chdir('C:/Users/micro/IA')

# URL de la playlist YouTube
playlist_url = 'https://www.youtube.com/@Antoine_Peytavin_Officiel/videos'

# Utiliser yt-dlp pour obtenir les informations sur la playlist
with yt_dlp.YoutubeDL() as ydl:
    playlist_info = ydl.extract_info(playlist_url, download=False)

# Extraire uniquement les URL des vidéos de la playlist
video_urls = [entry['webpage_url'] for entry in playlist_info['entries']]

# Ecrit la liste dans le fichier qui poste son nom
with open(f"{playlist_info['title']}.txt", "w", encoding="utf-8") as file:
    for url in video_urls:
        file.write(f"{url}\n")

