import pygame
import sys

# Initialising the game
pygame.init()

# Creating The Screen
height = 700
width = 400
screen = pygame.display.set_mode((width, height))

black = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
font = pygame.font.Font(None, 32)
BUTTON_WIDTH = 120
BUTTON_HEIGHT = 50  

start_button_rect = pygame.Rect((width/2 - BUTTON_WIDTH/2, height/2 - BUTTON_HEIGHT), (BUTTON_WIDTH, BUTTON_HEIGHT))
quit_button_rect = pygame.Rect((width/2 - BUTTON_WIDTH/2, height/2 + BUTTON_HEIGHT), (BUTTON_WIDTH, BUTTON_HEIGHT))
howtoplay_button_rect =  pygame.Rect((width/2 - BUTTON_WIDTH/2, height/3 - BUTTON_HEIGHT), (BUTTON_WIDTH, BUTTON_HEIGHT))

# Colors To Be used in the game
gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 240, 60)

# road and edge markers
road = (140, 0, 120, height)
roadmark_width = int(width/80)

# Title and icon
pygame.display.set_caption("Traffic Signs Pro")
icon = pygame.image.load("images/warning.png")
pygame.display.set_icon(icon)

# pedestrian sign
pedImg = pygame.image.load('images/ped.png')
x = 40
y = 150

def ped():
    screen.blit(pedImg, (x, y))

# stop sign 
stopImg = pygame.image.load('images/stop.png')
x1 = 40
y1 = 250

def stop():
    screen.blit(stopImg,(x1,y1))

# Obstacle Img
obImg = pygame.image.load('images/obstacle.png')
c=200
d=200

def obstacle():
    screen.blit(obImg,(c,d))

# Hole Img
holeimg = pygame.image.load('images/hole.png')
e=139
f=340

def hole():
    screen.blit(holeimg,(e,f))

# diversion 
divimg = pygame.image.load('images/diversion.png')
g=141
h=400

def div():
    screen.blit(divimg,(g,h))


# Car Image
carImg = pygame.image.load('images/car.png')
car_width = carImg.get_width()
car_height = carImg.get_height()
playerX = width/2.9
playerY = 600

def player():
    screen.blit(carImg, (playerX, playerY))

# pedestrian crossing
pedesImg = pygame.image.load('images/pedes.png')
a = 150
b = 10

def pedes():
    pedesImg_scaled = pygame.transform.scale(pedesImg, (100, 100))  # Change the size (50, 50) to the desired size
    screen.blit(pedesImg_scaled, (a, b))

# boolean variable for level_passed
level_passed = False


# Draw rectangle at the start of the game
pygame.draw.rect(screen,red, (0,50,width,150))


def draw_menu():
    # Draw the menu screen
    screen.fill(WHITE)

    # Draw the Start button
    start_button_text = font.render("Start", True, black)
    screen.blit(start_button_text, start_button_rect)

    # Draw the how to play button
    howtoplay_button_text = font.render("How To Play", True, black)
    screen.blit(howtoplay_button_text, howtoplay_button_rect)

    # Draw the Quit button
    quit_button_text = font.render("Quit", True, black)
    screen.blit(quit_button_text, quit_button_rect)

    pygame.display.update()

# Draw the menu screen initially
draw_menu()

# game Loop
def game_loop():
    global playerX, playerY
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Check for arrow key events
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if playerY > 0:
                playerY -= 0.1
        if keys[pygame.K_DOWN]:
            if playerY < height - car_height:
                playerY += 0.1
        if keys[pygame.K_LEFT]:
                playerX = 140        
        if keys[pygame.K_RIGHT]:
                playerX = 200


        # Checking if car's final position is below the pedes object
        if playerY > b and playerY < 590:
            level_passed = True

        # Checking if car stops at more than y-200px
        if playerY + car_height > y :
            level_passed = False

        # grass draw
        screen.fill(green)

        # road draw
        pygame.draw.rect(screen, gray, road)
        # Yellow line draw
        pygame.draw.rect(screen,yellow,(width/2 - roadmark_width/2, 0,roadmark_width,height))

        ped()
        stop()
        pedes()
        obstacle()
        hole()
        div()
        player()


        # Displaying level_passed value on the window
        font = pygame.font.SysFont(None, 22)
        text = font.render("Level Passed: " + str(level_passed), True, white)
        screen.blit(text, (10, 10))

        # Show Banner when level passed
        if level_passed:
            pygame.draw.rect(screen, red, (0, 50, width, 150))
            font = pygame.font.SysFont(None, 18)
            text2 = font.render("Level Passed Would you Like to Restart? Press Y or N" ,True,white)
            screen.blit(text2, (49,120))
            # Check if level is passed and restart game
            if level_passed:
                if keys[pygame.K_y]:
                    playerX = width/2.9
                    playerY = 600
                    level_passed = False  # Reset car position to initial
                else:
                    if keys[pygame.K_n]:
                        running = False

        pygame.display.update()

    pygame.quit()

draw_menu()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if start_button_rect.collidepoint(mouse_pos):
                game_loop()
            elif quit_button_rect.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit
            
    pygame.display.update()