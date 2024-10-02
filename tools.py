from langchain.tools import tool

from utils.download_youtube import YoutubeDownloader
from utils.audio import Audio
from utils.cria_partes_notas import Notes
from utils.image import ProcessImage


class IsaacTools:
    @tool
    def baixar_video_youtube(link: str) -> str:
        """Baixa o vídeo de um link do YouTube e extrai a descrição."""
        video_path = YoutubeDownloader().baixar_video(link)
        return video_path

    @tool
    def extrair_audio(video_path):
        """Extrai o áudio de um vídeo e salva em formato WAV."""
        audio_path = Audio.extrair(video_path)
        return audio_path

    @tool
    def descreve_imagem(image_path):
        """Analisa o image_path e retorna sua descrição detalhada, caso a imagem tenha textos, eles serão transcritos"""
        image_description = ProcessImage.openai_analysis(image_path)
        return image_description

    @tool
    def transcrever_audio(audio_path: str) -> str:
        """Transcreve um arquivo de áudio salvo em audio_path para texto."""
        transcricao_path = Audio.transcrever(audio_path)
        return transcricao_path

    @tool
    def salvar_nota(transcricao_path):
        """Salva o texto_final em um arquivo de texto_final no diretório _notas."""
        Notes.salvar_nota(transcricao_path)