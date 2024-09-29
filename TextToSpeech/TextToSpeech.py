import io
import pygame
from gtts import gTTS


def speak(text):
    if text == '':
        return
    with io.BytesIO() as file:
        gTTS(text=text, lang="en").write_to_fp(file)
        file.seek(0)
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue



if __name__ == '__main__':
    with open('speech.txt') as f:
        speech = [line.rstrip('\n') for line in f]
        for sentence in speech:
            speak(sentence)
    f.close()
