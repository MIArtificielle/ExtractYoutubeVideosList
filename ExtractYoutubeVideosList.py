import yt_dlp
import os

os.chdir('C:/Users/micro/IA')

# URL de la playlist YouTube
playlist_url = 'https://www.youtube.com/@Antoine_Peytavin_Officiel/videos'

# Configuration pour yt-dlp
ydl_opts = {
    'extract_flat': True,
    'quiet': True,
    'force_generic_extractor': True,
    'skip_download': True,
}

# Utiliser yt-dlp pour obtenir les informations sur la chaîne
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    channel_info = ydl.extract_info(channel_url)

# Extraire les URL des vidéos avec le préfixe ajouté
video_urls = [f"https://www.youtube.com/watch?v={entry['id']}" for entry in channel_info['entries']]

# Créer un répertoire avec le nom de la chaîne YouTube
os.makedirs(playlist_info['title'], exist_ok=True)

# Écrire les URLs dans un fichier
with open(f"./{playlist_info['title']}/url.lst", "w", encoding="utf-8") as file:
    for url in video_urls:
        file.write(f"{url}\n")
