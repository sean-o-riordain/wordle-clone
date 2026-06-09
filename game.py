# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
font = pygame.font.Font(None, 72)  # None = default font, 72 = size
letters = [""] * 25

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(pygame.Color(30, 30, 30))
    
    rects = []
    

    y = 70
    cell_index = 0
    for i in range(5):
        x = 25
        for j in range(5):
            rect = pygame.Rect(x, y, 100, 100)
            pygame.draw.rect(screen, "white", rect)
            if letters[cell_index]:
                text_surf = font.render(letters[cell_index], True, pygame.Color("black"))
                text_rect = text_surf.get_rect(center=rect.center)
                screen.blit(text_surf, text_rect)
            x += 120
            cell_index += 1
        y += 120

    for i in range(cell_index):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
            letters[i] = "W"
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
            letters[i] = "S"
        if keys[pygame.K_BACKSPACE]:
            letters[i] = ""
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()