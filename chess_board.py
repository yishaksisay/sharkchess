import pygame 


# intiling pygame
pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("chessboard")

# coloring 

LIGHT = (255, 255, 255)
DARK = (128, 0, 128)

def drew_board(screen):
    square_size = WIDTH // 8
    for r in range(8):
        for c in range(8):
            color = LIGHT if (r + c) % 2 == 0 else DARK
            x = c * square_size
            y = r * square_size
            pygame.draw.rect(screen, color, pygame.Rect(x, y, square_size,square_size))


# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        drew_board(screen)
        pygame.display.flip()

pygame.quit()
