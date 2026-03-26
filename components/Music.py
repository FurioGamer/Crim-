import pygame

class PlayMusic:
    def __init__(self, music_location):
        pygame.mixer.init()
        pygame.mixer.music.stop()
        pygame.mixer.music.load(music_location)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(loops=-1)

class PlayDing:
    def __init__(self, music_location):
        pygame.mixer.init()
        pygame.mixer.music.stop()
        pygame.mixer.music.load(music_location)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()