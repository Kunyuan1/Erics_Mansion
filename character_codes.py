import pygame
import easygui
from easygui import *
from buttoncodes import *

#sets up two lists for the inventory and clues, each representing 

player_clues_list = [False, False]
player_inventory_list = [False, False, False]
boss_health = True

def character_choose():
  """
  This represents the username input.
  Returns:
    output: str
  """
  # message to be displayed
  text = "Enter your username"
  
  # window title
  title = "Username Input"
  
  # default text
  d_text = "Enter here.."
  
  # creating a enter box
  output = enterbox(text, title, d_text)

  return str(output)

def backgroundstory(character):
  """
  This represents the background story.
  Arguments:
    character: str
  Returns:
    page: str
  """
  Background_s = [character, " is a 38 year old woman who works at one of the biggest Shanghai hospitals as a surgeon. She's been working there for multiple years and has always been respected as the 'Human Guardian Angel' for her unmatched ability in heart surgeries.", character, " popularity soon caught the eyes of the multi-billionaire Eric Song. She was transfered suddenly to a hospital in the rural Yangshuo town. Here she was administrated to what appears to be her most important patient yet. Although, something seems off..."]
  options = ["Continue"]
  page = buttonbox(("".join(Background_s)), ("Background Story"), (options))
  return page

def spawn(character):
  """
  This represents the text that appear when you spawn.
  Arguments:
    character: str
  Returns:
    page: str
  """
  spawn_text = [character, " wakes up dazed and confused in a cold office room. She noticed that she has nothing on her other than her clothes. She's not sure where she is but she has a feeling that she needs to escape from here or something really bad will happen"]
  options = ["Continue"]
  page = buttonbox((''.join(spawn_text)), ("Spawn point"), (options))
  return page

def Med_Travel():
  """
  This represents the medical room travel options.
  Returns:
    page: str
  """
  Background_s = ["Pick a location to travel to:"]
  options = ["Spawn", "Medic Room", "Basement"]
  page = buttonbox(("\n".join(Background_s)), ("Travel Location"), (options))
  return page

def Basement_Travel():
  """
  This represents the basement travel options.
  Returns:
    page: str
  """
  Background_s = ["Pick a location to travel to:"]
  options = ["Spawn", "Medic Room", "Arcade", "Basement"]
  page = buttonbox(("\n".join(Background_s)), ("Travel Location"), (options))
  return page

def Arcade_Travel():
  """
  This represents the arcade room travel options.
  Returns:
    page: str
  """
  Background_s = ["Pick a location to travel to:"]
  options = ["Spawn", "Basement", "Living Room", "Arcade"]
  page = buttonbox(("\n".join(Background_s)), ("Travel Location"), (options))
  return page

def Living_Travel():
  """
  This represents the living room travel options.
  Returns:
    page: str
  """
  Background_s = ["Pick a location to travel to:"]
  options = ["Spawn", "Basement", "Arcade", "Final Room", "Living Room"]
  page = buttonbox(("\n".join(Background_s)), ("Travel Location"), (options))
  return page

def Final_Travel():
  """
  This represents the final room travel options.
  Returns:
    page: str
  """
  Background_s = ["Pick a location to travel to:"]
  options = ["Living Room", "Escape"]
  page = buttonbox(("\n".join(Background_s)), ("Travel Location"), (options))
  return page

def room_search(current_location, player_clues, player_inventory, character):
  """
  This checks the players current position and gives them a clue or item accordingly
  Arguments:
    current_location: int
    player_clues: list
    player_inventory: list
    character: str
  Returns:
    player_clues: list
    player_inventory: list
  """
  #if the player is at spawn this part of the function will run
  if current_location == 1:
    #if the player is at spawn and doesn't have the first clue yet this will run
    if player_clues == [False, False]:
      #changes the players first clue to 20169288 indicating he got the first clue
      player_clues = [20169288, False]
      print(character, " sees a bloody damaged tape and tape player in the far corner of the room. She decides to play the tape to see if she can get any information.")
      print()
      print("*static sound* H-help me! I can't find the way out. I've lost sense of time and don't know how long I've been stuck here for. Please, if anyone finds this, look for me! I don't know how much longer I can last. There's...a thing that's here. I don't know what it is but it scares me. Send help please! I believe the only way to get out is to kill it. I have a code that you might need later on. 20169288. Remember it.")
      print()
    #if the player is at spawn and already has the first clue or both, then this wil run
    else:
      print("The tape player seems to have broke after using it and can no longer play it.")
      print()
  #runs if player is currently in the final room
  elif current_location == 5:
    if player_clues == [20169288, False]:
      player_clues = [20169288, 
  """ ____________________________________
        |                                    |
        |          DONT TRUST ANYONE         |
        |      _                 _           |
        |     | | --> 4         |_| --> 7    |
        |       |               |_|          |
        |      _                 _           |
        |     |_  --> 6         |_| --> 6    |
        |     |_|                _|          |
        |      _                             |
        |     |_  --> 5          _  --> 1    |
        |      _|                            |
        |                                    |
        |            DONT USE MATH           |
         ____________________________________"""]
      print("After killing the figure,", character, "looks around the room and sees that there is a single piece of blood-stained paper on a table ", character, " walks over to the table and picks it up", character, " takes a the paper and puts her lighter near it to read it. When she looked back up, She sees a door at the other end of the room.")
      print()
    else:
      print("Other than the piece of paper in this room, there's not much else.")
      print()
  elif current_location == 2:
    if player_inventory == [False, False, False]:
      player_inventory = ["Lighter", False, False]
      print("After opening some cabinets ", character, " came accross 3 lighters that she stores in her pocket. It seems like that's all that has been left here.")
      print()
    else:
      print("There seems to be nothing else in here.")
      print()
  elif current_location == 3:
    #if player already has first item, then he can get the second one
    if player_inventory == ["Lighter", False, False]:
      #changes this to the new inventory
      player_inventory = ["Lighter", "Mask", False]
      #prints this statement
      print("Pulling out her lighter from earlier, ", character, " crawls makes her way through the dusty basement. Here, she found an unused mask that she put into his pocket. She wasn't sure what she'll use it for but she might as well take everything she can to be prepared for anything. With nothing else here, ", character, " decides to leave.")
      print()
    elif player_inventory == ["Lighter", "Mask", False]:
      print("There seems to be nothing left in this room.")
      print()
    else:
      print("This room is way too dark to see anything.", character, " needs a source of light to be able to navigate through here.")
      print()
  elif current_location == 4:
    if player_inventory == ["Lighter", "Mask", False]:
      player_inventory = ["Lighter", "Mask", "Axe"]
      print(character, "looks around the arcade and sees a treasure chest wrapped in a bunch of thick rope. Curious, she puts on her mask and using her lighter to burn the rope, she managed to open the chest. When she opened the chest ", character, " finds an axe lying on the inside. Out of every object she has found so far, this one gave her the most comfort. With an axe now in her possesion, ", character, " leaves and continues to try and find an exit.")
      print()
    elif player_inventory == ["Lighter", "Mask", "Axe"]:
      print("There seems to be nothing left in this room.")
      print()
    else:
      print("No matter how hard", character, " tries, she cannot destroy the thick ropes that are wrapped around the chest.")
      print()

  #returns the new clues list
  return player_clues, player_inventory


def locked_door_code():
  """
  This represents the code the user enters to enter the arcade room .
  Returns:
    code: str
  """
  message = "Enter Code Here"
  title = "Locked Door"
  d_text = "Enter here.."
  output = enterbox(message, title, d_text)
  return str(output)

def final_locked_door_code():
  """
  This represents the code the user enters to escape the mansion.
  Returns:
    code: str
  """
  title = "Locked Door"
  message = [ '|   _            _   _          _   |',
              '|  | | |_|  _   _| _|    =  _|  |',
              '|    |    |     |_   _|         _|  |',]
  hint = '\n'.join(message)
  d_text = "Enter here.."
  output = enterbox(hint, title, d_text)
  return str(output)

def Exit(character):
  """
  This represents the Exit.
  Arguments:
    character: str
  Returns:
    page: str
  """
  Escape_text = ["As ", character, " opens the door, a blast of cold air hits her in the face. As she opens her eyes, she felt the light of the sun on her dirty body and the coldness of the snow on her fingertips. It was a blissful feeling and she fell to her knees crying in happiness and relief."]
  options = ["End."]
  page = buttonbox((''.join(Escape_text)), ("Escape"), (options))
  return page

def boss():
  """
  This function represents the boss fight.
  returns:
    page: str
  """
  boss_hp = True
  text = "The doors suddenly slam shut and the room lights turn on all at once in a blinding flash. It seems to be a japanese styled room. You look around the room but then you freeze as you see a pitch black figure standing at the door. He moves his arms slowly and reveal a pair of sharp claws under the cloak. Then, he lunges at you."
  title = "Boss Fight"
  output = msgbox(text, title)
  title2 = ["Pick a move:"]
  options = ["Swing Axe", "Dodge", "Run"]
  page = buttonbox(("\n".join(title2)), ("Boss Fight"), (options))
  return page




def character_movement(screen, bg_choice, character_rect, character_image, front_images, back_images, left_images, right_images, doorrect_spawn, doorrect2_spawn, screen_scene, doorrectmed, doorrectbasement, doorrectbasement2, doorrectarcade, doorrectlivingroom, doorrectmansion, character, player_clues_list, player_inventory_list, boss_health, status):
  """
  This represents the character movement.
  Arg: 
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
    screen_scene: int
    player_clues_list: list
    player_inventory_list: list 
    boss_health: bool
    current_status: int
  """
  pygame.display.flip()
  pygame.time.wait(1000)
  #sets up a counter
  image_count = 0
  #sets up clock so that the program can be slowed down
  clock = pygame.time.Clock()
  #sets up a counter for the last scene of the game
  ending_count = 0
    
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
 
   
    # Get the keys pressed and changes the character location
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      image_count += 1
      character_image = left_images
      character_rect.x -= 10
  
    elif keys[pygame.K_RIGHT]:
      image_count += 1
      character_image = right_images
      character_rect.x += 10
  
    elif keys[pygame.K_UP]:
      image_count += 1
      character_image = back_images
      character_rect.y -= 10
  
    elif keys[pygame.K_DOWN]:
      image_count += 1
      character_image = front_images
      character_rect.y += 10
  
    else:
      image_count = 0

    screen.blit(bg_choice, (0, 0))
    player_clues_list, player_inventory_list, current_status = clicking(screen_scene, player_clues_list, player_inventory_list, character, status)
    #checks if current_status is 4 which represents exiting the game.
    if current_status == 4:
      running = False
    
    if image_count > 4:
      image_count = 1
    # Draw the character animation according the the keys pressec
    screen.blit(character_image[image_count], character_rect)
  
    #checks current character location
    if screen_scene == 1:
      #checks if the character collides with the door
      if character_rect.colliderect(doorrect_spawn):
        #opens travel menu
        screen_scene = Med_Travel()
        #sets a conditional statement for every room
        if screen_scene == "Spawn":
          screen_scene = 1
        elif screen_scene == 'Medic Room':
          #changes the map
          screen_scene = 2
        elif screen_scene == 'Basement':
          screen_scene = 3
        character_rect.x = 300
        running = False
      elif character_rect.colliderect(doorrect2_spawn):
        screen_scene = Med_Travel()
        if screen_scene == "Spawn":
          screen_scene = 1
        elif screen_scene == 'Medic Room':
          screen_scene = 2
        elif screen_scene == 'Basement':
          screen_scene = 3
        character_rect.x = 300
        running = False
      else:
        # Keep player on the screen and sets up the map boundaries
        if character_rect.top <= 380:
            character_rect.top = 380
        if character_rect.bottom >= 600:
            character_rect.bottom = 600

    if screen_scene == 2:
      if character_rect.colliderect(doorrectmed):
        screen_scene = Med_Travel()
        if screen_scene == "Spawn":
          screen_scene = 1
        elif screen_scene == 'Basement':
          screen_scene = 3
        else:
          screen_scene = 2
        character_rect.x = 300
        running = False
      else:
        if character_rect.right > 950:
            character_rect.right = 950
        if character_rect.top <= 495:
            character_rect.top = 495
        if character_rect.bottom >= 500:
            character_rect.bottom = 500

    if screen_scene == 3:
      if character_rect.colliderect(doorrectbasement):
        screen_scene = Basement_Travel()
        if screen_scene == "Spawn":
          screen_scene = 1
        elif screen_scene == 'Medic Room':
          screen_scene = 2
        elif screen_scene == 'Arcade':
          #prompts user to input the code for the door
          door_code = locked_door_code()
          #checks if user inputs the right code or not
          if door_code == "20169288":
            # title for the message box
            title = "Locked Door"
            # creating a message
            message = "Code accepted."
            # creating a message box
            msg = msgbox(message, title)
            screen_scene = 4
          else:
            # title for the message box
            title = "Locked Door"
            # creating a message
            message = "Error. Code input wrong."
            # creating a message box
            msg = msgbox(message, title)
            #screen scene stays the same since user got the wrong code
            screen_scene = 3
        else:
          screen_scene = 3
        character_rect.x = 300
        running = False
      elif character_rect.colliderect(doorrectbasement2):
        screen_scene = Basement_Travel()
        if screen_scene == "Spawn":
          screen_scene = 1
        elif screen_scene == 'Medic Room':
          screen_scene = 2
        elif screen_scene == 'Arcade':
          door_code = locked_door_code()
          if door_code == "20169288":
            # title for the message box
            title = "Locked Door"
            # creating a message
            message = "Code accepted."
            # creating a message box
            msg = msgbox(message, title)
            screen_scene = 4
          else:
            # title for the message box
            title = "Locked Door"
            # creating a message
            message = "Error. Code input wrong."
            # creating a message box
            msg = msgbox(message, title)
            screen_scene = 3
        else:
          screen_scene = 3
        character_rect.x = 300
        running = False
      else:
        if character_rect.top <= 350:
            character_rect.top = 350
        if character_rect.bottom >= 470:
            character_rect.bottom = 470

    if screen_scene == 4:
      if character_rect.colliderect(doorrectarcade):
        screen_scene = Arcade_Travel()
        if screen_scene == "Spawn":
            screen_scene = 1  
        elif screen_scene == 'Basement':
              screen_scene = 3
        elif screen_scene == 'Living Room':
          screen_scene = 5
        else:
          screen_scene = 4
        character_rect.x = 300
        running = False
      else:
        if character_rect.top < 250:
          character_rect.top = 250
        if character_rect.right > 700:
          character_rect.right = 700
        if character_rect.left < 400:
          character_rect.left = 400
        if character_rect.bottom >= 600:
          character_rect.bottom = 600

    if screen_scene == 5:
      if boss_health == True:
        choice = boss()
        if choice == 'Swing Axe':
          #checks user inventory to see if he has all the items to kill the boss
          if player_inventory_list == ['Lighter', 'Mask', 'Axe']:
            title = "Action"
            message = "You swing the axe at the figure and hits it right in the torso. As the figure falls onto the ground you put on your mask and swing your axe at him again. Being a doctor you know exactly where to aim. With one swift motion, you slice its head off. Then you pull out your lighter and burn the body to make sure it's dead."
            msg = msgbox(message, title)
            boss_health = False
          else:
            title = "Action"
            message = "Yoo reach for an axe but you don't have one. The figure smashes against your body and sinks his sharp claws into your torso. You died."
            msg = msgbox(message, title)
            #changes screen_scene to 1 since user died so he respawns at the spawn point
            screen_scene = 1
        elif choice == 'Dodge':
          title = "Action"
          message = "You duck to the ground and roll to the side. The figure smashes into the vase behind you, shattering it to pieces. It the turns around and lunges back at you, this time hitting its mark. You died."
          msg = msgbox(message, title)
          screen_scene = 1
        elif choice == "Run":
          title = "Action"
          message = "You turn towards the door to run but it's locked. You try your hardest to open it but it just wouldn't budge. The figure continues to approach you as you struggle to open the door. You turn around and the last thing you see is the figure's sharp claws coming down from above. You died."
          msg = msgbox(message, title)
          screen_scene = 1
      if character_rect.colliderect(doorrectlivingroom):
        screen_scene = Living_Travel()
        if screen_scene == "Spawn":
          screen_scene = 1
        elif screen_scene == 'Basement':
            screen_scene = 3
        elif screen_scene == 'Arcade':
          door_code = locked_door_code()
          if door_code == "20169288":
            title = "Locked Door"
            message = "code accepted."
            msg = msgbox(message, title)
            screen_scene = 4
          else:
            title = "Locked Door"
            message = "Error. Code input wrong."
            msg = msgbox(message, title)
            screen_scene = 5
        elif screen_scene == 'Final Room':
          screen_scene = 6
        else:
          screen_scene = 5
        character_rect.x = 300
        running = False
      else:
        if character_rect.right > 800:
          character_rect.right = 800
        if character_rect.left < 200:
          character_rect.left = 200
        if character_rect.bottom >= 590:
          character_rect.bottom =590
        if character_rect.top < 80:
          character_rect.top = 80

    if screen_scene == 6:
      if character_rect.colliderect(doorrectmansion):
        screen_scene = Final_Travel()
        if screen_scene == 'Escape':
          door_code = final_locked_door_code()
          if door_code == "4415525":
            title = "Locked Door"
            message = "Code accepted."
            msg = msgbox(message, title)
            screen_scene = 7
          else:
            title = "Locked Door"
            message = "Error. Code input wrong."
            msg = msgbox(message, title)
            screen_scene = 6
        elif screen_scene == 'Living Room':
          screen_scene = 5
        character_rect.x = 300
        running = False
      else:
        if character_rect.right > 990:
          character_rect.right = 990
        if character_rect.left < 20:
          character_rect.left = 20
        if character_rect.bottom >= 490:
          character_rect.bottom = 490
        if character_rect.top < 370:
          character_rect.top = 370
          
    if screen_scene == 7:
      #checks if it's the first time displaying the ending scene
      if ending_count == 0:
        Exit(character)
        title = "Game Complete"
        message = "Congratulations! You have successfully escaped Eric's Mansion. You now live to tell the tale to the rest of the world. Goodbye and see you next time!"
        msg = msgbox(message, title)
       
        #adds 1 to make sure it's not displayed again
        ending_count += 1
             
      #checks if it's the second time and changes the screen to the background
      elif ending_count == 1:
        screen.blit(bg_choice, (0, 0))
       
    # Update the screen
    pygame.display.update()

    #changes how fast the program runs
    clock.tick(15)
  #returns the screen_scene and clues and inventory
  return screen_scene, player_clues_list, player_inventory_list, boss_health, current_status