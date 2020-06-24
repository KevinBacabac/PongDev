import pygame  # Module imports
import sys

# Initialize pygame before use
pygame.init()

# Pick size of window
SIZE = (800, 600)

# Initialize the window
window = pygame.display.set_mode(SIZE)

# Control the frame rate
FPS = 30

# A special variable that will pause each frame
clock = pygame.time.Clock()

# Define our objects
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
paddle = pygame.Rect(20, 20, PADDLE_WIDTH, PADDLE_HEIGHT)

BALL_SIZE = 10
ball = pygame.Rect(100, 200, BALL_SIZE, BALL_SIZE)
ballDx = -2
ballDy = 1

# Controls
move_up = False
move_down = False

# Infinite loop
while True:
    # Check all pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        elif event.type in (pygame.KEYUP, pygame.KEYDOWN):
            if event.key == pygame.K_w:
                move_up = event.type == pygame.KEYDOWN
            elif event.key == pygame.K_s:
                move_down = event.type == pygame.KEYDOWN

    # Physics will go here
    if move_up:
        paddle.y -= 5
    elif move_down:
        paddle.y += 5

    ball.x += ballDx
    ball.y += ballDy

    if ball.colliderect(paddle) and ballDx < 0:
        ballDx *= -1

    # Drawing
    window.fill(pygame.Color("Black"))
    pygame.draw.rect(window, pygame.Color("White"), paddle)
    pygame.draw.rect(window, pygame.Color("White"), ball)

    # Show the new frame
    pygame.display.update()

    # Pause
    clock.tick(FPS)
