from tkinter import *
import pygame
from tkinter import filedialog
import os

root = Tk()
root.title("BoomBa Music Player")
root.iconbitmap('apple_music_android_logo_icon_134021.ico')
root.geometry("500x300")

pygame.mixer.init()  #to initialize pygame mixer in order to play music

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


#play function
def play():
    song = songlist.get(ACTIVE)
    song = f"{full_path}{song}.mp3"
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


#stop
def stop():
    pygame.mixer.music.stop()
    songlist.selection_clear(ACTIVE)

paused = False


def pause():
    global paused
    if paused == True:
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


#for button images
back_button_img = PhotoImage(file="previous.png")
forward_button_img = PhotoImage(file="next.png")
play_button_img = PhotoImage(file="play.png")
stop_button_img = PhotoImage(file="stop.png")
pause_button_img = PhotoImage(file="pause.png")

#create frames
controls_frame = Frame(root)
controls_frame.pack()

#create the buttons
back_button = Button(controls_frame, image=back_button_img, borderwidth=0, command=previous_song)
forward_button = Button(controls_frame, image=forward_button_img, borderwidth=0, command=next_song)
play_button = Button(controls_frame, image=play_button_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_button_img, borderwidth=0, command=pause)
stop_button = Button(controls_frame, image=stop_button_img, borderwidth=0, command=stop)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

#Menu
my_menu = Menu(root)
root.config(menu=my_menu)

addsongmenu = Menu(my_menu)
my_menu.add_cascade(label="Add songs", menu=addsongmenu)
addsongmenu.add_command(label="Add Songs to PLaylist", command=add_songs)

root.mainloop()
