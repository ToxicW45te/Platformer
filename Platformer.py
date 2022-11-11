import pygame
pygame.init()

pygame.display.set_caption("easy platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop


     
#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3



#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform
health = 100

#enemy variables
#expos = 200
#eypos = 630
#timer = 0
enemy1=[200, 630, 0]
enemy2=[430, 430, 90]
enemy3=[630, 230, 90]


#----------------------------------Function Definition-----------------------------------------
def enemyMove(enemyInfo):
    #print(enemyInfo)
    enemyInfo[2]+=1
    if enemyInfo[2] <= 60:
        enemyInfo[0] += 1
    elif enemyInfo[2] <= 120:
        enemyInfo[0] -=1
    else:
        enemyInfo[2] = 0 #reset timer
        
def enemyCollide(enemyInfo, playerX, playerY):
    if playerX +20>enemyInfo[0]: #right side of player, left side of enemy
        if playerX < enemyInfo[0]+20: #left side of player, right side of enemy
            if playerY < enemyInfo[1]+20: #top of the player, bottom of the enemy
                if playerY+20 > enemyInfo[1]:
                    return True
    else:
        return False
                    


#end function definition    

while not gameover and health > 0: #GAME LOOP############################################################
    clock.tick(60) #FPS
    
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_RIGHT:
                keys[RIGHT]=True

            elif event.key == pygame.K_UP:
                keys[UP]=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                keys[RIGHT]=False

            elif event.key == pygame.K_UP:
                keys[UP]=False
                
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True

            elif event.key == pygame.K_UP:
                keys[UP]=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False

            elif event.key == pygame.K_UP:
                keys[UP]=False
          
    #physics section--------------------------------------------------------------------
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        direction = LEFT
        
    elif keys[RIGHT]==True:
        vx=3
        direction = RIGHT

    #turn off velocity
    else:
        vx = 0
        #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        isOnGround = False
        direction = UP
    
    
    #function call for enemy movement
    enemyMove(enemy1) 
        
    enemyMove(enemy2)
        
    enemyMove(enemy3)
       
    
    #check collision with enemies
    if enemyCollide(enemy1, xpos, ypos):
        print("hit")
        health -=10
    if enemyCollide(enemy2, xpos, ypos):
        print("hit")
        health -=10
    if enemyCollide(enemy3, xpos, ypos):
        print("hit")
        health -=10
    
    
    #COLLISION
    if xpos>100 and xpos<200 and ypos+40 >750 and ypos+40 <770:
        ypos = 750-40
        isOnGround = True
        vy = 0
    elif xpos>200 and xpos<300 and ypos+40 >650 and ypos+40 <670: 
        ypos = 650-40
        isOnGround = True
        vy = 0
    elif xpos>300 and xpos<400 and ypos+40 >550 and ypos+40 <570:
        ypos = 550-40
        isOnGround = True
        vy = 0
    elif xpos>400 and xpos<500 and ypos+40 >450 and ypos+40 <470:
        ypos = 450-40
        isOnGround = True
        vy = 0
    elif xpos>500 and xpos<600 and ypos+40 >350 and ypos+40 <370:
        ypos = 350-40
        isOnGround = True
        vy = 0
    elif xpos>600 and xpos<700 and ypos+40 >250 and ypos+40 <270:
        ypos = 250-40
        isOnGround = True
        vy = 0
    else:
        isOnGround = False


    
    #stop falling if on bottom of game screen
    if ypos > 760:
        isOnGround = True
        vy = 0
        ypos = 760
    
    #gravity
    if isOnGround == False:
        vy+=.2 #notice this grows over time, aka ACCELERATION
    

    #update player position
    xpos+=vx 
    ypos+=vy
    
  
    # RENDER Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
  
    #draw player
    pygame.draw.rect(screen, (100, 200, 100), (xpos, ypos, 20, 40))
    #draw enemy
    pygame.draw.rect(screen, (255, 255, 255), (enemy1[0], enemy1[1], 20, 20))
    pygame.draw.rect(screen, (255, 255, 255), (enemy2[0], enemy2[1], 20, 20))
    pygame.draw.rect(screen, (255, 255, 255), (enemy3[0], enemy3[1], 20, 20))

   
    
    #first platform
    pygame.draw.rect(screen, (255, 0, 0), (100, 750, 100, 20))
    
    #second platform
    pygame.draw.rect(screen, (255, 165, 0), (200, 650, 100, 20))
    
    #third platform
    pygame.draw.rect(screen, (254, 254, 1), (300, 550, 100, 20))
    
    #fourth platform
    pygame.draw.rect(screen, (0, 255, 0), (400, 450, 100, 20))
    
    #fifth platform
    pygame.draw.rect(screen, (0, 0, 255), (500, 350, 100, 20))
    
    #sixth platform
    pygame.draw.rect(screen, (128, 0, 128), (600, 250, 100, 20))

    
    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
if health <=0:
    print("GAME OVER, YOU DIED!")
pygame.quit()