import pygame

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()

        self.tracks = ["music/track1.mp3", "music/track2.mp3"]
        self.current = 0
        self.paused = False

    def load_and_play(self):
        pygame.mixer.music.load(self.tracks[self.current])
        pygame.mixer.music.play()
        self.paused = False
        print("Playing:", self.tracks[self.current])

    def play(self):
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            self.load_and_play()

    def pause(self):
        pygame.mixer.music.pause()
        self.paused = True

    def stop(self):
        pygame.mixer.music.stop()
        self.paused = False

    def next(self):
        self.current = (self.current + 1) % len(self.tracks)
        self.load_and_play()

    def prev(self):
        self.current = (self.current - 1) % len(self.tracks)
        self.load_and_play()