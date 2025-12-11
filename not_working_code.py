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

#atbildes pos
x = 150
y = 210

font = pygame.font.Font("freesansbold.ttf", 32)

problem = font.render(f"What is {num_1}{operation}{num_2}?", True, (250, 250, 250))
textRect = problem.get_rect()
textRect.center = (300, 100)

choice_1 = font.render(f"{num_3}", True, (250, 250, 250))
ch1Rect = choice_1.get_rect()
ch1Rect.center = (x, y)

choice_2 = font.render(f"{num_4}", True, (250, 250, 250))
ch2Rect = choice_2.get_rect()
ch2Rect.center = (x + 150, y)

choice_3 = font.render(f"{answer}", True, (250, 250, 250))
ch3Rect = choice_3.get_rect()
ch3Rect.center = (x + 300, y)

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
    screen.blit(problem, textRect)
    screen.blit(choice_1, ch1Rect)
    screen.blit(choice_2, ch2Rect)
    screen.blit(choice_3, ch3Rect)

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

    #atbildes parbaude


    pygame.display.flip()

    if (game_over):
        pygame.quit()

    dt = clock.tick(60) / 1000

pygame.quit()
