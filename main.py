"""
Final Game Project
Kunyuan Hu
ICS3U
This program creates a game based off my adventure game
History:
March 21, 2023: Program creation
"""
#======================== IMPORTS & SETUP ========================
import sys
import easygui as g
from easygui import *
from character_codes import *
from PlayerBackgroundcode import *
#allows access to the pygame library
import pygame

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
  )

#initialize pygame
pygame.init()

def main(screen, first_spawn, first_room, second_room, third_room, fourth_room, fifth_room, ending_page, character_rect, character_image, front_images, back_images, left_images, right_images, doorrect_spawn, doorrect2_spawn, doorrectmed, doorrectbasement, doorrectbasement2, doorrectarcade, doorrectlivingroom, doorrectmansion, player_clues_list, player_inventory_list, boss_health):
  """
  This function is the main driver for the program.
  Args: 
    screen: int
    bg_choice:image
    character_rect: rect
    character_image: image
    front_images: image
    back_images: image
    left_images: image
    right_images: image
    doorrect_spawn:  rect
    doorrect2_spawn: rect
    screen_scene: rect
    doorrectmed: rect
    doorrectbasement: rect
    doorrectbasement2: rect
    doorrectarcade: rect
    doorrectlivingroom: rect
    doorrectmansion: rect
    character: img
    player_clues_list: list
    player_inventory_list: list
    boss_health: bool
  Returns: 
    running: bool
  """
  status = 1
  running = True
  while running:
    if status == 1:
      status = welcome()
    elif status == 2:
      status = instructions()
    if status == 3:
      status = game(screen, first_spawn, first_room, second_room, third_room, fourth_room, fifth_room, ending_page, character_rect, character_image, front_images, back_images, left_images, right_images, doorrect_spawn, doorrect2_spawn, doorrectmed, doorrectbasement, doorrectbasement2, doorrectarcade, doorrectlivingroom, doorrectmansion, player_clues_list, player_inventory_list, boss_health, status)
    elif status == 4:
      running = False
    #This is needed in order to show everything for each screen
    pygame.display.update()
  return running
  
def welcome():
  """
  This function is the welcome for the program. There is a button to get the instructions and a button to start the game
  Args: none
  Returns: choice: int
  """
  choice = 1
  screen.blit(Morioh_Town,(0,0))
  width = screen.get_width()
  height = screen.get_height()
  #None = default font
  font = pygame.font.Font(None, 40)
  #Draw Instructions Button. First creates the text, then sets up the rectangle based on the text
  instText = font.render('Instructions', True, (0,0,0))
  instRect = instText.get_rect()
  instRect.center = width/2-320, height/2-180
  pygame.draw.rect(screen, (0,0,0), (instRect[0]-10,instRect[1]-10,instRect[2]+20, instRect[3]+20), 2)
  screen.blit(instText, instRect)
  #Draw Play button. First creates the text, then sets up the rectangle based on the text
  gameText = font.render('Play', True, (0,0,0))
  gameRect = instText.get_rect()
  gameRect.center = width/2-320, height/2-120
  pygame.draw.rect(screen, (0,0,0), (gameRect[0]-10,gameRect[1]-10,gameRect[2]+20, gameRect[3]+20), 2)
  screen.blit(gameText, gameRect)

  for event in pygame.event.get():
    mouse = pygame.mouse.get_pos()
    if event.type == pygame.QUIT:
      pygame.quit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if instRect[0] <= mouse[0] <= instRect[0]+instRect[2] and instRect[1] <= mouse[1] <= instRect[1]+instRect[3]:
        choice = 2
      if gameRect[0] <= mouse[0] <= gameRect[0]+gameRect[2] and gameRect[1] <= mouse[1] <= gameRect[1]+gameRect[3] and choice < 3:
        choice = 3
  return choice

def instructions():
  """
  This function is the instructions for the program. There is a button to get back to the menu
  Args: none
  Returns: choice: int
  """
  choice = 2
  screen.blit(Intro_bg,(0,0))
  width = screen.get_width()
  height = screen.get_height()
  font = pygame.font.Font(None, 25)
  instructions_texts = "Use arrow keys to move. To change maps collide with the map boundaries. Collect hints and items to escape!"
  instructionText = font.render(instructions_texts, True, (255, 255, 255))
  instructionRect = instructionText.get_rect()
  instructionRect.center = width/2, height/2-100
  pygame.draw.rect(screen,(255, 255, 255),(instructionRect[0]-10,instructionRect[1]-10,instructionRect[2]+20, instructionRect[3]+20), 2)
  screen.blit(instructionText, instructionRect)
  
  gameText = font.render('Return', True, (255, 215, 0))
  gameRect = gameText.get_rect()
  gameRect.center = width/2, height/2+100
  pygame.draw.rect(screen, (255,215,0), (gameRect[0]-10,gameRect[1]-10,gameRect[2]+20, gameRect[3]+20), 2)
  screen.blit(gameText, gameRect)
  
  for event in pygame.event.get():
    mouse = pygame.mouse.get_pos()
    if event.type == pygame.QUIT:
      pygame.quit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if gameRect[0] <= mouse[0] <= gameRect[0]+gameRect[2] and gameRect[1] <= mouse[1] <= gameRect[1]+gameRect[3] and choice < 3:
        choice = 1
  return choice

def game(screen, first_spawn, first_room, second_room, third_room, fourth_room, fifth_room, ending_page, character_rect, character_image, front_images, back_images, left_images, right_images, doorrect, doorrect2, doorrectmed, doorrectbasement, doorrectbasement2, doorrectarcade, doorrectlivingroom, doorrectmansion, player_clues_list, player_inventory_list, boss_health, status):
  '''
  Args:
    screen: int
    bg_choice:image
    character_rect: rect
    character_image: image
    front_images: image
    back_images: image
    left_images: image
    right_images: image
    doorrect_spawn:  rect
    doorrect2_spawn: rect
    screen_scene: rect
    doorrectmed: rect
    doorrectbasement: rect
    doorrectbasement2: rect
    doorrectarcade: rect
    doorrectlivingroom: rect
    doorrectmansion: rect
    character: img
    player_clues_list: list
    player_inventory_list: list
    boss_health: bool
    status: int
  Returns:
    status: int
  '''
  #allows user to choose their character
  character = character_choose()
  #shows the background story
  backgroundstory(character)
  #shows the spawn text
  spawn(character)
  #sets a screen scene counter
  screen_scene = 1
  running = True

  
  while running:
    #shows scenes according to the screen_scene counter and status
    if screen_scene == 1 and status == 3:
      #calls character_movement function and assigns values to all these variables that change throughout the game.
      screen_scene, player_clues_list, player_inventory_list, boss_health, status = character_movement(screen, first_spawn, character_rect, character_image, front_images, back_images, left_images, right_images, doorrect, doorrect2, screen_scene, doorrectmed, doorrectbasement, doorrectbasement2, doorrectarcade, doorrectlivingroom, doorrectmansion, character, player_clues_list, player_inventory_list, boss_health, status)
      if status == 4:
        running = False
    elif screen_scene == 2 and status == 3:
      screen_scene, player_clues_list, player_inventory_list, boss_health, status = character_movement(screen, first_room, character_rect, character_image, front_images, back_images, left_images, right_images, doorrect, doorrect2, screen_scene, doorrectmed, doorrectbasement, doorrectbasement2, doorrectarcade, doorrectlivingroom, doorrectmansion, character, player_clues_list, player_inventory_list, boss_health, status)
      if status == 4:
        running = False
    elif screen_scene == 3 and status == 3:
      screen_scene, player_clues_list, player_inventory_list, boss_health, status = character_movement(screen, second_room, character_rect, character_image, front_images, back_images, left_images, right_images, doorrect, doorrect2, screen_scene, doorrectmed, doorrectbasement, doorrectbasement2, doorrectarcade, doorrectlivingroom, doorrectmansion, character, player_clues_list, player_inventory_list, boss_health, status)
      if status == 4:
        running = False
    elif screen_scene == 4 and status == 3:
      screen_scene, player_clues_list, player_inventory_list, boss_health, status = character_movement(screen, third_room, character_rect, character_image, front_images, back_images, left_images, right_images, doorrect, doorrect2, screen_scene, doorrectmed, doorrectbasement, doorrectbasement2, doorrectarcade, doorrectlivingroom, doorrectmansion, character, player_clues_list, player_inventory_list, boss_health, status)
      if status == 4:
        running = False
    elif screen_scene == 5 and status == 3:
      screen_scene, player_clues_list, player_inventory_list, boss_health, status = character_movement(screen, fourth_room, character_rect, character_image, front_images, back_images, left_images, right_images, doorrect, doorrect2, screen_scene, doorrectmed, doorrectbasement, doorrectbasement2, doorrectarcade, doorrectlivingroom, doorrectmansion, character, player_clues_list, player_inventory_list, boss_health, status)
      if status == 4:
        running = False
    elif screen_scene == 6 and status == 3:
      screen_scene, player_clues_list, player_inventory_list, boss_health, status = character_movement(screen, fifth_room, character_rect, character_image, front_images, back_images, left_images, right_images, doorrect, doorrect2, screen_scene, doorrectmed, doorrectbasement, doorrectbasement2, doorrectarcade, doorrectlivingroom, doorrectmansion, character, player_clues_list, player_inventory_list, boss_health, status)
      if status == 4:
        running = False
    elif screen_scene == 7 and status == 3:
      screen_scene, player_clues_list, player_inventory_list, boss_health, status = character_movement(screen, ending_page, character_rect, character_image, front_images, back_images, left_images, right_images, doorrect, doorrect2, screen_scene, doorrectmed, doorrectbasement, doorrectbasement2, doorrectarcade, doorrectlivingroom, doorrectmansion, character, player_clues_list, player_inventory_list, boss_health, status)
      if status == 4:
        running = False
  #returns status so the game knows whether to keep running or to stop
  return status



#===========================MAIN============================
#sets screen size and image
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
first_spawn = first_spawn.convert_alpha()
screen.blit(first_spawn, (0, 0))

#sets up all the spirte animations
frontleft = pygame.image.load("LeftFoot (1).png")
frontright = pygame.image.load("RightFoot (1).png")
frontidle = pygame.image.load("BlueGirlSprite (1).png")
#adds them all into a list
front_images = [frontidle, frontleft, frontleft, frontright, frontright]
character_rect = frontidle.get_rect()
character_rect.x = 430
character_rect.y = 400
character_image = front_images

backleft = pygame.image.load("backleftfoot (1).png")
backright = pygame.image.load("backrightfoot (1).png")
backidle = pygame.image.load("backidle (1).png")
back_images = [backidle, backleft, backleft, backright, backright]

leftleft = pygame.image.load("leftsideleftfoot (1).png")
leftright = pygame.image.load("leftsiderightfoot (1).png")
leftidle = pygame.image.load("leftsideidle (1).png")
left_images = [leftidle, leftleft, leftleft, leftright, leftright]

rightleft = pygame.image.load("rightsideleftfoot (1).png")
rightright = pygame.image.load("rightsiderightfoot (1).png")
rightidle = pygame.image.load("rightsideidle (1).png")
right_images = [rightidle, rightleft, rightleft, rightright, rightright]

#sets up the door sprite and gets it's rectangles
door = pygame.image.load('doorsprite (1).png')
doorrect_spawn = door.get_rect()
doorrect_spawn.x = -20
doorrect_spawn.y = 290
doorrect2_spawn = door.get_rect()
doorrect2_spawn.x = 850
doorrect2_spawn.y = 290
doorrectmed = door.get_rect()
doorrectmed.x = -50
doorrectmed.y = 290
doorrectbasement = door.get_rect()
doorrectbasement.x = -70
doorrectbasement.y = 290
doorrectbasement2 = door.get_rect()
doorrectbasement2.x = 950
doorrectbasement2.y = 290
doorrectarcade = door.get_rect()
doorrectarcade.x = 500
doorrectarcade.y = 0
doorrectlivingroom = door.get_rect()
doorrectlivingroom.x = 50
doorrectlivingroom.y = 0
doorrectmansion = door.get_rect()
doorrectmansion.x = 985
doorrectmansion.y = 290

# Set up the loading text
font = pygame.font.Font(None, 50)
loading_text = font.render("Loading...", True, (255, 255, 255))
loading_text_rect = loading_text.get_rect(center=(screen_width / 2, screen_height / 2))

# Set up the progress bar
progress_bar_width = 400
progress_bar_height = 20
progress_bar_x = (screen_width / 2) - (progress_bar_width / 2)
progress_bar_y = (screen_height / 2) + 50
progress_bar_outline_rect = pygame.Rect(progress_bar_x, progress_bar_y, progress_bar_width, progress_bar_height)
progress_bar_rect = pygame.Rect(progress_bar_x + 2, progress_bar_y + 2, 0, progress_bar_height - 4)

load = pygame.image.load("tahmkenchloading (1).jpg").convert()
screen.blit(load, (0,0))


#sets up a counter for what scene the player is at
scenenum = 0
clock = pygame.time.Clock()
# Set up the game loop
running = True
while running:
  pressed_keys = pygame.key.get_pressed()
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  if scenenum == 0:
    w = screen.get_width()
    h = screen.get_height()
    progress_bar_rect.width += 1
    if progress_bar_rect.width >= progress_bar_width - 4:
	    progress_bar_rect.width = progress_bar_width - 4
	    scenenum += 1
	
		# Draw everything
    screen.blit(load, (0,0)) 
    pygame.draw.rect(screen, (255, 255, 255), progress_bar_outline_rect, 2)
    pygame.draw.rect(screen, (255, 255, 255), progress_bar_rect)
    screen.blit(loading_text, loading_text_rect)

    openingText = font.render("Eric's Mansion", True, (255, 215, 0))
    openingRect = openingText.get_rect()
    openingRect.center = w/2, h/2-100
    pygame.draw.rect(screen,(255, 215, 0),(openingRect[0]-10,openingRect[1]-10,openingRect[2]+20, openingRect[3]+20), 2)
    screen.blit(openingText, openingRect)
  
  if scenenum == 1:
    running = main(screen, first_spawn, first_room, second_room, third_room, fourth_room, fifth_room, ending_page, character_rect, character_image, front_images, back_images, left_images, right_images, doorrect_spawn, doorrect2_spawn, doorrectmed, doorrectbasement, doorrectbasement2, doorrectarcade, doorrectlivingroom, doorrectmansion, player_clues_list, player_inventory_list, boss_health)

  #updates display
  pygame.display.update()
  clock.tick(120)

#quits program
pygame.quit()