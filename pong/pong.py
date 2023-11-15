import pygame as p
import math 
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

screenWidth = 900
screenHeight = 600


class hitarea:
    destroy = False
    x = 0
    y = 0
    width = 0
    height = 0
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    



class gameball:
    
    intialBallx = 435
    intialBally = 290
    ball = p.Rect(intialBallx,intialBally,30,30)

    multipler = 6
    ballspeedx = 3
    ballspeedy = 3

    def stop(self):
        self.ballspeedx = 0
        self.ballspeedy = 0
        self.intialBallx = 450
        self.intialBally = 300
    
    def reset(self):
        Xrand = random.choice([-1,1])
        Yrand = random.choice([-1,1])
        self.ballspeedx = 3 * Xrand
        self.ballspeedy = 3 * Yrand


def pyGamePong():
    
    p.init()
    p.font.init()
    GAME_FONT = p.font.SysFont('Comic Sans MS', 60)
    
    gameScore = [0,0]
    pause = False
    # Set the width and height of the screen [width, height]
    size = (screenWidth, screenHeight)
    screen = p.display.set_mode(size)
    intialHumanY= 250
    intialCpuY= 250
    speed = 7

    theBall = gameball()    
    
    p.display.set_caption("basic Python graphics window()")
     
    # Loop until the user clicks the close button.
    running = True 
     
    # Used to manage how fast the screen updates
    clock = p.time.Clock()

    player1 = p.Rect(85, intialCpuY, 30, 150)
    player2 = p.Rect(785, intialHumanY, 30, 150)
  
    # -------- Main Program Loop -----------
    while running:
        # --- Main event loop
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
        
        """ Check for keyboard presses. """
        key = p.key.get_pressed()
        
        if (key[p.K_ESCAPE] == True): 
            running = False
        if (key[p.K_UP] == True):
            if(intialHumanY > 0):
                intialHumanY = intialHumanY - speed
                player2 = p.Rect(785, intialHumanY, 30, 150)
            pass
        if (key[p.K_DOWN] == True): 
            if(intialHumanY < 450):
                intialHumanY = intialHumanY + speed
                player2 = p.Rect(785, intialHumanY, 30, 150)
            pass
        if (key[p.K_LEFT] == True):
            pass
        if (key[p.K_RIGHT] == True):
            pass
        if (key[p.K_SPACE] == True):
            if pause:
                theBall.reset()
                pause = False
            pass

        #check boundaries
        if theBall.intialBallx < 15:
            gameScore[1] = gameScore[1] +1
            theBall.stop()
            pause = True
            intialCpuY = 250
            print(gameScore)
        if theBall.intialBallx > 860:
            gameScore[0] = gameScore[0] +1
            theBall.stop()
            pause = True
            intialCpuY = 250
            print(gameScore)

        if theBall.intialBally < 15 or theBall.intialBally > 560:
            theBall.ballspeedy = theBall.ballspeedy * -1.1

        if abs(theBall.intialBallx - player2.centerx) < 45 and abs(player2.centery - theBall.intialBally) < 75:
            theBall.ballspeedx = theBall.ballspeedx *-1.1
    
        if abs(theBall.intialBallx - player1.centerx) < 45 and abs(player1.centery - theBall.intialBally) < 75:
            theBall.ballspeedx = theBall.ballspeedx *-1.1
        
        if intialCpuY < theBall.intialBally and intialCpuY < 450:
            intialCpuY = intialCpuY + speed 
        
        if intialCpuY + 25 > theBall.intialBally and intialCpuY > 0:
            intialCpuY = intialCpuY - speed 

        theBall.intialBallx = theBall.intialBallx + theBall.ballspeedx
        theBall.intialBally = theBall.intialBally + theBall.ballspeedy
       
        player1 = p.Rect(85, intialCpuY, 30, 150)
       
        if gameScore[0] > 2 or gameScore[1] > 2:
            running = False

        # --- Game logic should go here
        
        # --- Screen-clearing code goes here
     
        # Here, we clear the screen to black. Don't put other drawing commands
        # above this, or they will be erased with this command.
     
        # If you want a background image, replace this clear with blit'ing the
        # background image.
        screen.fill(BLACK)
        
        # --- Drawing code should go here
        p.draw.circle(screen, ORANGE, [theBall.intialBallx,theBall.intialBally], 30)
        p.draw.line(screen, GREEN, [0, 300], [900, 300], 2)
        p.draw.line(screen, GREEN, [100, 0], [100, 600], 2)
        p.draw.line(screen, GREEN, [800, 0], [800, 600], 2)
        p.draw.rect(screen,CYAN,player1)
        p.draw.rect(screen,CYAN,player2)

        if pause:
            winner_text = f"{gameScore[0]} - {gameScore[1]}"
            text_surface = GAME_FONT.render(winner_text,False,GREEN)
            screen.blit(text_surface, (380, 50))

                
        # --- Go ahead and update the screen with what we've drawn.
        p.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
     
    # Close the window and quit.
    p.quit()
    
    return

pyGamePong()