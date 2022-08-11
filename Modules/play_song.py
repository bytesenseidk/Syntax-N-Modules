import os
import pygame

def play(song_path):
    song = song_path.split("/")[-1]
    rel_path = os.path.join(song_path.strip(song))
    os.chdir(rel_path)
    print(rel_path)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

if __name__ == "__main__":
    print("Drag Song Here:")
    song = input("  >> ")
    play(song)
