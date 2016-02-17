import spritesheet_handler, pygame
pygame.init()

#Base class for all beings in the game.
class Olio():
    def __init__(self,posX,posY,Sprite, SpriteWidth, SpriteHeight):
        #Each character has a position, and a sprite sheet.
        self.__x = posX
        self.__y = posY
        self.__sprites = spritesheet_handler.spritesheet(Sprite)
        #self.__n = 0
        self.__spriteWidth = SpriteWidth
        self.__spriteHeight = SpriteHeight
        #self.__runner = SpriteStripAnim(Sprite,pygame.Rect(216,2,41,351),5)
        self.__leftruns = [(216,0,41,65),
                           (216,72,41,65),
                           (216,144,41,67),
                           (216,215,37,68),
                            (216,287,41,64)]

    def __get_anims(SpritePosList):
        for column in SpritePosList:
            self.__anims.append

    #The function for drawing the character.
    def __draw__(self, gameDisplay,moveX,moveY):
        image = self.__sprites.image_at((0,0,41,65))
        if moveY > 0:
            try:
                image = self.__sprites.image_at(self.__leftruns[self.__n])
                self.__n += 1
            except IndexError:
                self.__n = 0
            #image = self.__runner.
        #elif moveY != 0:
        gameDisplay.blit(image,(self.__x,self.__y))
        #gameDisplay.blit(self.__sprites.image_at(pygame.Rect(1,2,40,64)),(self.__x,self.__y))

    #Move character on the X-axis.
    def __move_x_axis__(self, moveAmount):
        self.__x += moveAmount

    #Move character on the Y-axis.
    def __move_y_axis__(self, moveAmount):
        self.__y += moveAmount

    #Function for handling the animation. Work in progress.
    def __animation(self):
        self.__runner

#Class of the Player character. Derived from the base character class Olio.
class main_dude(Olio):
    def __nothing(self):
        pass
    '''
    def __init__(self,posX,posY,Sprite):
        self.__x = posX
        self.__y = posY
        self.__sprites = spritesheet_handler.spritesheet(Sprite)'''


#class enemy(olio):
