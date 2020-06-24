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
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100

paddle = pygame.Rect(20, 20, PADDLE_WIDTH, PADDLE_HEIGHT)

# Infinite loop
while True:
    # Check all pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    # Physics will go here

    # Drawing
    window.fill(pygame.Color("Black"))
    pygame.draw.rect(window, pygame.Color("White"), paddle)

    # Show the new frame
    pygame.display.update()

    # Pause
    clock.tick(FPS)
