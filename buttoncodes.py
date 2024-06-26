import pygame
# from character_codes import *
import character_codes as c
pygame.init()
screen = pygame.display.set_mode((1000, 600))
 
buttons = pygame.sprite.Group()
#defines a class called Buttons
class Button(pygame.sprite.Sprite):
    def __init__(self, screen, position, text, size, colors="white on blue"):
      '''
      Sets the colors, font and font size as well as the position of the buttons.
      Arguments:
        self: str
        screen: int
        position: int
        text: str
        size: int
        colors: str
      '''
      super().__init__()
      self.colors = colors
      self.fg, self.bg = self.colors.split(" on ")
      self.font = pygame.font.SysFont("Arial", size)
      self.text_render = self.font.render(text, 1, self.fg)
      self.image = self.text_render
      self.x, self.y, self.w , self.h = self.text_render.get_rect()
      self.x, self.y = position
      self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
      self.position = position
      self.pressed = False
      self.update()
      buttons.add(self)
 
    def update(self):
      '''
      Draws the lines of the borders for the buttons and sets it rectangle
      Arguments:
        self: str
      '''
      self.fg, self.bg = self.colors.split(" on ")
      pygame.draw.line(screen, (150, 150, 150), (self.x, self.y), (self.x + self.w , self.y), 5)
      pygame.draw.line(screen, (150, 150, 150), (self.x, self.y - 2), (self.x, self.y + self.h), 5)
      pygame.draw.line(screen, (50, 50, 50), (self.x, self.y + self.h), (self.x + self.w , self.y + self.h), 5)
      pygame.draw.line(screen, (50, 50, 50), (self.x + self.w , self.y + self.h), [self.x + self.w , self.y], 5)
      pygame.draw.rect(screen, self.bg, (self.x, self.y, self.w , self.h))
        # screen.blit(self.text_render, self.position)
 
        # self.rect = screen, position, text, size, colors="white on blue"screen.blit(self.text_render, (self.x, self.y))
 


def not_hover():
  '''
  Changes the color to red on yellow when the mouse is not hovering over the button.
  '''
  for x in buttons:
      x.colors = "red on yellow"
      x.update()
 
def clicking(p_location, player_clues, player_inventory, character, status):
  """ 
  This checks if a button is being hovered on or being clicked and changes it according to that 
  Arguments:
    character: str
    p_location: int
    player_clues: list
    player_inventory: list
  """
  # 2. put the collide check for mouse hover here for each button
  if b0.rect.collidepoint(pygame.mouse.get_pos()):
    b0.colors = "red on green"
  elif b1.rect.collidepoint(pygame.mouse.get_pos()):
    b1.colors = "red on green"
  elif b2.rect.collidepoint(pygame.mouse.get_pos()):
    b2.colors = "red on green"
  elif b3.rect.collidepoint(pygame.mouse.get_pos()):
    b3.colors = "red on green"
  else:
    # this will work for every buttons going back to original color after mouse goes out
    not_hover()

  if pygame.mouse.get_pressed()[0]:
    # here the interactions with the click of the mouse
    if b0.rect.collidepoint(pygame.mouse.get_pos()) and b0.pressed == False:
      #changes self.press to True so that it knows that is' been pressed once so it doesn't keep running if the mouse is held down
      b0.pressed = True
      print("You search the room and find:")
      player_clues, player_inventory = c.room_search(p_location, player_clues, player_inventory, character)
      print()
    if b1.rect.collidepoint(pygame.mouse.get_pos()) and b1.pressed == False:
      b1.pressed = True
      print("This is your inventory:")
      print("Item 1:", player_inventory[0])
      print("Item 2:", player_inventory[1])
      print("Item 3:", player_inventory[2])
      print()
    if b2.rect.collidepoint(pygame.mouse.get_pos()) and b2.pressed == False:
      b2.pressed = True
      print("You have these clues:")
      print("Clue 1:", player_clues[0])
      print("Clue 2:", player_clues[1])
      print()
    if b3.rect.collidepoint(pygame.mouse.get_pos()) and b3.pressed == False:
      b3.pressed = True
      print("Goodbye!")
      #sets status to 4 since player clicked exit
      status = 4
  else:
    #changes it to False so that you can press it again another time
    b0.pressed = False
    b1.pressed = False
    b2.pressed = False
    b3.pressed = False

  # pygame.display.update()
  buttons.update()
  buttons.draw(screen)
  return player_clues, player_inventory, status
  

# 1 - create the buttons with an istance of Button here...
b0 = Button(screen, (10, 10), "Search the room", 20, "red on yellow")
b1 = Button(screen, (10, 40), "Inventory", 20, "red on yellow")
b2 = Button(screen, (10, 70), "Clues", 20, "red on yellow")
b3 = Button(screen, (10, 100), "Exit", 20, "red on yellow")

 
