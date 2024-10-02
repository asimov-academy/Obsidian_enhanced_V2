import os
import re
from pytube import YouTube
from pytube.download_helper import download_video

class YoutubeDownloader:
    def baixar_video(self, link='https://www.youtube.com/watch?v=dQw4w9WgXcQ'):
        print(f"Baixando vídeo do link: {link}")
        yt = YouTube(link)
        titulo = yt.title
        stream = yt.streams.get_highest_resolution()

        output_path = '_videos'
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print(f"Criada pasta '{output_path}'")

        title = re.sub(r'[<>:"/\\|?*]', '', titulo)
        title = title.replace("'", "")
        title = title.strip().replace(' ', '_')
        title = f'_{title}.mp4'
        video_path = stream.download(output_path, title)
        print(f"Baixado vídeo '{titulo}' para '{video_path}'")
        video_path = f'{output_path}/{title}'
        print(f"Vídeo baixado em: {video_path}")
        return video_path

if __name__ == '__main__':
    yt = YoutubeDownloader()
    link =  'PARA TESTAR ADICIONE O LINK DE UM VIDEO DO YOUTUBE'
    yt.baixar_video(link)