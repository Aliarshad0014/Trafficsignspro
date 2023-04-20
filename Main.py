import pygame
import sys

# Initialising the game
pygame.init()

# Creating The Screen
height = 700
width = 400
screen = pygame.display.set_mode((width, height))

# Menu bottons height and width 
font = pygame.font.Font(None, 32)
button_width = 120
button_height = 50  

start_button_rect = pygame.Rect((170,259), (button_width, button_height))
quit_button_rect = pygame.Rect((175,420), (button_width, button_height))
how_to_play_rect =  pygame.Rect((140,340), (button_width, button_height))
ok_button_rect = pygame.Rect((170,600), (button_width, button_height))
Sedan_rect = pygame.Rect((30, 600), (button_width, button_height))
Suv_rect = pygame.Rect((180, 600), (button_width, button_height))
Sports_rect = pygame.Rect((298, 600), (button_width, button_height))

# Colors To Be used in the game
gray = (100, 100, 100)
green = (69,139,116)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 240, 60)
black = (0, 0, 0)
white = (255, 255, 255)

# road and edge markers
road = (100, 0, 200, height)
roadmark_width = int(width/80)

# Title and icon
pygame.display.set_caption("Traffic Signs Pro")
icon = pygame.image.load("images/warning.png")
pygame.display.set_icon(icon)

# pedestrian sign
pedImg = pygame.image.load('images/ped.png')
x = 25
y = 175

def ped():
    screen.blit(pedImg, (x, y))

# stop sign 
stopImg = pygame.image.load('images/stop.png')
x1 = 25
y1 = 250

def stop():
    screen.blit(stopImg,(x1,y1))

# Obstacle Img
obImg = pygame.image.load('images/obstacle.png')
c=220
d=200
ob_rect = pygame.Rect(c, d, obImg.get_width(), obImg.get_height())

def obstacle():
    screen.blit(obImg,(c,d))

# Hole Img
holeimg = pygame.image.load('images/hole.png')
e=125
f=340
hole_rect = pygame.Rect(e, f, holeimg.get_width(), holeimg.get_height())

def hole():
    screen.blit(holeimg,(e,f))

# diversion 
divimg = pygame.image.load('images/diversion.png')
g=125
h=400
div_rect = pygame.Rect(g, h, divimg.get_width(), divimg.get_height())

def div():
    screen.blit(divimg,(g,h))


# Car Image
carImg = pygame.image.load('images/car.png')
car_width = carImg.get_width()
car_height = carImg.get_height()
playerX = width/3.3
playerY = 600

def player():
    screen.blit(carImg, (playerX, playerY))

# pedestrian crossing
pedesImg = pygame.image.load('images/pedes.png')
pedesImg_scaled = pygame.transform.scale(pedesImg, (100, 100))
a = 150
b = 10
pedes_rect = pygame.Rect(a, b+25, pedesImg_scaled.get_width(), pedesImg_scaled.get_height() - 50)

def pedes():
    screen.blit(pedesImg_scaled, (a, b))

# boolean variable for level_passed
level_passed = False

# Draw rectangle at the start of the game
pygame.draw.rect(screen,red, (0,50,width,150))

def level_failed():
    global playerX, level_passed, playerY
    pygame.draw.rect(screen, red, (0, 200, width, 150))
    font = pygame.font.SysFont(None, 18)
    text2 = font.render("Level Failed Would you Like to Restart? Press Y or N" ,True,white)
    screen.blit(text2, (49,265))
    pygame.display.update()
    # Check for arrow key events
    keys = pygame.key.get_pressed()
    if not level_passed:
        if keys[pygame.K_y]:
            playerX = width/3.3
            playerY = 600
            level_passed = False  # Reset car position to initial
        elif keys[pygame.K_n]:
            pygame.quit()

def draw_menu():
    # Draw the menu background image
    menu_bg_image = pygame.image.load("images/TFPF.png")
    screen.blit(menu_bg_image,(0,0))

    # Draw the Start button
    start_button_text = font.render("Start", True, black)
    screen.blit(start_button_text, start_button_rect)

    # Draw the how to play button
    howtoplay_button_text = font.render("How To Play", True, black)
    screen.blit(howtoplay_button_text, how_to_play_rect)

    # Draw the Quit button
    quit_button_text = font.render("Quit", True, black)
    screen.blit(quit_button_text, quit_button_rect)

    # Draw the Sedan button
    Sedan_text = font.render("Sedan", True, black)
    screen.blit(Sedan_text, Sedan_rect)

    # Draw the Suv Button
    Suv_text = font.render("Suv", True, black)
    screen.blit(Suv_text, Suv_rect)

    # Draw the Sports Button
    Sports_text = font.render("Sports", True, black)
    screen.blit(Sports_text, Sports_rect)

    pygame.display.update()


def draw_how_to_play_menu():
    menu_bg_image = pygame.image.load("images/HTPF.png")
    screen.blit(menu_bg_image,(0,0))

    # Draw the Start button
    ok_button_text = font.render("OK", True, black)
    screen.blit(ok_button_text, ok_button_rect)


def game_loop():
    global playerX, playerY, level_passed
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
            playerX = 120
        if keys[pygame.K_RIGHT]:
            playerX = 220

        # grass draw
        screen.fill(green)

        # road draw
        pygame.draw.rect(screen, gray, road)
        # Yellow line draw
        pygame.draw.rect(screen, yellow, (width/2 - roadmark_width/2, 0, roadmark_width, height))

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
            pygame.draw.rect(screen, red, (0, 200, width, 150))
            font = pygame.font.SysFont(None, 18)
            text2 = font.render("Level Passed Would you Like to Restart? Press Y or N" ,True,white)
            screen.blit(text2, (49,265))
            # Check if level is passed and restart game
            if level_passed:
                if keys[pygame.K_y]:
                    playerX = width/3.3
                    playerY = 600
                    level_passed = False  # Reset car position to initial
                else:
                    if keys[pygame.K_n]:
                        running = False

        # Checking if car's final position is below the pedes object
        if playerY > b and playerY < 300:
            level_passed = True

        # Checking if car stops at more than a certain point
        if playerY + car_height > 155:
            level_passed = False

        player_rect = pygame.Rect(playerX, playerY, carImg.get_width(), carImg.get_height())
        # Check for collision
        if player_rect.colliderect(hole_rect) or player_rect.colliderect(ob_rect) or player_rect.colliderect(pedes_rect) or player_rect.colliderect(div_rect):
            level_passed = False
            level_failed()
   
        pygame.display.update()

    pygame.quit()

def main_menu_loop():
    global carImg
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button_rect.collidepoint(mouse_pos):
                    game_loop()

                elif how_to_play_rect.collidepoint(mouse_pos):
                    draw_how_to_play_menu()

                elif ok_button_rect.collidepoint(mouse_pos):
                    draw_menu()
                    
                elif Sedan_rect.collidepoint(mouse_pos):
                    carImg = pygame.image.load('images/HTP.png')

                elif Suv_rect.collidepoint(mouse_pos):
                    carImg = pygame.image.load('images/car3.png')

                elif Sports_rect.collidepoint(mouse_pos):
                    carImg = pygame.image.load('images/car2.png')
                
                elif quit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit
        pygame.display.update()


draw_menu()
main_menu_loop()
            
    
    