import pyautogui
import pyaudio
import numpy as np
import wave
import cv2
from moviepy.editor import VideoFileClip, AudioFileClip
import threading
import time

# Configurações de gravação de áudio
AUDIO_FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
AUDIO_OUTPUT = 'audio.wav'

# Configurações de gravação de vídeo
VIDEO_OUTPUT = 'output.avi'
VIDEO_FPS = 24

# Função para gravar áudio
def record_audio():
    p = pyaudio.PyAudio()

    stream = p.open(format=AUDIO_FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []

    print("Gravando áudio...")

    while recording:
        data = stream.read(CHUNK)
        frames.append(data)

    print("Parando gravação de áudio.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(AUDIO_OUTPUT, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(AUDIO_FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

# Função para gravar vídeo
def record_video():
    screen_size = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(VIDEO_OUTPUT, fourcc, VIDEO_FPS, screen_size)

    print("Gravando vídeo...")

    while recording:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)

    print("Parando gravação de vídeo.")
    out.release()

# Inicia as gravações de áudio e vídeo em threads separadas
recording = True
audio_thread = threading.Thread(target=record_audio)
video_thread = threading.Thread(target=record_video)

audio_thread.start()
video_thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    recording = False
    audio_thread.join()
    video_thread.join()

print("Gravação finalizada. Arquivos salvos.")

# Combinar áudio e vídeo
print("Combinando áudio e vídeo...")
video_clip = VideoFileClip(VIDEO_OUTPUT)
audio_clip = AudioFileClip(AUDIO_OUTPUT)
final_clip = video_clip.set_audio(audio_clip)
final_clip.write_videofile("final_output.mp4", codec='libx264', audio_codec='aac')

print("Vídeo final salvo como 'final_output.mp4'.")
