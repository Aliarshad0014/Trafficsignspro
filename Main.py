import pygame
import easygui

# Initialising the game
pygame.init()

# Creating The Screen
height = 700
width = 400
screen = pygame.display.set_mode((width, height))

# Colors To Be used in the game
gray = (100, 100, 100)
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
brown = (101, 67, 33)

# road and edge markers
road = (155, 0, 100, height)

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

# Car Image
carImg = pygame.image.load('images/car.png')
car_width = carImg.get_width()
car_height = carImg.get_height()
playerX = 173
playerY = 600

def player():
    screen.blit(carImg, (playerX, playerY))

# pedestrian crossing
pedesImg = pygame.image.load('images/pedes.png')
a = 155
b = 5

def pedes():
    pedesImg_scaled = pygame.transform.scale(pedesImg, (100, 100))  # Change the size (50, 50) to the desired size
    screen.blit(pedesImg_scaled, (a, b))

# boolean variable for level_passed
level_passed = False

# Show level 1 start pop-up message
easygui.msgbox("Level 1: Stop At Pedestrian Crossing\nControls: Use Up And Down Arrow Key To Control The Car", title="Level 1")

# game Loop
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

    # draw dotted road line
    dot_spacing = 20  # spacing between dots
    dot_size = 2  # size of dots
    dot_color = white  # color of dots

    # calculate the number of dots needed based on the height of the road
    num_dots = road[3] // dot_spacing

    # calculate the y-coordinate of the first dot
    first_dot_y = road[1] + (road[3] - num_dots * dot_spacing) // 2

    # draw the dotted line
    for i in range(num_dots):
        dot_y = first_dot_y + i * dot_spacing
        pygame.draw.circle(screen, dot_color, (road[0] + road[2] // 2, dot_y), dot_size)

    ped()
    stop()
    pedes()
    player()

    # Displaying level_passed value on the window
    font = pygame.font.SysFont(None, 22)
    text = font.render("Level Passed: " + str(level_passed), True, white)
    screen.blit(text, (10, 10))
    
    pygame.display.update()

    # Check if level is passed and restart game
    if level_passed:
        pygame.time.delay(1000)  # Delay for 1 second
        playerY = 600  # Reset car position to initial

    # Show restart confirmation message box
        choice = easygui.buttonbox("Level Passed! Do you want to restart?", choices=["Yes", "No"])
        if choice == "No":
            running = False
        elif choice == "Yes":
            continue
        else:
            print("Invalid input. Game will exit.") 
            running = False

pygame.quit()
