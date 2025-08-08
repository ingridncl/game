import pygame

print('setup start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('loop Start')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Quitting...')
            pygame.quit()  # close window
            Quit()  # end pygame
