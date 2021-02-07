import pygame
import os # Define the path on operating system (iamges)
pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 900, 500 # Set size of width & height
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Set screen size
pygame.display.set_caption("First Game") # Display name of game

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (255, 255, 0)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3

CHARACTER_HIT = pygame.USEREVENT + 1
COIN_HIT = pygame.USEREVENT + 2 

CHARACTER_WIDTH, CHARACTER_HEIGHT = 50, 65

CHARACTER_IMAGE = pygame.image.load(os.path.join('Assets', 'Character.png'))
CHARACTER_COIN = pygame.image.load(os.path.join('Assets', 'Coin.png'))

BG_SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

CHARACTER_RESIZE = pygame.transform.rotate(pygame.transform.scale(
    CHARACTER_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT)), 360) # Resize & Rotate image (0 degree)
CHARACTER_RESIZE = pygame.transform.scale(
    CHARACTER_IMAGE, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

def character_handle_movements(keys_pressed, character):
    if keys_pressed[pygame.K_a] and character.x - VEL > 0: # LEFT
        character.x -= VEL
    if keys_pressed[pygame.K_d] and character.x + VEL + character.width < BORDER.x: # RIGHT
        character.x += VEL
    if keys_pressed[pygame.K_w] and character.y - VEL > 0: # UP
        character.y -= VEL
    if keys_pressed[pygame.K_s] and character.y + VEL + character.height < HEIGHT: # DOWN
        character.y += VEL

def coin_handle_movements(keys_pressed, coin):
    if keys_pressed[pygame.K_LEFT] and coin.x - VEL > BORDER.x + BORDER.width: # LEFT
        coin.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and coin.x + VEL + coin.width < WIDTH: # RIGHT
        coin.x += VEL
    if keys_pressed[pygame.K_UP] and coin.y - VEL > 0: # UP
        coin.y -= VEL
    if keys_pressed[pygame.K_DOWN] and coin.y + VEL + coin.height < HEIGHT: # DOWN
        coin.y += VEL

def draw_window(character, coin, character_bullets, coin_bullets, character_health, coin_health):
    # WIN.fill(WHITE) # Background color
    WIN.blit(BG_SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    character_health_text = HEALTH_FONT.render("Health: " + str(coin_health), 1, WHITE)
    coin_health_text = HEALTH_FONT.render("Health: " + str(character_health), 1, WHITE)
    WIN.blit(character_health_text, (WIDTH - character_health_text.get_width() - 10, 10))
    WIN.blit(coin_health_text, (10, 10))

    WIN.blit(CHARACTER_RESIZE, (character.x, character.y)) # Postion image
    WIN.blit(CHARACTER_COIN, (coin.x, coin.y))

    for bullet in character_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    
    for bullet in coin_bullets:
        pygame.draw.rect(WIN, GREEN, bullet)

    pygame.display.update()

# Collider
def handle_bulltes(character_bullets, coin_bullets, character, coin):
    for bullet in character_bullets:
        bullet.x += BULLET_VEL
        if coin.colliderect(bullet):
            pygame.event.post(pygame.event.Event(COIN_HIT))
            character_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            character_bullets.remove(bullet)
    
    for bullet in coin_bullets:
        bullet.x -= BULLET_VEL
        if character.colliderect(bullet):
            pygame.event.post(pygame.event.Event(CHARACTER_HIT))
            coin_bullets.remove(bullet)
        elif bullet.x < 0:
            coin_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

# Create function for isn't exit window automatically
def main():
    character = pygame.Rect(100, 300, CHARACTER_WIDTH, CHARACTER_HEIGHT)
    coin = pygame.Rect(700, 300, CHARACTER_WIDTH, CHARACTER_HEIGHT)

    character_bullets = []
    coin_bullets = []

    character_health = 10
    coin_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(character_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(character.x + character.width, character.y + character.height//2 - 2, 10, 5)
                    character_bullets.append(bullet) # 'append' meant add

                if event.key == pygame.K_RCTRL and len(coin_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(coin.x, coin.y + coin.height//2 - 2, 10, 5)
                    coin_bullets.append(bullet)
            
            if event.type == CHARACTER_HIT:
                character_health -= 1

            if event.type == COIN_HIT:
                coin_health -= 1

        winner_text = ""
        if character_health <= 0:
            winner_text = "Coin Winner!"

        if coin_health <= 0:
            winner_text = "Character Winner!"

        if winner_text != "":
            draw_winner(winner_text)
            break
        
        print(character_bullets, coin_bullets)
        keys_pressed = pygame.key.get_pressed()
        character_handle_movements(keys_pressed, character)
        coin_handle_movements(keys_pressed, coin)

        handle_bulltes(character_bullets, coin_bullets, character, coin)

        draw_window(character, coin, character_bullets, coin_bullets, character_health, coin_health)
                
    pygame.quit()

if __name__ == "__main__": # Special Python Variable, Specific pygame function
    main()
