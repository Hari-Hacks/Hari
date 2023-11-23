import pygame

# Initialize pygame
pygame.init()

# Set screen size
screen_width = 800
screen_height = 600

# Set ball properties
ball_radius = 20
ball_color = (255, 255, 255)
ball_speed = [5, 5]

# Set paddle properties
paddle_width = 20
paddle_height = 100
paddle_color = (255, 255, 255)
paddle_speed = 10

# Create screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Create clock for game loop
clock = pygame.time.Clock()

# Create ball
ball = pygame.Surface((ball_radius * 2, ball_radius * 2))
ball.fill(ball_color)
ball_rect = ball.get_rect()
ball_rect.center = (screen_width / 2, screen_height / 2)

# Create paddles
left_paddle = pygame.Surface((paddle_width, paddle_height))
left_paddle.fill(paddle_color)
left_paddle_rect = left_paddle.get_rect()
left_paddle_rect.left = 0
left_paddle_rect.centery = screen_height / 2

right_paddle = pygame.Surface((paddle_width, paddle_height))
right_paddle.fill(paddle_color)
right_paddle_rect = right_paddle.get_rect()
right_paddle_rect.right = screen_width
right_paddle_rect.centery = screen_height / 2

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move ball
    ball_rect = ball_rect.move(ball_speed)

    # Check for ball collision with walls
    if ball_rect.left < 0 or ball_rect.right > screen_width:
        ball_speed[0] = -ball_speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > screen_height:
        ball_speed[1] = -ball_speed[1]

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle_rect.top -= paddle_speed
    if keys[pygame.K_s]:
        left_paddle_rect.top += paddle_speed
    if keys[pygame.K_UP]:
        right_paddle_rect.top -= paddle_speed
    if keys[pygame.K_DOWN]:
        right_paddle_rect.top += paddle_speed

    # Check for paddle collision with walls
    if left_paddle_rect.top < 0:
        left_paddle_rect.top = 0
    if left_paddle_rect.bottom > screen_height:
        left_paddle_rect.bottom = screen_height
    if right_paddle_rect.top < 0:
        right_paddle_rect.top = 0
