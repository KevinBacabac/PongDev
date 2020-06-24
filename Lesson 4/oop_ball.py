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
    WIDTH = 10
    HEIGHT = 100

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, self.WIDTH, self.HEIGHT)

    def check_bounds(self, SIZE):
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, SIZE[1])

    def draw(self, window):
        pygame.draw.rect(window, pygame.Color("White"), self.rect)

left_paddle = Paddle(20, 20)

class Ball:
    SIZE = 10

    def __init__(self, x, y):
        self.rect = pygame.Rect(200, 200, self.SIZE, self.SIZE)
        self.dx = -2
        self.dy = 4

    def check_vertical(self):
        if self.rect.top < 0 and self.dy < 0:
            self.dy *= -1

        if self.rect.bottom > 600 and self.dy > 0:
            self.dy *= -1

    def draw(self, window):
        pygame.draw.rect(window, pygame.Color("White"), self.rect)

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

ball = Ball(200, 200)

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
    left_paddle.check_bounds(SIZE)

    # Move the ball
    ball.move()

    # Ball hits left paddle
    if ball.rect.colliderect(left_paddle.rect) and ball.dx < 0:
        ball.dx *= -1

    # Ball leaves screen
    ball.check_vertical()

    # Drawing
    window.fill(pygame.Color("Black"))
    left_paddle.draw(window)
    ball.draw(window)

    # Show the new frame
    pygame.display.update()

    # Pause
    clock.tick(FPS)
