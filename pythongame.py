# importowanie bibliotaki pygame
import random
import time
import pygame
import sys
import pyautogui

# inicjowanie wyświetlania okna
pygame.init()
disply = pygame.display.set_mode((800, 600))
pygame.display.set_caption('SnakeGame by Kris')

# inicjacja barw
white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)

Timer = pygame.time.Clock()


def message(msg, color):  # wypisywanie zakończenia gry
    mesg = pygame.font.SysFont("Impact", 50).render(msg, True, color)
    disply.blit(mesg, [350, 250])


def Scorer(score):  # wypisywanie punktów
    msg = pygame.font.SysFont("Impact", 30).render("Score: " + str(score), True, red)
    disply.blit(msg, [0, 0])  # wypisywanie informacji o liczbie zdobytych punktów w rogu ekranu


def Speed(speed):  # wypisanie prędkości
    msg = pygame.font.SysFont("Impact", 30).render("Speed: " + str(speed), True, red)
    disply.blit(msg, [200, 0])


def mySnake(snake_list):
    for s in snake_list:
        pygame.draw.rect(disply, black, [s[0], s[1], 10, 10])


def Game():
    game_over = False
    foodies = 1
    speed = 30

    xs = 400
    ys = 300
    x_ch = 0
    y_ch = 0
    xf = [random.randint(10, 700), random.randint(10, 700), random.randint(10, 700)]
    yf = [random.randint(10, 500), random.randint(10, 500), random.randint(10, 500)]
    Food = [pygame.Rect(xf[0], yf[0], 10, 10), pygame.Rect(xf[1], yf[1], 10, 10), pygame.Rect(xf[2], yf[2], 10, 10)]
    Snake = pygame.Rect(xs, ys, 10, 10)

    snake_list = []
    snake_lenght = 1

    while not game_over:
        pyautogui.press('space')
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:  # jeśli typ eventu jest qiut to okno zostanie zamknięte
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.key == pygame.K_RIGHT:
                    x_ch = 5
                    y_ch = 0
                elif event.key == pygame.K_LEFT:
                    x_ch = -5
                    y_ch = 0
                elif event.key == pygame.K_UP:
                    x_ch = 0
                    y_ch = -5
                elif event.key == pygame.K_DOWN:
                    x_ch = 0
                    y_ch = 5
            if Snake.x >= 800 or Snake.x < 0 or Snake.y >= 600 or Snake.y < 0:
                game_over = True

            Snake.x += x_ch
            Snake.y += y_ch

            # rysowanie
            disply.fill(white)
            pygame.draw.rect(disply, black, Snake)  # blok węża
            pygame.draw.rect(disply, blue, Food[0])  # blok jedzonka
            if foodies == 2:
                pygame.draw.rect(disply, blue, Food[1])  # blok jedzonka
            if foodies == 3:
                pygame.draw.rect(disply, blue, Food[1])  # blok jedzonka
                pygame.draw.rect(disply, blue, Food[2])  # blok jedzonka

            pygame.display.flip()

            if Snake.x in range(xf[0] - 10, xf[0] + 10) and Snake.y in range(yf[0] - 10, yf[0] + 10) \
                    or Snake.x in range(xf[1] - 10, xf[1] + 10) and Snake.y in range(yf[1] - 10, yf[1] + 10) \
                    or Snake.x in range(xf[2] - 10, xf[2] + 10) and Snake.y in range(yf[2] - 10, yf[2] + 10):
                # print("Mniamuśnie")
                foodies = random.randint(1, 3)
                xf = [random.randint(10, 700), random.randint(10, 700), random.randint(10, 700)]
                yf = [random.randint(10, 500), random.randint(10, 500), random.randint(10, 500)]
                Food = [pygame.Rect(xf[0], yf[0], 10, 10), pygame.Rect(xf[1], yf[1], 10, 10),
                        pygame.Rect(xf[2], yf[2], 10, 10)]
                snake_lenght += 1
                pygame.display.flip()

            snake_head = []
            snake_head.append(Snake.x)
            snake_head.append(Snake.y)
            snake_list.append(snake_head)

            if len(snake_list) > snake_lenght:
                del snake_list[0]
            for x in snake_list[:-1]:
                if x == snake_head:
                    game_over = True

            mySnake(snake_list)
            Scorer(snake_lenght - 1)
            Speed(speed)
            pygame.display.flip()

            Timer.tick(speed)  # prędkość węża

    if game_over == True:
        message("You Lost", red)
        pygame.display.flip()
        time.sleep(2)

    # zamknięcie okna gry
    pygame.quit()
    quit()


Game()
