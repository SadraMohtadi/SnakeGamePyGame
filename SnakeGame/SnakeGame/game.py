import pygame
import time
import random
pygame.init()
width , height = 400,400
backgroundColor = (52, 140, 49)
gameScreen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")

x,y = 200,200
deltaX,deltaY = 10,0
foodX,foodY = random.randrange(0 , width)//10*10,random.randrange(0 , height)//10*10
body_list  = [(x,y)]
clock = pygame.time.Clock()

gameOver = False

fontSize25 = pygame.font.SysFont("bahnschrift",25)
fontSize15 = pygame.font.SysFont("bahnschrift",15)
def snake():
    global x,y ,foodX , foodY , gameOver
    x = (x + deltaX)%width
    y = (y + deltaY)%height
    if ((x,y) in body_list):
        gameOver =True
        return
    body_list.append((x,y))
    if (foodX == x and foodY == y):
        while((foodX,foodY) in body_list):
            foodX,foodY = random.randrange(0 , width)//10*10,random.randrange(0 , height)//10*10
    else:
        del body_list[0]        
    gameScreen.fill(backgroundColor)
    score = fontSize15.render("Score: "+str(len(body_list)),True,(255,255,255))
    gameScreen.blit(score, [0,0])
    pygame.draw.rect(gameScreen, (247, 51, 14), [foodX,foodY, 10 ,10])
    for (i,j) in body_list:
         pygame.draw.rect(gameScreen, (0, 102, 255), [i,j, 10 ,10])
    pygame.display.update()
while True :
    if(gameOver):
        gameScreen.fill(backgroundColor)
        msg = fontSize25.render("GAME OVER!" , True, (255,255,255))
        msg2 = fontSize15.render("App will close in 10 Seconds" , True , (255,255,255))
        gameScreen.blit(msg, [width//3, height//3])
        gameScreen.blit(msg2,[115, 170])
        pygame.display.update()
        time.sleep(10)
        pygame.quit()
        quit()
    events = pygame.event.get()
    for event in events:
		
        if(event.type == pygame.QUIT):
           pygame.quit() 
           quit()
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_LEFT):
                if(deltaX != 10):
                   deltaX = -10
                deltaY = 0
            elif(event.key == pygame.K_RIGHT):
                if(deltaX != -10):
                   deltaX = 10
                deltaY = 0
            elif(event.key == pygame.K_UP):
                if(deltaY != 10):
                   deltaY = -10
                deltaX = 0
            elif(event.key == pygame.K_DOWN):
                if(deltaY != -10):
                  deltaY = 10
                deltaX = 0
            elif(event.key == pygame.K_e):
                gameOver = True
            else:
                continue    
            snake() 
    if (not events):                  
        snake()   
    clock.tick(10)    	
