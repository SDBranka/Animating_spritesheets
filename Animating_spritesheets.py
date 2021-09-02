import pygame
import spritesheet

# initialize pygame
pygame.init()

# screen set up
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
# change the title of the displayed in display window
pygame.display.set_caption("Loading SpriteSheets")

# load spritesheet image
spritesheet_image = pygame.image.load("doux.png").convert_alpha()
# create instance of Spritesheet class
sprite_sheet = spritesheet.Spritesheet(spritesheet_image)

# set background color
background = (50, 50, 50)

# defining the color black to later remove color from png backgrounds
BLACK = (0, 0, 0)

# create animation list
animation_list = []
# animation_list broken into another list by action (4 idle, 6 running right, 3 in jump, 4 for death scene)
animation_steps = [4, 6, 3, 4]
# used to store which animation task character is performing
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 250
frame = 0
step_counter = 0

for animation in animation_steps:
    temp_image_list = []
    for _ in range(animation):
        temp_image_list.append(sprite_sheet.get_image(step_counter, 24, 24, 3, BLACK))
        step_counter += 1
    animation_list.append(temp_image_list)


run = True
while run:

    # applies background color to screen
    screen.fill(background)

    # update animation
    # checks to see if current time is greater than the last update by the animation cooldown
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        # increments the frame by one
        frame += 1
        # sets last_update to current time to restart animation cooldown clock
        last_update = current_time
        # checks to see position in animation cycle and resets to beginning if at the end
        if frame >= len(animation_list[action]):
            frame = 0


    # display frame image
    screen.blit(animation_list[action][frame], (0, 0))


    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and action > 0:
                action -= 1
                frame = 0
            if event.key == pygame.K_UP and action < len(animation_list) - 1:
                action += 1
                frame = 0







    pygame.display.update()

pygame.quit()