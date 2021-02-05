import pygame
import os # Define the path on operating system (iamges)
pygame.init()

WIDTH, HEIGHT = 900, 500 # Set size of width & height
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Set screen size
pygame.display.set_caption("First Game") # Display name of game

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

FPS = 60
VEL = 5
CHARACTER_WIDTH, CHARACTER_HEIGHT = 50, 65

CHARACTER_IMAGE = pygame.image.load(os.path.join('Assets', 'Character.png'))
CHARACTER_COIN = pygame.image.load(os.path.join('Assets', 'Coin.png'))

CHARACTER_RESIZE = pygame.transform.rotate(pygame.transform.scale(
    CHARACTER_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT)), 360) # Resize & Rotate image (0 degree)
CHARACTER_RESIZE = pygame.transform.scale(
    CHARACTER_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

def character_handle_movements(keys_pressed, character):
    if keys_pressed[pygame.K_a] and character.x - VEL > 0: # LEFT
        character.x -= VEL
    if keys_pressed[pygame.K_d] and character.x + VEL < 400: # RIGHT
        character.x += VEL
    if keys_pressed[pygame.K_w] and character.y - VEL > 0: # UP
        character.y -= VEL
    if keys_pressed[pygame.K_s] and character.y + VEL < HEIGHT - 60: # DOWN
        character.y += VEL

def coin_handle_movements(keys_pressed, coin):
    if keys_pressed[pygame.K_LEFT]: # LEFT
        coin.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and coin.x + VEL < WIDTH - 25: # RIGHT
        coin.x += VEL
    if keys_pressed[pygame.K_UP]: # UP
        coin.y -= VEL
    if keys_pressed[pygame.K_DOWN]: # DOWN
        coin.y += VEL

def draw_window(character, coin):
    WIN.fill(WHITE) # Background color
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(CHARACTER_RESIZE, (character.x, character.y)) # Postion image
    WIN.blit(CHARACTER_COIN, (coin.x, coin.y))
    pygame.display.update()

# Create function for isn't exit window automatically
def main():
    character = pygame.Rect(100, 300, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    coin = pygame.Rect(700, 300, CHARACTER_WIDTH, CHARACTER_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        character_handle_movements(keys_pressed, character)
        coin_handle_movements(keys_pressed, coin)
        draw_window(character, coin)
                
    pygame.quit()

if __name__ == "__main__": # Special Python Variable, Specific pygame function
    main()
