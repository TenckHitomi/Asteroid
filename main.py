import pygame
import sys


def laser_update(laser_list, speed=300):
    for rect in laser_list:
        rect.y -= speed * dt
        if rect.bottom < 0:
            laser_list.remove(rect)


def display_score():
    score_text = f"Score: {pygame.time.get_ticks() // 1000}"
    text_surf = font.render(score_text, True, 'White')
    text_rect = text_surf.get_rect(midbottom=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))
    display_surface.blit(text_surf, text_rect)
    pygame.draw.rect(display_surface, 'white', text_rect.inflate(30, 30), width=8, border_radius=10)



# game init
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Asteroid Shooter')
clock = pygame.time.Clock()

# ship import
ship_surf = pygame.image.load('graphics/images/ship.png').convert_alpha()
ship_rect = ship_surf.get_rect(center=(640, 360))

# background
background_surf = pygame.image.load('graphics/images/background.png').convert()

# laser import
laser_surf = pygame.image.load('graphics/images/laser.png').convert_alpha()
laser_list = []
laser_rect = laser_surf.get_rect(midbottom=ship_rect.midtop)

# text imports
font = pygame.font.Font('graphics/fonts/subatomic.ttf', 50)

# drawing


while True:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print('shoot laser')
            laser_rect = laser_surf.get_rect(midbottom=ship_rect.midtop)
            laser_list.append(laser_rect)

    # framerate limit
    dt = clock.tick(120) / 1000

    # mouse input
    ship_rect.center = pygame.mouse.get_pos()

    # update
    laser_update(laser_list)

    pygame.time.get_ticks()

    # drawing
    display_surface.fill((0, 0, 0))
    display_surface.blit(background_surf, (0, 0))

    display_score()

    # for loop that draws laser surface
    for laser in laser_list:
        display_surface.blit(laser_surf, laser)

    display_surface.blit(ship_surf, ship_rect)

    # draw the final frame
    pygame.display.update()
