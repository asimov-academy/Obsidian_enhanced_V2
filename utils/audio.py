import os

from moviepy.editor import *

from faster_whisper import WhisperModel

from dotenv import load_dotenv
load_dotenv()

class Audio:
    def extrair(video_path):
        """Extrai o áudio de um vídeo e salva em formato."""
        print(f"\nExtraindo áudio do vídeo: {video_path}")
        
        video_path = video_path.replace("'", "")
        
        print(f'video_path = {video_path}')
        
        output_path = os.path.dirname(video_path)
        output_path = output_path.replace('videos', 'audios')
        print(f'output_path = {output_path}')
        
        base_name = os.path.splitext(os.path.basename(video_path))[0]
        print(f'basename = {base_name}')

        audio_path = f'{output_path}/{base_name}.mp3'
        print(f'audio_path = {audio_path}')

        video = VideoFileClip(video_path)

        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print(f"Criada pasta {output_path}")

        video.audio.write_audiofile(audio_path)

        print(f'audio salvo em: {audio_path}')
        return audio_path

    def transcrever(audio_path: str) -> str:
        """Transcreve um arquivo de áudio salvo em audio_path para texto utilizando reconhecimento de fala."""
        print(f"Transcrevendo áudio: {audio_path}")
        
        audio_path = audio_path.replace("'", "")
        model = WhisperModel("medium") # , "cuda"

        result = model.transcribe(audio_path)

        transcricao = ""
        for segment in result[0]:
            transcricao += segment.text + " "

        output_path = os.path.dirname(audio_path)
        output_path = output_path.replace('audios', 'transcricoes')
        base_name = os.path.splitext(os.path.basename(audio_path))[0]
        transcricao_path = f'{output_path}/{base_name}.md'

        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print(f"Criada pasta '{output_path}'")

        with open(transcricao_path, 'w') as f:
            f.write(transcricao.strip())

        print(f'transcrição salva em: {transcricao_path}')
        return transcricao_path

if __name__ == '__main__':
    video_path = 'PARA TESTAR ADICIONE O CAMINHO DE UM VIDEO MP4'
    print('PARA TESTAR ADICIONE O CAMINHO DE UM VIDEO MP4')
    audio_path = Audio.extrair(video_path)
    transcricao = Audio.transcrever(audio_path)
