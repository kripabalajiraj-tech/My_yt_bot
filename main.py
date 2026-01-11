import os
from yt_dlp import YoutubeDL

def get_last_hour_video(search_query):
    # Search options: last hour ki video aur 1 result
    # 'dateafter': 'now-1h' pichle 1 ghante ki videos filter karta hai
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_extractor': True,
        'default_search': 'ytsearch1',
        'daterange': 'now-1h', 
    }

    search_url = f"https://www.youtube.com/results?search_query={search_query}&sp=EgIIAQ%253D%253D"

    with YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(search_url, download=False)
            if 'entries' in info and len(info['entries']) > 0:
                video = info['entries'][0]
                print(f"Title: {video.get('title')}")
                print(f"Link: https://www.youtube.com/watch?v={video.get('id')}")
            else:
                print("Pichle 1 ghante mein is topic par koi video nahi mili.")
        except Exception as e:
            print(f"Error: {e}")

# Example Search
topic = input("Kya search karna hai? ")
get_last_hour_video(topic)
