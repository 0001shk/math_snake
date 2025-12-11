import pygame
import random
import operator

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
dt = 0
game_over = False
snake = []

box1 = ()
box2 = ()
box3 = ()

num_1 = random.randint(1, 10)
num_2 = random.randint(1, 10)
operators = {'+': operator.add, '-': operator.sub, '*': operator.mul}
operation = random.choice(list(operators.keys()))
answer = operators[operation](num_1, num_2)

snake_pos = pygame.Vector2(screen.get_width() / 2, 400)
box1_pos = pygame.Vector2(150, 200)

def new_example():
    global num_1, num_2, operation, answer, wrong1, wrong2, apple_values

    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    operation = random.choice(["+", "-", "*"])

    if operation == "+":
        answer = num_1 + num_2
    elif operation == "-":
        answer = num_1 - num_2
    else:
        answer = num_1 * num_2

    wrong1 = answer + random.randint(1, 5)
    wrong2 = answer - random.randint(1, 5)

    while wrong1 == answer or wrong2 == answer or wrong1 == wrong2:
        wrong1 = answer + random.randint(1, 5)
        wrong2 = answer - random.randint(1, 5)

    apple_values = [answer, wrong1, wrong2]
    random.shuffle(apple_values)

new_example()

apple_positions = [
    pygame.Vector2(100, 160),
    pygame.Vector2(250, 160),
    pygame.Vector2(400, 160)
]

snake_length = 1


while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    pygame.draw.rect(screen, (92, 60, 40), (140, 140, 10, 30))
    pygame.draw.rect(screen, (255,0,0), (100, 160, 100, 100))

    pygame.draw.rect(screen, (92, 60, 40), (290, 140, 10, 30))
    pygame.draw.rect(screen, (255,0,0), (250, 160, 100, 100))

    pygame.draw.rect(screen, (92, 60, 40), (440, 140, 10, 30))
    pygame.draw.rect(screen, (255,0,0), (400, 160, 100, 100))

    font = pygame.font.Font(None, 40)

    problem_text = font.render(f"{num_1} {operation} {num_2}", True, (255,255,255))
    screen.blit(problem_text, (250, 100))

    for i, pos in enumerate(apple_positions):
        text = font.render(str(apple_values[i]), True, (255,255,255))
        screen.blit(text, (pos.x + 35, pos.y + 35))


    pygame.draw.circle(screen, "white", snake_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake_pos.y -= 200 * dt
    elif keys[pygame.K_DOWN]:
        snake_pos.y += 200 * dt
    elif keys[pygame.K_RIGHT]:
        snake_pos.x += 200 * dt
    elif keys[pygame.K_LEFT]:
        snake_pos.x -= 200 * dt

    snake_rect = pygame.Rect(snake_pos.x - 40, snake_pos.y - 40, 80, 80)

    for i, pos in enumerate(apple_positions):
        apple_rect = pygame.Rect(pos.x, pos.y, 100, 100)

        if snake_rect.colliderect(apple_rect):

            if apple_values[i] == answer:
                snake_length += 1
                snake_pos = pygame.Vector2(screen.get_width() / 2, 400)
                new_example()
            else:
                game_over = True

    pygame.display.flip()
    if game_over:
        screen.fill((0, 0, 0))
        over_text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(over_text, (200, 250))
        pygame.display.flip()

        pygame.time.delay(2000)
        running = False

    dt = clock.tick(60) / 1000

pygame.quit()
