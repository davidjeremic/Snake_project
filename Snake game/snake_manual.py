import pygame
import math
import random

pygame.init()
sx = 500
sy = 500
screen = pygame.display.set_mode((sx, sy))
done = False
x = 0
y = 0
ev = 'r'
fl = 0
clock = pygame.time.Clock()
color = (0, 128, 255)
sp = {0: (x, y)}
size = 1
points = 0


def checkOut(a1, b1, ev1):
    if a1 == sx - 20 and b1 == sy - 20:
        if ev1 == 'r' or ev1 == 'd':
            return True
    if a1 == 0 and b1 == 0:
        if ev1 == 'l' or ev1 == 'u':
            return True
    if a1 == 0 and b1 == sy - 20:
        if ev1 == 'd' or ev1 == 'l':
            return True
    if a1 == sx - 20 and b1 == 0:
        if ev1 == 'r' or ev1 == 'u':
            return True
    if a1 == sx - 20:
        if ev1 == 'r':
            return True
    if a1 == 0:
        if ev1 == 'l':
            return True
    if b1 == 0:
        if ev1 == 'u':
            return True
    if b1 == sy - 20:
        if ev1 == 'd':
            return True
    zx, zy = sp[0]
    for i in range(2, size):
        tex, tey = sp[i]
        if zx == tex and zy == tey:
            return True
    return False


def move(a, b, ev):
    if ev == 'r':
        if a <= sx - 40:
            a += 20
    if ev == 'l':
        if a >= 20:
            a -= 20
    if ev == 'u':
        if b >= 20:
            b -= 20
    if ev == 'd':
        if b <= sy - 40:
            b += 20
    return a, b


# If you want snake to move through edges
def move2(a, b, ev):
    if ev == 'r':
        if a <= sx - 40:
            a += 20
        else:
            a = 0
    if ev == 'l':
        if a >= 20:
            a -= 20
        else:
            a = sx - 20
    if ev == 'u':
        if b >= 20:
            b -= 20
        else:
            b = sy - 20
    if ev == 'd':
        if b <= sy - 40:
            b += 20
        else:
            b = 0
    return a, b


pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 20)


def drawbox(x, y, col=color):
    pygame.draw.rect(screen, col, pygame.Rect(x, y, 20, 20))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x, y, 20, 20), 2)
    # pygame.draw.rect(screen, [200, 200, 200], pygame.Rect(x,y, 20), 5)


def randomSnack():
    rx1 = random.randrange((sx - 20) / 20)
    ry1 = random.randrange((sy - 20) / 20)
    return rx1 * 20, ry1 * 20


rx, ry = randomSnack()

while not done:
    fl = 0
    screen.fill((0, 0, 0))
    screen.blit(pygame.image.load('apple.png'), (rx - 2, ry - 2))
    textsurface = myfont.render(str(points), False, (255, 255, 0))
    screen.blit(textsurface, (sx - 60, 10))
    # pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(rx, ry, 20, 20))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                r1 = random.randrange(255)
                g1 = random.randrange(255)
                b1 = random.randrange(255)
                color = (r1, g1, b1)
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP] or pressed[pygame.K_w]:
                ev = 'u'
            if pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
                ev = 'd'
            if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
                ev = 'l'
            if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
                ev = 'r'

            if pressed[pygame.K_q]:
                done = True

    x, y = move2(x, y, ev)
    nx, ny = sp[0]
    nx1, ny1 = move2(nx, ny, ev)

    sp[0] = (nx1, ny1)
    sp[1] = (nx, ny)
    for i in range(size - 1, 0, -1):
        nx, ny = sp[i]
        drawbox(nx, ny, color)
        tx, ty = sp[i - 1]
        sp[i] = (tx, ty)
    drawbox(nx1, ny1, (0, 0, 255))
    pygame.display.flip()
    clock.tick(10)
    if x == rx and y == ry:
        sp[size] = (rx + 1, ry + 1)
        rx, ry = randomSnack()
        size += 1
        points += 10
    # print(sp)
    if checkOut(nx, ny, ev):
        size = 1
        points = 0
        x, y = 0, 0
        sp[0] = (x, y)
        ev = 'r'
    # print("out")
