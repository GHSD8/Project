from tkinter import *
import pygame
from tkinter import filedialog
import os

root = Tk()
pygame.mixer.init()  #to initialize pygame mixer in order to play music

root.title('MP3 Player')
root.iconbitmap('apple_music_android_logo_icon_134021.ico')
root.geometry('500x300')

songlist = Listbox(root, bg="black", fg="green", width=60, selectbackground="grey", selectforeground="black")
songlist.pack(pady=20)

songs_folder = "songs/"
musicplayer_dir = os.path.dirname(os.path.realpath(__file__))
full_path_backslash = os.path.join(musicplayer_dir, songs_folder)
full_path = full_path_backslash.replace("\\", "/")


def add_songs():
    songs = filedialog.askopenfilenames(initialdir="songs/", title="Choose a song", filetypes=(("mp3 Files", "*.mp3"),))
    for song in songs:
        song = song.replace(full_path, "")
        song = song.replace(".mp3", "")
        songlist.insert(END, song)


def play_music():
    song = songlist.get(ACTIVE)
    song = f"{full_path}{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def stop_music():
    pygame.mixer.music.stop()

paused = False

def pause_music():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False


    else:
        pygame.mixer.music.pause()
        paused = True


def next_song():
    nextsong = songlist.curselection()
    nextsong = nextsong[0]+1
    song = songlist.get(nextsong)

    song = f"{full_path}{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    songlist.selection_clear(0, END)
    songlist.activate(nextsong)
    songlist.selection_set(nextsong, last=None)


def previous_song():
    prevsong = songlist.curselection()
    prevsong = prevsong[0] - 1
    song = songlist.get(prevsong)

    song = f"{full_path}{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    songlist.selection_clear(0, END)
    songlist.activate(prevsong)
    songlist.selection_set(prevsong, last=None)


back_img = PhotoImage(file=r"previous.png")
forward_img = PhotoImage(file=r"next.png")
pause_img = PhotoImage(file=r"pause.png")
play_img = PhotoImage(file=r"play.png")
stop_img = PhotoImage(file=r"stop.png")

controls = Frame(root)
controls.pack()

back_button = Button(controls, image=back_img, borderwidth=0, command = previous_song)
forward_button = Button(controls, image=forward_img, borderwidth=0, command = next_song)
pause_button = Button(controls, image=pause_img, borderwidth=0, command=pause_music)
play_button = Button(controls, image=play_img, borderwidth=0, command=play_music)
stop_button = Button(controls, image=stop_img, borderwidth=0, command=stop_music)

back_button.grid(row=0, column=0, padx=10, pady=40)
forward_button.grid(row=0, column=1, padx=10, pady=40)
pause_button.grid(row=0, column=2, padx=10, pady=40)
play_button.grid(row=0, column=3, padx=10, pady=40)
stop_button.grid(row=0, column=4, padx=10, pady=40)

#Menu
my_menu = Menu(root)
root.config(menu=my_menu)

addsongmenu = Menu(my_menu)
my_menu.add_cascade(label="Add songs", menu=addsongmenu)
addsongmenu.add_command(label="Add Songs to PLaylist", command=add_songs)

root.mainloop()