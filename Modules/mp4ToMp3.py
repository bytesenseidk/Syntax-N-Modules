import os
from moviepy.editor import *

def video_to_sound(video_path):
    name = video_path.split("/")[-1]
    song_path = movie_path.strip(name)
    name = name.split(".")[0]
    video = VideoFileClip(os.path.join(movie_path))
    video.audio.write_audiofile(os.path.join(f"{song_path}{name}.mp3"))

if __name__ == "__main__":
    print("Drag 'n Drop Video Here:")
    movie_path = input(r"  >> ").strip('"')
    video_to_sound(movie_path)

