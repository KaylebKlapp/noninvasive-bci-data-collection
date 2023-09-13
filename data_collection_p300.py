import pygame
from datetime import datetime

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Alata", 700)

time_keys = []
letters = ['K', 'W', 'E']
keys = [pygame.K_k, pygame.K_w, pygame.K_e]

def render_ront(str, color = (0, 0, 0)):
    text = font.render(str, True, (0,0,0))
    return text

def start_window():
    pygame.display.set_caption("BCI training")
    screen = pygame.display.set_mode((550, 500))
    
    letter_index = 0
    running = True;
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False;
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == keys[letter_index]:
                    time_keys.append([letters[letter_index], datetime.now()])
                    letter_index += 1
                    letter_index %= len(letters)
                    
        screen.fill((205, 205, 205))
        text = render_ront(letters[letter_index])
        screen.blit(text, (50, 50))
        pygame.display.flip();                    


start_window()

with open("test.csv", "w") as fp:
    for input in time_keys:
        fp.write(f"{input[0]},{input[1]}\n")
