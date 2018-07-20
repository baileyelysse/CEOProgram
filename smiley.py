"""
title: smiley.py
author: Bailey Patterson
date: 7/20/18 9:35 AM
"""

# Import a library of functions called 'pygame'
import pygame

# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 215, 10)
BROWN = (102, 51, 0)
ORANGE = (255, 128, 0)

PI = 3.141592653
x_coord, x_speed, y_coord, y_speed = 0, 0, 0, 0
ball_pos_x, ball_pos_y = 1200, 1110
ball_speed_x, ball_speed_y = 0, 50

# Set the height and width of the screen
size = (2000, 2500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Move Stick Figure")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()


def draw_stick_figure(screen, x, y):
    # head shape
    pygame.draw.ellipse(screen, YELLOW, [800 + x, 75 + y, 1025, 1025])
    # eyes and mouth
    pygame.draw.ellipse(screen, BLACK, [1100 + x, 500 + y, 75, 150])
    pygame.draw.ellipse(screen, BLACK, [1450 + x, 500 + y, 75, 150])
    pygame.draw.arc(screen, BLACK, [1100 + x, 800 + y, 150, 50], PI, 0, 25)
    # body
    pygame.draw.line(screen, BLACK, [1300 + x, 1100 + y], [1300 + x, 1150 + y], 4)
    # right arm
    pygame.draw.line(screen, BLACK, [1300 + x, 1125 + y], [1400 + x, 1150 + y], 4)
    # left arm
    pygame.draw.line(screen, BLACK, [1300 + x, 1125 + y], [1200 + x, 1150 + y], 4)
    pygame.draw.line(screen, BLACK, [1300 + x, 1150 + y], [1325 + x, 1250 + y], 4)
    pygame.draw.line(screen, BLACK, [1300 + x, 1150 + y], [1275 + x, 1250 + y], 4)


def draw_stick(screen, x, y):
    pygame.draw.line(screen, BROWN, [1400 + x, 1160 + y], [1400 + x, 1125 + y], 3)


def draw_lollipop(screen, x, y):
    pygame.draw.circle(screen, ORANGE, (x, y), 20)


# Loop as long as done == False
while not done:
    if ball_pos_y > (1200 + y_coord):
        ball_speed_y = -55
    if ball_pos_y < (1190 + y_coord):
        ball_speed_y = 55
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -50
            elif event.key == pygame.K_RIGHT:
                x_speed = 50
            elif event.key == pygame.K_UP:
                y_speed = -50
            elif event.key == pygame.K_DOWN:
                y_speed = 50
        elif event.type == pygame.KEYUP:
            x_speed = 0
            y_speed = 0

    # All drawing code happens after the for loop and but
    # inside the main while not done loop.

    # Clear the screen and set the screen background
    screen.fill(WHITE)
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    ball_pos_y = ball_pos_y + ball_speed_y
    ball_pos_x = x_coord + 1200

    draw_stick_figure(screen, x_coord, y_coord)
    draw_stick(screen, ball_pos_x, ball_pos_y)
    draw_lollipop(screen, ball_pos_x, ball_pos_y)

    # Draw on the screen a line from (0,0) to (100,100)
    # 5 pixels wide.
    # pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)

    # Draw on the screen a lines from (0,10) to (100,110)
    # 5 pixels wide.
    # pygame.draw.line(screen, RED, [0, 10], [100, 110], 5)

    # Draw a rectangle
    # pygame.draw.rect(screen, BLACK, [20, 20, 250, 100], 2)

    # Draw an ellipse, using a rectangle as the outside boundaries
    # pygame.draw.ellipse(screen, BLACK, [120, 120, 200, 200], 40)

    # Draw a filled in ellipse, using a rectangle as the outside boundaries

    # Draw an arc as part of an ellipse.
    # Use radians to determine what angle to draw.
    # pygame.draw.arc(screen, BLACK, [20, 220, 250, 200], 0, PI / 2, 2)
    # pygame.draw.arc(screen, GREEN, [20, 220, 250, 200], PI / 2, PI, 2)
    # pygame.draw.arc(screen, BLUE, [20, 220, 250, 200], PI, 3 * PI / 2, 2)
    # pygame.draw.arc(screen, RED, [20, 220, 250, 200], 3 * PI / 2, 2 * PI, 2)

    # This draws a triangle using the polygon command
    # pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

    # Select the font to use, size, bold, italics
    # font = pygame.font.SysFont('Calibri', 25, True, False)

    # Render the text. "True" means anti-aliased text.
    # Black is the color. This creates an image of the
    # letters, but does not put it on the screen
    # text = font.render("My text", True, BLACK)

    # Put the image of the text on the screen at 250x250
    # screen.blit(text, [250, 250])

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()
