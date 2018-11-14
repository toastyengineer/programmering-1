import pygame
import random
import sys
from pygame.locals import *

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0, 0, 40)
FPS = 60
BADDIEMINSIZE = 20
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 2
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 7
ADDNEWPOWERRATE = 20
POWERSIZE = 25
PLAYERMOVERATE = 5


def terminate():
    pygame.quit()
    sys.exit()


def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits
                    terminate()
                return


def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def playerHasCollectedPowerup(playerRect, power):
    for p in power:
        if playerRect.colliderect(p['rect']):
            powerUpSound.play()
            power.remove(p)
            return True
    return False


def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# set up pygame, the window, and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Sponger')
pygame.mouse.set_visible(False)

# set up fonts
font = pygame.font.SysFont(None, 48)

# set up sounds
gameOverSound = pygame.mixer.Sound('gameover.wav')
powerUpSound = pygame.mixer.Sound('powerup.wav')
pygame.mixer.music.load('bgmusic.mp3')


# set up images
backGround = pygame.image.load('bg.png')
playerImage = pygame.image.load('player.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('baddie.png')
powerImage = pygame.image.load('power.png')

# show the "Start" screen
drawText('Dodger', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Press a key to start.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()


topScore = 0
while True:
    # set up the start of the game
    baddies = []
    power = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    powerAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)
    windowSurface.blit(backGround, (0, 0))
    pygame.display.flip()

    while True:  # the game loop runs while the game part is playing
        score += 1  # increase score

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == ord('z'):
                    reverseCheat = True
                if event.key == ord('x'):
                    slowCheat = True
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w'):
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s'):
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == ord('z'):
                    reverseCheat = False
                    score = 0
                if event.key == ord('x'):
                    slowCheat = False
                    score = 0
                if event.key == K_ESCAPE:
                        terminate()

                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False

            if event.type == MOUSEMOTION:
                # If the mouse moves, move the player where the cursor is.
                playerRect.move_ip(event.pos[0] - playerRect.centerx, event.pos[1] - playerRect.centery)

        # Add new baddies at the top of the screen, if needed.
        if not reverseCheat and not slowCheat:
            baddieAddCounter += 1
        if baddieAddCounter == ADDNEWBADDIERATE:
            baddieAddCounter = 0
            baddieSize = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)
            newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH-baddieSize), 0 - baddieSize, baddieSize, baddieSize),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface':pygame.transform.scale(baddieImage, (baddieSize-10, baddieSize)),
                        }

            baddies.append(newBaddie)
        #POWER
        if not reverseCheat and not slowCheat:
            powerAddCounter += 1
        if powerAddCounter == ADDNEWPOWERRATE:
            powerAddCounter = 0
            powerSize = POWERSIZE
            newPower = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH-powerSize), 0 - powerSize, powerSize, powerSize),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface':pygame.transform.scale(powerImage, (powerSize, powerSize)),
                        }

            power.append(newPower)

        # Move the player around.
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)

        # Move the mouse cursor to match the player.
        pygame.mouse.set_pos(playerRect.centerx, playerRect.centery)

        # Move the baddies down.
        for b in baddies:
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat:
                b['rect'].move_ip(0, -5)
            elif slowCheat:
                b['rect'].move_ip(0, 1)
        # Move the powerups down
        for p in power:
            if not reverseCheat and not slowCheat:
                p['rect'].move_ip(0, p['speed'])
            elif reverseCheat:
                p['rect'].move_ip(0, -5)
            elif slowCheat:
                p['rect'].move_ip(0, 1)

        # Delete baddies that have fallen past the bottom.
        for b in baddies[:]:
            if b['rect'].top > WINDOWHEIGHT:
                baddies.remove(b)
        for p in power[:]:
            if p['rect'].top > WINDOWHEIGHT:
                power.remove(p)

        # Draw the game world on the window.
        windowSurface.blit(backGround, (0, 0))

        # Draw the score and top score.
        drawText('Score: %s' % score, font, windowSurface, 10, 0)
        drawText('Top Score: %s' % topScore, font, windowSurface, 10, 40)

        # Draw the player's rectangle
        windowSurface.blit(playerImage, playerRect)

        # Draw each baddie
        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])
        for p in power:
            windowSurface.blit(p['surface'], p['rect'])

        pygame.display.update()

        # Check if any of the baddies have hit the player.
        if playerHasHitBaddie(playerRect, baddies):
            if score > topScore:
                topScore = score  # set new top score
            break

        if playerHasCollectedPowerup(playerRect, power):
            score += 500



        mainClock.tick(FPS)

    # Stop the game and show the "Game Over" screen.
    pygame.mixer.music.stop()
    gameOverSound.play()

    drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    drawText('Press a key to play .', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
    pygame.display.update()
    waitForPlayerToPressKey()

    gameOverSound.stop()
