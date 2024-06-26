import pygame

#setting screen dimensions
length = 1000
width = 600

#create screen size and title
screen = pygame.display.set_mode((length, width))
pygame.display.set_caption("Escape Eric's Mansion")

#setting character and background
Morioh = pygame.image.load('MoriohTownStartPage.png')
Intro_bg_start = pygame.image.load('InstructionBg.png')
first_spawn = pygame.image.load('FirstSpawnResized.webp')
first_room = pygame.image.load('MedRoomResized.jpg')
second_room = pygame.image.load('BasementResized.jpg')
third_room = pygame.image.load('ArcadeRoom.jpg')
fourth_room = pygame.image.load('LivingRoomResized.png')
fifth_room = pygame.image.load('JoestarMansion (1).jpg')
ending_page_none_resized = pygame.image.load('EndingPage.jpg')

#Change the size of the character background
Morioh_Town = pygame.transform.scale(Morioh, (1000, 600))
Intro_bg = pygame.transform.scale(Intro_bg_start, (1000, 600))
ending_page = pygame.transform.scale(ending_page_none_resized, (1000, 600))