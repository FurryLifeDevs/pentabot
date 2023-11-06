import yt_dlp
from youtube_search import YoutubeSearch
import os


async def string2link(string: str):
    if "youtube" not in string:
        string = "/watch?v=dQw4w9WgXcQ"  # WARNING! RICK ROLL!!!
    search_result = search(string, 1)
    return 'https://www.youtube.com' + search_result[0]['url_suffix']


def search(arg: str, max_results: int):
    results = YoutubeSearch(arg, max_results=max_results).to_dict()
    print(results)
    return results


def download_audio(url: str, id: int):
    if os.path.isfile("audio.m4a"):
        os.remove("audio.m4a")
    if os.path.isfile(f"data/{id}/{hash(url)}.m4a"):
        return
    URLS = [url]
    ydl_opts = {
        'noplaylist': True,
        'outtmpl': 'data/' + str(id) + f'/{hash(url)}' + '.%(ext)s',
        'format': 'm4a/bestaudio/best',
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_title = info_dict['title']
        error_code = ydl.download(URLS)
    return video_title
