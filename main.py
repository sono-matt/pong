import pygame
import time

pygame.init()
pygame.font.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

font = pygame.font.SysFont("verdana", 40)
FPS = 100
clock = pygame.time.Clock()

one_score = 0
two_score = 0

RECT_WIDTH = 15
RECT_HEIGHT = 100


class Player:
    VEL = 15
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect((x,  y), (RECT_WIDTH, RECT_HEIGHT))
    def draw(self):
        self.rect = pygame.Rect((self.x, self.y), (RECT_WIDTH, RECT_HEIGHT))
        pygame.draw.rect(screen, 'white', self.rect) # rect takes in x, y, width, height

#init player objects

p_one = Player(10, HEIGHT/2)
p_two = Player(WIDTH - RECT_WIDTH - 10, HEIGHT/2)
BALL_SIZE = 10

class Ball:
    Y_VEL = 2
    X_VEL = 5
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect((x,y), (BALL_SIZE, BALL_SIZE))
    def draw(self):
        self.rect = pygame.Rect((self.x, self.y), (BALL_SIZE,BALL_SIZE))
        pygame.draw.rect(screen, 'white', self.rect) # rect takes in x, y, width, heigh

ball = Ball(WIDTH/2, HEIGHT/2)

def reset():
    time.sleep(1)
    Ball.Y_VEL = -Ball.Y_VEL


def detect_collision():
    collide_1 = pygame.Rect.colliderect(ball.rect,p_one.rect)
    collide_2 = pygame.Rect.colliderect(ball.rect, p_two.rect)
    if collide_1:
        ball.x += BALL_SIZE 
        Ball.X_VEL = -Ball.X_VEL
    if collide_2:
        ball.x -= BALL_SIZE
        Ball.X_VEL = -Ball.X_VEL

def main():
    global one_score
    global two_score
    def update_display():
        screen.fill((0,0,0))
        p_one.draw()
        p_two.draw()
        ball.draw()
        one_score_render = font.render(f"{one_score}", 1, (255,255,255))
        two_score_render = font.render(f"{two_score}", 1, (255,255,255))
        screen.blit(one_score_render, (100,100))
        screen.blit(two_score_render, (WIDTH-100, 100))
        pygame.display.update()
    running = True
    update_display()
    time.sleep(1)
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                p_one.y -= Player.VEL # p1 up
            if keys[pygame.K_s]:
                p_one.y+= Player.VEL #p1 down
            if keys[pygame.K_i]:
                p_two.y -= Player.VEL #p2 up
            if keys[pygame.K_k]:
                p_two.y += Player.VEL #p2 down

        detect_collision()

        # making the ball move
        ball.x+=Ball.X_VEL
        ball.y+=-Ball.Y_VEL
        
        # handling two loss
        if ball.x == WIDTH-BALL_SIZE:
            Ball.X_VEL = -Ball.X_VEL
            one_score += 1
            ball.x = WIDTH/2
            ball.y = HEIGHT/2
            update_display()
            reset()

        # handle one loss
        elif ball.x == 0:
            Ball.X_VEL = -Ball.X_VEL
            two_score += 1
            ball.x = WIDTH/2
            ball.y = HEIGHT/2
            update_display()
            reset()
        if ball.y == HEIGHT - BALL_SIZE:
            Ball.Y_VEL = -Ball.Y_VEL
        elif ball.y == 0:
            Ball.Y_VEL = -Ball.Y_VEL
        
        update_display()

main()
        
