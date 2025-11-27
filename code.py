import pygame
import random
import operator

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
dt = 0
game_over = False
snake = ()

box1 = ()
box2 = ()
box3 = ()

num_1 = random.randint(1, 10)
num_2 = random.randint(1, 10)
num_3 = random.randint(1, 20)
num_4 = random.randint(1, 20)
operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv,}
operation = random.choice(list(operators.keys()))
answer = operators.get(operation)(num_1, num_2)

snake_pos = pygame.Vector2(screen.get_width() / 2, 400)
box1_pos = pygame.Vector2(150, 200)

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    box1 = ()
    pygame.draw.rect(screen, (92, 60, 40), (140, 140, 10, 30))
    pygame.draw.rect(screen, (255,0,0), (100, 160, 100, 100))

    box2 = ()
    pygame.draw.rect(screen, (92, 60, 40), (290, 140, 10, 30))
    pygame.draw.rect(screen, (255,0,0), (250, 160, 100, 100))

    box3 = ()
    pygame.draw.rect(screen, (92, 60, 40), (440, 140, 10, 30))
    pygame.draw.rect(screen, (255,0,0), (400, 160, 100, 100))

    pygame.draw.circle(screen, "white", snake_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake_pos.y -= 200 * dt
        if snake_pos.y == 600:
            game_over = True


    elif keys[pygame.K_DOWN]:
        snake_pos.y += 200 * dt
        if snake_pos.y == 0:
            game_over = True



    elif keys[pygame.K_RIGHT]:
        snake_pos.x += 200 * dt
        if snake_pos.x == 600:
            game_over = True


    elif keys[pygame.K_LEFT]:
        snake_pos.x -= 200 * dt
        if snake_pos.x == 0:
            game_over = True

    pygame.display.flip()

    if (game_over):
        pygame.quit()

    dt = clock.tick(60) / 1000

pygame.quit()
