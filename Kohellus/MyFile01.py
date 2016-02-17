import pygame
import time
import random
pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

block_color = (53,115,255)

car_width = 69

carImg = pygame.image.load('racecar.png')
cubeImg = pygame.image.load('skinface.png')
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit racey')

def things_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text,(0,0))

def things(thingX,thingY,thingW,thingH,color):
    pygame.draw.rect(gameDisplay,color,[thingX,thingY,thingW,thingH])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text,True, black)
    return  textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()
    time.sleep(2)

    game_loop()

def crash():
    message_display('You crashed!')

def game_loop():


    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startX = random.randrange(0,display_width)
    thing_startY = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    dodged = 0

    clock = pygame.time.Clock()
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                    if event.key == pygame.K_RIGHT:
                        pass
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                    if event.key == pygame.K_LEFT:
                        pass

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            print(event)
        x += x_change

        gameDisplay.fill(white)
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        #moves the block back to the beginning
        if thing_startY > display_height:
            thing_startY = 0 - thing_height
            thing_startX = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y < thing_startY+thing_height:
            print('step 1')
            if x < thing_startX + thing_width and x > thing_startX:
                #print('step 2')
                crash()
            elif x + car_width < thing_startX + thing_width and x + car_width > thing_startX:
                #print('step 2')
                crash()


        things(thing_startX,thing_startY,thing_width,thing_height,block_color)
        thing_startY += thing_speed

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()