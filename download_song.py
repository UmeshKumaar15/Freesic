#Freesic 2023
#The codes for downloading the song and its Album cover are included here.
#Umesh Kumaar

import os
import requests
from pytube import YouTube
from youtubesearchpython import VideosSearch
import subprocess
from googleapiclient.discovery import build
download_folder = "Freesic\\songs_pic"  

# Define your API key and custom search engine ID
API_KEY = "AIzaSyCb5SQ0AIX0G2kJKmdhYnjGCBjQceaqbkc"
CUSTOM_SEARCH_ID = "44ee7c4ccef574c60"
def search_youtube_song(song_name):
    videos = VideosSearch(song_name, limit=1)
    results = videos.result()
    
    if results:
        first_video = results['result'][0]
        video_url = f"https://www.youtube.com/watch?v={first_video['id']}"
        return video_url
    else:
        return None, None
    
def download_top_google_image(query, download_folder):

    # Build the Google Custom Search API service
    service = build("customsearch", "v1", developerKey=API_KEY)

    # Perform a search for images
    result = service.cse().list(
        q=query,
        cx=CUSTOM_SEARCH_ID,
        searchType="image",
        num=1  # Number of results to retrieve (1 for the top image)
    ).execute()

    # Check if results were found
    if "items" in result:
        top_image = result["items"][0]
        image_url = top_image["link"]

        # Get the image content
        image_response = requests.get(image_url)
        if image_response.status_code == 200:

            # Save the image content to the specified download folder
            filename = os.path.join(download_folder, f"{query}.jpg")
            with open(filename, "wb") as file:
                file.write(image_response.content)
            print(f"Downloaded top image to {filename}")
        else:
            print("Failed to download the image.")
    else:
        print("No images found in the search results.")

def add_song(song_name):
    destination = "Freesic\\Playlist"
    audio_files = [f for f in os.listdir(destination) if f.lower().endswith(('.mp3', '.wav', '.ogg', '.aac'))]
    
    if song_name in audio_files:
        return

    yt_url = search_youtube_song(song_name)
    
    if yt_url:
        yt = YouTube(yt_url)
        stream = yt.streams.filter(only_audio=True).first()
        out_file = stream.download(output_path=destination)
        base, _ = os.path.splitext(out_file)
        mp3_file = os.path.join(destination, song_name + '.mp3')
        ffmpeg_path = "C:\\Users\\umesh\\Documents\\Bangalore codes\\Freesic\\ffmpeg-2023-10-26-git-2b300eb533-essentials_build\\bin\\ffmpeg.exe"
        subprocess.run([ffmpeg_path, '-n', '-i', out_file, mp3_file])
        os.remove(out_file)
        
        # Download the thumbnail and save it to "Freesic\\songs_pic"
        download_top_google_image(song_name, download_folder)
        print(yt.title + " has been successfully added.")