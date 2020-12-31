import io
import pygame
from gtts import gTTS

def speak(text):
    # Save sound to RAM
    with io.BytesIO() as file:
        gTTS(text=text, lang="en").write_to_fp(file)
        file.seek(0)
        # Play the sound
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

if __name__ == '__main__':
    print("What should i say?")
    text = input("  >> ")
    speak(text)

