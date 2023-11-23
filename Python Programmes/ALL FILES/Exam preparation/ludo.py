import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window
WIDTH, HEIGHT = 600, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ludo")

# Define colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK= (0,0,255)

# Define player positions
player_positions = {
    "red": [(170, 170), (240, 170), (170, 240), (240, 240)],
    "green": [(350, 170), (420, 170), (350, 240), (420, 240)],
    "blue": [(170, 350), (240, 350), (170, 420), (240, 420)],
    "yellow": [(350, 350), (420, 350), (350, 420), (420, 420)]
}

# Define winning positions
winning_positions = {
    "red": [(170, 170), (170, 240), (240, 170), (240, 240)],
    "green": [(350, 170), (350, 240), (420, 170), (420, 240)],
    "blue": [(170, 350), (170, 420), (240, 350), (240, 420)],
    "yellow": [(350, 350), (350, 420), (420, 350), (420, 420)]
}

# Initialize player positions
current_positions = {
    "red": [-1, -1, -1, -1],
    "green": [-1, -1, -1, -1],
    "blue": [-1, -1, -1, -1],
    "yellow": [-1, -1, -1, -1]
}

# Define dice positions
dice_pos = (WIDTH // 2 - 25, HEIGHT // 2 - 25)

# Roll the dice
def roll_dice():
    return random.randint(1, 6)

# Move the player
def move_player(player, dice_roll):
    if current_positions[player][0] == -1 and dice_roll == 6:
        current_positions[player][0] = 0
    else:
        for i in range(4):
            if current_positions[player][i] != -1:
                current_positions[player][i] = (current_positions[player][i] + dice_roll) % 56
                break

# Check if a player has won
def check_win(player):
    for pos in current_positions[player]:
        if pos not in winning_positions[player]:
            return False
    return True

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice_roll = roll_dice()
                print("Dice Roll:", dice_roll)
                move_player("red", dice_roll)  # Replace "red" with the current player's color

    win.fill(WHITE)
    pygame.draw.rect(win, RED, (150, 150, 300, 300))
    pygame.draw.rect(win, WHITE, (170, 170, 260, 260))
    pygame.draw.circle(win, RED, (250, 250), 20)

    for player, positions in player_positions.items():
        for i, pos in enumerate(positions):
            if current_positions[player][i] == -1:
                pygame.draw.circle(win, player, pos, 15)
            else:
                pygame.draw.circle(win, player, pos, 15)
                pygame.draw.circle(win, WHITE, (pos[0] + 5, pos[1] + 5), 5)

    pygame.draw.rect(win, WHITE, (dice_pos[0], dice_pos[1], 50, 50))
    pygame.draw.rect(win, BLACK, (dice_pos[0], dice_pos[1], 50, 50), 2)
    # Draw dice dots based on dice_roll value

    pygame.display.flip()

pygame.quit()
