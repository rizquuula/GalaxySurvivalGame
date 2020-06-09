#GalaxySurvival (a 2D shooting game)
#Created by: Muhammad Razif Rizqullah
#From: Lampung University
#Under Licensed of LinkGish coorp
#Write in 2 weeks work
#Free to share

import pygame,sys,random
from pygame.locals import *

FPS = 50
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
CELLSIZE = 25
BOARDX = WINDOWWIDTH/CELLSIZE/2
BOARDY = WINDOWHEIGHT/CELLSIZE
LEFTMARGIN = int(WINDOWWIDTH - (BOARDX*CELLSIZE))/2
TOPMARGIN  = 0 
assert (WINDOWHEIGHT+WINDOWWIDTH)%CELLSIZE == 0 

#RGB            R    G    B
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
LIGHTRED    = (175,  20,  20)
GREEN       = (  0, 155,   0)
LIGHTGREEN  = ( 20, 175,  20)
BLUE        = (  0,   0, 155)
LIGHTBLUE   = ( 20,  20, 175)
YELLOW      = (155, 155,   0)
LIGHTYELLOW = (175, 175,  20)

BORDERCOLOR     = BLUE
BGCOLOR         = BLACK
TEXTCOLOR       = WHITE
TEXTSHADOWCOLOR = GRAY
COLORS          = (BLUE,GREEN,RED,YELLOW,WHITE,GRAY,LIGHTRED,LIGHTGREEN,LIGHTBLUE,LIGHTYELLOW)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
STOP = 'stop'
START = 0

def main():
    global FPSCLOCK,DISPLAYSURF
    global FONT,gameOverFont,startFONT
    global imgPLANE, imgBULLET, imgENEMY1, imgENEMY2, imgENEMY3, imgENEMY4, START_GAME, BGstart, SETT, HOWto, MAINMENU_B, MAINMENU_W, EXITb, EXITw
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
    FONT = pygame.font.Font('asset/ArtificeSSK.ttf', 18)
    gameOverFont = pygame.font.Font('asset/ArtificeSSK.ttf', 150)
    startFONT = pygame.font.Font('asset/ArtificeSSK.ttf', 100)
    pygame.display.set_caption('Galaxy Survival 1.00')
    imgPLANE  = pygame.image.load('asset/JETPLANE.png')
    imgPLANE  = pygame.transform.smoothscale(imgPLANE, (CELLSIZE*2, CELLSIZE*2))
    imgBULLET = pygame.image.load('asset/gem7.png')
    imgBULLET = pygame.transform.smoothscale(imgPLANE, (int(CELLSIZE/3), CELLSIZE))
    imgENEMY1 = pygame.image.load('asset/ENEMY1.png')
    imgENEMY1 = pygame.transform.smoothscale(imgENEMY1, (CELLSIZE, CELLSIZE))
    imgENEMY2 = pygame.image.load('asset/ENEMY2.png')
    imgENEMY2 = pygame.transform.smoothscale(imgENEMY2, (CELLSIZE, CELLSIZE))
    imgENEMY3 = pygame.image.load('asset/ENEMY3.png')
    imgENEMY3 = pygame.transform.smoothscale(imgENEMY3, (CELLSIZE, CELLSIZE))
    imgENEMY4 = pygame.image.load('asset/ENEMY4.png')
    imgENEMY4 = pygame.transform.smoothscale(imgENEMY4, (CELLSIZE, CELLSIZE))
    START_GAME = pygame.image.load('asset/startgame.png')
    SETT = pygame.image.load('asset/setting.png')
    HOWto = pygame.image.load('asset/howtoplay.png')
    MAINMENU_B = pygame.image.load('asset/mainmenub.png')
    MAINMENU_W = pygame.image.load('asset/mainmenuw.png')
    EXITb = pygame.image.load('asset/EXITb.png')
    EXITw = pygame.image.load('asset/EXITw.png')
    BGstart = pygame.image.load('asset/BGstart.png')
    startGame()
    while True:
        runGame()
        GameOver()
    
        
def startGame():
    degree=0
    degree1=180
    degree2=90
    while True:
        DISPLAYSURF.fill(GRAY)
        DISPLAYSURF.blit(BGstart,(0,0))
        three_menu()
        start_text()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if pygame.Rect(WINDOWWIDTH*5/6,WINDOWHEIGHT*5.7/8,
                               START_GAME.get_width(),START_GAME.get_height()).collidepoint(mousex, mousey):
                    return
                elif pygame.Rect(WINDOWWIDTH*5/6,WINDOWHEIGHT*6.35/8,
                               START_GAME.get_width(),START_GAME.get_height()).collidepoint(mousex, mousey):
                    howtoplay()
                elif pygame.Rect(WINDOWWIDTH*5/6,WINDOWHEIGHT*7/8,
                               START_GAME.get_width(),START_GAME.get_height()).collidepoint(mousex, mousey):
                    terminate()
            
        compass = pygame.image.load('asset/compass.png')
        compass = pygame.transform.scale(compass, (CELLSIZE*8, CELLSIZE*8))
        compassSurf = pygame.transform.rotate(compass, degree)
        compassRect = compassSurf.get_rect()
        compassRect.center = (WINDOWWIDTH/6,WINDOWHEIGHT*3/4)
        DISPLAYSURF.blit(compassSurf,compassRect)
        degree+=15
            
        compass1 = pygame.image.load('asset/compass1.png')
        compass1 = pygame.transform.scale(compass1, (CELLSIZE*10, CELLSIZE*10))
        compassSurf1 = pygame.transform.rotate(compass1, degree1)
        compassRect1 = compassSurf1.get_rect()
        compassRect1.center = (WINDOWWIDTH/3,WINDOWHEIGHT*3/4)
        DISPLAYSURF.blit(compassSurf1,compassRect1)
        degree1-=25

        compass2 = pygame.image.load('asset/compass2.png')
        compass2 = pygame.transform.scale(compass2, (CELLSIZE*5, CELLSIZE*5))
        compassSurf2 = pygame.transform.rotate(compass2, degree2)
        compassRect2 = compassSurf2.get_rect()
        compassRect2.center = (WINDOWWIDTH*3/12,WINDOWHEIGHT*5/8)
        DISPLAYSURF.blit(compassSurf2,compassRect2)
        degree2+=45
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)        

def runGame():
    
    startx  = startxx =int( (LEFTMARGIN/CELLSIZE) + (BOARDX-3)/2)
    starty  = startyy = int((TOPMARGIN+BOARDY-1))
    planeCoords = [{'x': startx,'y':starty}]
    bulletCoords = [{'x': startxx,'y':startyy}]
    direction = STOP
    ENEMY1 = getRandomLocation()
    ENEMY2 = getRandomLocation()
    ENEMY3 = getRandomLocation()
    ENEMY4 = getRandomLocation()
    ENEMY5 = getRandomLocation()
    score= 0
    ENEMY1['y'] = ENEMY1['y']
    ENEMY2['y'] = ENEMY2['y']
    ENEMY3['y'] = ENEMY3['y']
    ENEMY4['y'] = ENEMY4['y']
    ENEMY5['y'] = ENEMY5['y']

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_LEFT or event.key == K_a:
                    direction = LEFT
                elif event.key == K_RIGHT or event.key == K_d:
                    direction = RIGHT
                elif event.key == K_UP or event.key == K_w:
                    direction = UP
                elif event.key == K_LCTRL:
                    direction = STOP
                elif event.key == K_ESCAPE:
                    terminate()
                else:
                    direction = STOP
            elif event.type == pygame.KEYUP:
                if event.key == K_UP or event.key == K_w:
                    direction = STOP
                elif event.key == K_LEFT or event.key == K_a:
                    direction = STOP
                elif event.key == K_RIGHT or event.key == K_d:
                    direction = STOP
    
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if pygame.Rect(WINDOWWIDTH*5/6,WINDOWHEIGHT*6.35/8,
                               START_GAME.get_width(),START_GAME.get_height()).collidepoint(mousex, mousey):
                    return main()
                elif pygame.Rect(WINDOWWIDTH*5/6,WINDOWHEIGHT*7/8,
                               START_GAME.get_width(),START_GAME.get_height()).collidepoint(mousex, mousey):
                    terminate()

            #ENEMY_Control
                    
        if bulletCoords[START]['x'] == ENEMY1['x'] and bulletCoords[START]['y'] == ((WINDOWHEIGHT/CELLSIZE) - 3):
            ENEMY1 = getRandomLocation()
            score+=1
        elif bulletCoords[START]['x'] == ENEMY2['x'] and bulletCoords[START]['y'] == ((WINDOWHEIGHT/CELLSIZE) - 3):
            ENEMY2 = getRandomLocation()
            score+=1
        elif bulletCoords[START]['x'] == ENEMY3['x'] and bulletCoords[START]['y'] == ((WINDOWHEIGHT/CELLSIZE) - 3):
            ENEMY3 = getRandomLocation()
            score+=1
        elif bulletCoords[START]['x'] == ENEMY4['x'] and bulletCoords[START]['y'] == ((WINDOWHEIGHT/CELLSIZE) - 3):
            ENEMY4 = getRandomLocation()
            score+=1
        elif bulletCoords[START]['x'] == ENEMY5['x'] and bulletCoords[START]['y'] == ((WINDOWHEIGHT/CELLSIZE) - 3):
            ENEMY5 = getRandomLocation()
            score+=1

        vel1=0.17
        vel2=0.2
        vel3=0.07
        vel4=0.12
        vel5=0.19

        ENEMY1['y']+=vel1
        ENEMY2['y']+=vel2
        ENEMY3['y']+=vel3
        ENEMY4['y']+=vel4
        ENEMY5['y']+=vel5
           
            
            #PLAYER_Control
        if direction == LEFT and (planeCoords[START]['x'])>LEFTMARGIN/CELLSIZE:
            MOVETO = {'x': planeCoords[START]['x']-1, 'y': planeCoords[START]['y']}
            BulletMOVE = MOVETO
        elif direction == RIGHT and (planeCoords[START]['x'])<(LEFTMARGIN/CELLSIZE+(BOARDX-1)):
            MOVETO = {'x': planeCoords[START]['x']+1, 'y': planeCoords[START]['y']}
            BulletMOVE = MOVETO
        elif direction == STOP:
            MOVETO = {'x': planeCoords[START]['x'], 'y': planeCoords[START]['y']}
            BulletMOVE = MOVETO
        elif direction == UP and bulletCoords[START]['y']>bulletCoords[START]['y']-4:
            BulletMOVE = {'x': bulletCoords[START]['x'], 'y': bulletCoords[START]['y']-2}
        elif direction == DOWN and (planeCoords[START]['x'])<(LEFTMARGIN/CELLSIZE+(BOARDX)):
            BulletMOVE = {'x': bulletCoords[START]['x'], 'y': bulletCoords[START]['y']+1}
        else:
            BulletMOVE = None
            MOVETO = None

            #HOW_to_LOSE
        if planeCoords[START]['y'] == int(ENEMY1['y']) or planeCoords[START]['y'] == int(ENEMY2['y']) or planeCoords[START]['y'] == int(ENEMY3['y']) or planeCoords[START]['y'] == int(ENEMY4['y']) or planeCoords[START]['y'] == int(ENEMY5['y']):
            return
        
        bulletCoords.insert(0, BulletMOVE)
        planeCoords.insert(0, MOVETO)
        del planeCoords[-1]
        del bulletCoords[1]
        DISPLAYSURF.fill(BLACK)
        drawBoard()
        two_menu()
        #gridline()
        drawEnemy345(ENEMY1)
        drawEnemy12(ENEMY2)
        drawEnemy345(ENEMY3)
        drawEnemy12(ENEMY4)
        drawEnemy345(ENEMY5)
        drawBullet(bulletCoords)
        drawPlane(planeCoords)
        drawScore(score)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def drawEnemy12(coord):
    imgLIST_ENEMY = (imgENEMY1, imgENEMY2)
    imgENEMY = random.sample(imgLIST_ENEMY,1)[0]
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    enemyRect = imgENEMY.get_rect()
    enemyRect.topleft = (x,y)
    DISPLAYSURF.blit(imgENEMY,enemyRect)

def drawEnemy345(coord):
    imgLIST_ENEMY1 = (imgENEMY3, imgENEMY4)
    imgENEMY1 = random.sample(imgLIST_ENEMY1,1)[0]
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    enemyRect = imgENEMY1.get_rect()
    enemyRect.topleft = (x,y)
    DISPLAYSURF.blit(imgENEMY1,enemyRect)
    
def drawBullet(bulletCoords):
    for coord in bulletCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        bulletRect = imgBULLET.get_rect()
        bulletRect.topleft = (x+(CELLSIZE/3),y+(CELLSIZE/2))
        DISPLAYSURF.blit(imgBULLET,bulletRect)

def drawPlane(planeCoords):
    for coord in planeCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        planeRect = imgPLANE.get_rect()
        planeRect.topleft = (x-(CELLSIZE/2),y-(CELLSIZE))
        DISPLAYSURF.blit(imgPLANE,planeRect)

def drawScore(score):
    scoreSurf = FONT.render('Score: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - (LEFTMARGIN*3/4), WINDOWHEIGHT/16)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

def drawBoard():
    imgBGR = pygame.image.load('asset/BGimg.png')
    imgBGR = pygame.transform.scale(imgBGR,(WINDOWWIDTH,WINDOWHEIGHT))                          
    imgBGRRect = imgBGR.get_rect()
    imgBGRRect.topleft = (0,0)
    DISPLAYSURF.blit(imgBGR,imgBGRRect)

    imgBG = pygame.image.load('asset/BG.jpg')
    imgBG = pygame.transform.scale(imgBG,(int(CELLSIZE*BOARDX), int(CELLSIZE*BOARDY)))
    imgBGRect = imgBG.get_rect()
    imgBGRect.topleft = (LEFTMARGIN,TOPMARGIN)
    DISPLAYSURF.blit(imgBG,imgBGRect)

    pygame.draw.rect(DISPLAYSURF, GRAY, (LEFTMARGIN-2, TOPMARGIN - 7, (BOARDX * CELLSIZE+5), (BOARDY * CELLSIZE+CELLSIZE)), 5)
def getRandomLocation():
    return {'x': random.randint((LEFTMARGIN/CELLSIZE),((LEFTMARGIN/CELLSIZE)+BOARDX-1)),'y': 0}#random.randint(0, (WINDOWHEIGHT/CELLSIZE*3/4))}

def terminate():
    pygame.quit()
    sys.exit()

def gridline():
    for x in range (0, WINDOWWIDTH,CELLSIZE):
        pygame.draw.line(DISPLAYSURF, GRAY,(x,0),(x,WINDOWHEIGHT))
    for y in range (0, WINDOWHEIGHT,CELLSIZE):
        pygame.draw.line(DISPLAYSURF, GRAY,(0,y),(WINDOWWIDTH,y))

def start_text():
    RANDCOLOR = random.sample(COLORS,1)[0]
    RANDCOLOR1 = random.sample(COLORS,1)[0]
        
    startSurf = startFONT.render('GALAXY', True, RANDCOLOR)
    startRect = startSurf.get_rect()
    startRect.topleft = (WINDOWWIDTH / 6, WINDOWHEIGHT/4)
    DISPLAYSURF.blit(startSurf, startRect)
    
    start1Surf = startFONT.render('SURVIVAL', True, RANDCOLOR1)
    start1Rect = start1Surf.get_rect()
    start1Rect.topleft = (WINDOWWIDTH / 3, WINDOWHEIGHT*2/5)
    DISPLAYSURF.blit(start1Surf, start1Rect)

def three_menu():
    DISPLAYSURF.blit(START_GAME,(WINDOWWIDTH*5/6,WINDOWHEIGHT*5.7/8))
    DISPLAYSURF.blit(HOWto,(WINDOWWIDTH*5/6,WINDOWHEIGHT*6.35/8))
    DISPLAYSURF.blit(EXITw,(WINDOWWIDTH*5/6,WINDOWHEIGHT*7/8))

def two_menu():
    DISPLAYSURF.blit(MAINMENU_W,(WINDOWWIDTH*5/6,WINDOWHEIGHT*6.35/8))
    DISPLAYSURF.blit(EXITw,(WINDOWWIDTH*5/6,WINDOWHEIGHT*7/8))

def howtoplay():
    while True:
        FONTsize = 25
        FS = 15
        descFONT = pygame.font.Font('asset/ArtificeSSK.ttf', FONTsize)
        howtoFONT = pygame.font.Font('asset/FACEBOLF.OTF', FS)
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(descFONT.render("How to play the game",True,(BLACK)),(50,50))
        DISPLAYSURF.blit(howtoFONT.render("Game description and guide:",True,(BLACK)),(50,50+(2*FONTsize)))
        DISPLAYSURF.blit(howtoFONT.render("Galaxy Survival is a shooting game that the goal is you need to fight and defeat all enemy",True,(BLACK)),(50,50+(2*FONTsize)+FS))
        DISPLAYSURF.blit(howtoFONT.render("in the field. In this game, you just have one life, so when you failed to kill an enemy and let it",True,(BLACK)),(50,50+(2*FONTsize)+2*FS))
        DISPLAYSURF.blit(howtoFONT.render("passed you, you will be die and game over. The enemy have different speed, you need to think ",True,(BLACK)),(50,50+(2*FONTsize)+3*FS))
        DISPLAYSURF.blit(howtoFONT.render("which one is your priority first cause some enemy will move faster and make you die easily.",True,(BLACK)),(50,50+(2*FONTsize)+4*FS))
        
        DISPLAYSURF.blit(howtoFONT.render("Movement:",True,(BLACK)),(50,50+(3*FONTsize)+5*FS))
        DISPLAYSURF.blit(howtoFONT.render("- press arrow left and right or button A and button D to move the plane horizontally",True,(BLACK)),(50,50+(3*FONTsize)+6*FS))
        DISPLAYSURF.blit(howtoFONT.render("- press arrow up or button W to fire the bullet ",True,(BLACK)),(50,50+(3*FONTsize)+7*FS))
        DISPLAYSURF.blit(howtoFONT.render("- press button ESC to close Galaxy Survival",True,(BLACK)),(50,50+(3*FONTsize)+8*FS))
        
        DISPLAYSURF.blit(howtoFONT.render("Tips and Trick",True,(BLACK)),(50,50+(4*FONTsize)+9*FS))
        DISPLAYSURF.blit(howtoFONT.render("- Dont hold arrow up or button W while firing, because its make bullet stop recharging ",True,(BLACK)),(50,50+(4*FONTsize)+10*FS))
        DISPLAYSURF.blit(howtoFONT.render("- Press other button such as left CTRL or space to recharge bullet faster ",True,(BLACK)),(50,50+(4*FONTsize)+11*FS))
        
        DISPLAYSURF.blit(EXITb,(WINDOWWIDTH*5/6,WINDOWHEIGHT*7/8))
        DISPLAYSURF.blit(MAINMENU_B,(WINDOWWIDTH*5/6,WINDOWHEIGHT*6.35/8))
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if pygame.Rect(WINDOWWIDTH*5/6,WINDOWHEIGHT*6.35/8,
                               START_GAME.get_width(),START_GAME.get_height()).collidepoint(mousex, mousey):
                    return startGame()
                elif event.type == pygame.QUIT or pygame.Rect(WINDOWWIDTH*5/6,WINDOWHEIGHT*7/8,
                                                              START_GAME.get_width(),START_GAME.get_height()).collidepoint(mousex, mousey):
                    terminate()
            
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def GameOver():
    overSurf = gameOverFont.render('Over', True, WHITE)
    overRect = overSurf.get_rect()
    overRect.midtop = (WINDOWWIDTH / 2, WINDOWHEIGHT/2)
    DISPLAYSURF.blit(overSurf, overRect)
    
    gameSurf = gameOverFont.render('Game', True, WHITE)
    gameRect = gameSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, WINDOWHEIGHT/4)
    DISPLAYSURF.blit(gameSurf, gameRect)

    CONTINUEFONT = pygame.font.Font('asset/FACEBOLF.OTF', 18)
    clickSurf = CONTINUEFONT.render('Press space to start a new game', True, WHITE)
    clickRect = clickSurf.get_rect()
    clickRect.topleft = (WINDOWWIDTH/10, WINDOWHEIGHT*7/8)
    DISPLAYSURF.blit(clickSurf, clickRect)
    
    pygame.time.delay(1000)
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if pygame.Rect(WINDOWWIDTH*5/6,WINDOWHEIGHT*6.35/8,
                               START_GAME.get_width(),START_GAME.get_height()).collidepoint(mousex, mousey):
                    return main()
                elif pygame.Rect(WINDOWWIDTH*5/6,WINDOWHEIGHT*7/8,
                               START_GAME.get_width(),START_GAME.get_height()).collidepoint(mousex, mousey):
                    terminate()
            elif event.type == pygame.KEYUP:
                if event.key == K_SPACE:
                    return
               

if __name__ == '__main__':
    main()

