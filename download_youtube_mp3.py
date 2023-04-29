import yt_dlp
from pydub import AudioSegment


def baixar_video(url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'noplaylist': True,
            'quiet': True,
            'no_warnings': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            nome_arquivo = ydl.prepare_filename(info)
    except Exception as e:
        print("Erro ao baixar o vídeo:", e)
        return None

    return nome_arquivo


def converter_para_mp3(nome_arquivo):
    try:
        audio = AudioSegment.from_file(nome_arquivo)
        nome_arquivo_mp3 = f"{nome_arquivo.split('.')[0]}.mp3"
        audio.export(nome_arquivo_mp3, format="mp3")
    except Exception as e:
        print("Erro ao converter o vídeo para MP3:", e)
        return None

    return nome_arquivo_mp3


def baixar_e_converter(url):
    print("Baixando o vídeo...")
    nome_arquivo = baixar_video(url)
    if nome_arquivo is None:
        print("Não foi possível baixar o vídeo.")
        return None

    print("Convertendo o vídeo para MP3...")
    nome_arquivo_mp3 = converter_para_mp3(nome_arquivo)
    if nome_arquivo_mp3 is None:
        print("Não foi possível converter o vídeo para MP3.")
        return None

    return nome_arquivo_mp3
