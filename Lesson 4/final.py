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

# Define our classes
class Ball:
    SIZE = 10

    def __init__(self, x, y, dx, dy):
        self.rect = pygame.Rect(200, 200, self.SIZE, self.SIZE)
        self.dx = dx
        self.dy = dy

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


# Define our objects
left_paddle = Paddle(20, SIZE[1] / 2)
right_paddle = Paddle(SIZE[0] - Paddle.WIDTH - 20, SIZE[1] / 2)
PADDLES = (left_paddle, right_paddle)

balls = []
balls.append(Ball(200, 200, -2, 4))

# Controls
left_move_up = False
left_move_down = False
right_move_up = False
right_move_down = False

# Infinite loop
while True:
    # Check all pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        elif event.type in (pygame.KEYUP, pygame.KEYDOWN):
            if event.key == pygame.K_w:
                left_move_up = event.type == pygame.KEYDOWN
            elif event.key == pygame.K_s:
                left_move_down = event.type == pygame.KEYDOWN

            if event.key == pygame.K_UP:
                right_move_up = event.type == pygame.KEYDOWN
            elif event.key == pygame.K_DOWN:
                right_move_down = event.type == pygame.KEYDOWN

    # Physics will go here
    if left_move_up:
        left_paddle.rect.y -= 5
    elif left_move_down:
        left_paddle.rect.y += 5

    if right_move_up:
        right_paddle.rect.y -= 5
    elif right_move_down:
        right_paddle.rect.y += 5


    # Stay within the screen
    for paddle in PADDLES:
        paddle.check_bounds(SIZE)

    # Move the ball
    for ball in balls:
        ball.move()

    for ball in balls:
        # Ball hits left or right paddle
        if (ball.rect.colliderect(left_paddle.rect) and ball.dx < 0
            or ball.rect.colliderect(right_paddle.rect) and ball.dx > 0):
            ball.dx *= -1

        # Ball hits floor / ceiling
        ball.check_vertical()

        # Ball leaves screen
        if ball.rect.right < 0 or ball.rect.left > SIZE[0]:
            # You could implement a score system here

            balls.remove(ball)

            # Create a new ball
            balls.append(Ball(200, 200))

    # Drawing
    window.fill(pygame.Color("Black"))

    for paddle in PADDLES:
        paddle.draw(window)

    for ball in balls:
        ball.draw(window)

    # Show the new frame
    pygame.display.update()

    # Pause
    clock.tick(FPS)
