from tkinter import Tk
import tkinter.filedialog as tkf
# import moviepy.editor as editor // mp4 to mp3
from pydub import AudioSegment
import os

root=Tk()
root.withdraw()

rutas = tkf.askopenfilenames(filetypes=[('Video', '*.ogg')])

for ruta in rutas:
    nombre = os.path.basename(ruta)
    nombre = nombre.split('.')[0]
    song = AudioSegment.from_ogg(ruta)
    song.export(nombre + ".mp3", format="mp3")

    # video_clip = editor.VideoFileClip(ruta) // mp4 to mp3
    # video_clip.audio.write_audiofile(nombre.replace(".mp4", ".mp3")) // mp4 to mp3