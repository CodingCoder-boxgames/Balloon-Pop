from const import *
import pygame, sys
from game import Game

pygame.mixer.init()
class Main:
    def __init__(self):
        self.height = HEIGHT
        self.width = WIDTH
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.game = Game(self.screen)
        self.cur_time = 0
        self.bg_cur_time = 0
        self.can_shoot = True
        self.bg_count = 1
        self.path = 'src/graphics/background/background' + str(self.bg_count) + '.png'
        self.song = 1 
        self.music_path = "src/graphics/music/music" + str(self.song) + ".wav"
        self.bg = pygame.image.load(self.path)

    def loop(self):

        clock = pygame.time.Clock()
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.play(-1, 0.0)
        pygame.init()
        Game(self.screen).add_hearths()
        while True:
            self.path = 'src/graphics/background/background' + str(self.bg_count) + '.png'

            self.bg = pygame.image.load(self.path)
            self.screen.blit(self.bg, (0,0))
            pygame.display.set_caption("Balloon Pop")
            self.game.gameloop()
            # shoot delaying
            if self.can_shoot == False:

                self.cur_time += 0.5
                if self.cur_time >= 15:
                    self.can_shoot = True
                    self.cur_time = 0
            # bg animating
            self.bg_cur_time += 1
            if self.bg_cur_time >= 10:
                
                if self.bg_count <= 39:
                    self.bg_count += 1
                else: self.bg_count = 1
                self.bg_cur_time = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.can_shoot:
                    self.game.shoot()
                    
                    self.game.new_player()
                    self.can_shoot = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                    self.next_song()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5: self.previous_song()
            # game loop    

            # update and fps      
            clock.tick(FPS)
            pygame.display.update()
    
    def next_song(self):
        if self.song == 7:
            self.song = 0



        self.song += 1
        self.music_path = "src/graphics/music/music" + str(self.song) + ".wav"
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.play(-1, 0.0)
        print(self.song)
    def previous_song(self):
        if self.song == 1:
            self.song = 7
            
        else:
            self.song -= 1
        self.music_path = "src/graphics/music/music" + str(self.song) + ".wav"
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.play(-1, 0.0)
        print(self.song)
main = Main()
if __name__ == "__main__":
    main.loop()