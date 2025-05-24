import pygame
from tkinter import *
from tkinter import filedialog, ttk
import os

pygame.mixer.init()

def load_and_play_song():
    song_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    if song_path:
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        song_label.config(text="Playing: " + os.path.basename(song_path)) 
        update_time() 

def stop_song():
    pygame.mixer.music.stop()
    song_label.config(text="No song playing") 

def pause_song():
    pygame.mixer.music.pause()

def resume_song():
    pygame.mixer.music.unpause()
    update_time()  

def update_time():
    if pygame.mixer.music.get_busy(): 
        current_time = pygame.mixer.music.get_pos() // 1000
        mins, secs = divmod(current_time, 60)
        time_label.config(text=f"Time: {mins:02}:{secs:02}")
        window.after(1000, update_time) 

window = Tk()
window.title("Python Music Player")
window.geometry("400x400")
window.config(bg="#2d3436")

song_label = Label(window, text="No song playing", bg="#2d3436", fg="#dfe6e9", font=("Helvetica", 10))
song_label.pack(pady=10)

Button(window, text="Load & Play", command=load_and_play_song, bg="#0984e3", fg="white",font=("Helvetica", 12, "bold")).pack(pady=10)
Button(window, text="Stop", command=stop_song, bg="#0984e3", fg="white",font=("Helvetica", 12, "bold")).pack(pady=5)
Button(window, text="Pause", command=pause_song, bg="#0984e3", fg="white",font=("Helvetica", 12, "bold")).pack(pady=5)
Button(window, text="Resume", command=resume_song, bg="#0984e3", fg="white",font=("Helvetica", 12, "bold")).pack(pady=5)

Label(window, text="Volume", bg="#2d3436", fg="#dfe6e9",font=("Helvetica", 12,)).pack()
volume_slider = Scale(window, from_=0, to=1, orient=HORIZONTAL, resolution=0.1, command=lambda v: pygame.mixer.music.set_volume(float(v)), bg="#636e72", fg="#dfe6e9", troughcolor="#0984e3")
volume_slider.set(0.5)
volume_slider.pack()

time_label = Label(window, text="Time: 00:00")
time_label.pack(pady=5)

window.mainloop()
