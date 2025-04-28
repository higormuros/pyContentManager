import yt_dlp
import speech_recognition as sr
from pydub import AudioSegment
import os

def youtube_audio_to_text(youtube_url):
   
    try:
        ydl_opts = {
            'extractaudio': True,
            'format': 'bestaudio/best',
            'outtmpl': 'audio_temp.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(youtube_url, download=True)
            audio_file = ydl.prepare_filename(info_dict)

        try:
            audio = AudioSegment.from_file(audio_file)
        except Exception as e:
            print(f"Erro ao carregar o arquivo de áudio: {e}")
            os.remove(audio_file)
            return None

        r = sr.Recognizer()
        text = ""
        chunk_size = 60000
        start = 0
        end = chunk_size

        while start < len(audio):
            print(f"Processando trecho de áudio: {start // 60000} - {end // 60000} minutos")
            audio_chunk = audio[start:end]
            audio_chunk.export("audio_chunk.wav", format="wav")

            with sr.AudioFile("audio_chunk.wav") as source:
                try:
                    audio_data = r.record(source)
                    partial_text = r.recognize_google(audio_data, language='pt-BR')
                    text += partial_text + " "
                except sr.UnknownValueError:
                    text += "[Não foi possível entender este trecho] "
                except sr.RequestError as e:
                    print(f"Erro na requisição ao serviço de reconhecimento de voz do Google; {e}")
                    os.remove("audio_chunk.wav")
                    os.remove(audio_file)
                    return None

            start = end
            end += chunk_size
            os.remove("audio_chunk.wav")

        os.remove(audio_file)
        return text.strip()

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None

url_do_video = "URL VIDEO"
texto_transcrito = youtube_audio_to_text(url_do_video)

if texto_transcrito:
    print("\nTexto transcrito:")
    print(texto_transcrito)
else:
    print("\nNão foi possível transcrever o áudio.")