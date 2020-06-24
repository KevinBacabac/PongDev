import pygame  # Module imports
import sys

# Initialize pygame before use
pygame.init()

# Pick size of window
SIZE = (800, 600)

# Initialize the window
window = pygame.display.set_mode(SIZE)

# Control the frame rate
FPS = 60

# A special variable that will pause each frame
clock = pygame.time.Clock()

# Define our objects
class Paddle:
    def __init__(self, x, y):
        self.WIDTH = 10
        self.HEIGHT = 100
        self.rect = pygame.Rect(x, y, self.WIDTH, self.HEIGHT)

left_paddle = Paddle(20, 20)

BALL_SIZE = 10
ball = pygame.Rect(200, 200, BALL_SIZE, BALL_SIZE)
ballDx = -2
ballDy = 6

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
        left_paddle.rect.y -= 5
    elif move_down:
        left_paddle.rect.y += 5

    # Stay within the screen
    left_paddle.rect.top = max(left_paddle.rect.top, 0)
    left_paddle.rect.bottom = min(left_paddle.rect.bottom, 600)

    # Move the ball
    ball.x += ballDx
    ball.y += ballDy

    # Ball hits paddle
    if ball.colliderect(left_paddle.rect) and ballDx < 0:
        ballDx *= -1

    # Ball leaves screen
    if ball.top < 0 and ballDy < 0:
        ballDy *= -1

    if ball.bottom > 600 and ballDy > 0:
        ballDy *= -1

    # Drawing
    window.fill(pygame.Color("Black"))
    pygame.draw.rect(window, pygame.Color("White"), left_paddle.rect)
    pygame.draw.rect(window, pygame.Color("White"), ball)

    # Show the new frame
    pygame.display.update()

    # Pause
    clock.tick(FPS)
