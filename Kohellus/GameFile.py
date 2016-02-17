import pygame
from olioTiedosto import *
pygame.init()

#load assets and constants.
#give variables initial values

#display creation block
display_width = 600
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Härväyssohellus.')

#color definition block
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#asset loading block
skinface = pygame.image.load('skinface.png')
skinface = pygame.transform.scale(skinface,(display_width,display_height))
#racecar = pygame.image.load('racecar.png')
heroImg = 'zelda.png'

#Handles keyboard events
def event_handler(MoveAmount,x_change,y_change):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            #button handling block
            if event.type == pygame.KEYDOWN:
                #control the guy
                if event.key == pygame.K_LEFT:
                    x_change = -MoveAmount
                    #main_guy.__move_x_axis__(-MoveAmount)
                elif event.key == pygame.K_RIGHT:
                    x_change = MoveAmount
                    #main_guy.__move_x_axis__(MoveAmount)
                elif event.key == pygame.K_UP:
                    y_change = -MoveAmount
                    #main_guy.__move_y_axis__(-MoveAmount)
                elif event.key == pygame.K_DOWN:
                    y_change = MoveAmount
                    #main_guy.__move_y_axis__(MoveAmount)
                elif event.key == pygame.K_SPACE:
                    going_on = False
            elif event.type == pygame.KEYUP:
                x_change = 0
                y_change = 0
    return x_change,y_change

#This is where the game happens.
def game_loop():
    #The flag for keeping the game going.
    going_on = True
    #The clock.
    clock = pygame.time.Clock()
    #Characters speed in any direction
    MoveAmount = 7
    #Change in the character's coordinates.
    x_change = 0
    y_change = 0

    #Initialization of the player character.
    main_guy = main_dude(100,100,heroImg,70,70)

    #The actual, actual loop of the game.
    while (going_on == True):
        #Event handling. Take keyboard controls.
        x_change,y_change = event_handler(MoveAmount, x_change,y_change)

        #Movement update. Updates the player characters position.
        if x_change != 0:
            main_guy.__move_x_axis__(x_change)
        if y_change != 0:
            main_guy.__move_y_axis__(y_change)

        #screen update block
        gameDisplay.blit(skinface,(0,0))
        #updates the player characters sprite on the display.
        main_guy.__draw__(gameDisplay,x_change,y_change)
        #Dunno. Don't touch it.
        pygame.display.update()
        clock.tick(30)


game_loop()
pygame.quit()
quit()