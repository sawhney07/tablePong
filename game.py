import pygame
import sys

pygame.init()

WIDTH, HIGHT = 1200, 800
BALL_RADIUS = 20
PADDLE_WIDTH, PADDLE_HIGHT = 20, 120
FPS = 60
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HIGHT))
pygame.display.set_caption("Pong Game")

clock = pygame.time.Clock()

player1 = pygame.Rect(50, HIGHT // 2 - PADDLE_HIGHT // 2, PADDLE_WIDTH, PADDLE_HIGHT)
player2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HIGHT // 2 - PADDLE_HIGHT // 2, PADDLE_WIDTH, PADDLE_HIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS // 2, HIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)

ball_speed = [5, 5]

score_player1 = 0
score_player2 = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    # Player 1 controls
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= 5
    if keys[pygame.K_s] and player1.bottom < HIGHT:
        player1.y += 5

    # Player 2 controls
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= 5
    if keys[pygame.K_DOWN] and player2.bottom < HIGHT:
        player2.y += 5

    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.top <= 0 or ball.bottom >= HIGHT:
        ball_speed[1] = -ball_speed[1]

    if ball.colliderect(player1) or ball.colliderect(player2): 
        ball_speed[0] = -ball_speed[0]

    if ball.left <= 0:
        score_player2 += 1
        ball.x = WIDTH // 2 -BALL_RADIUS // 2
        ball_speed[0] = -ball_speed[0]
    elif ball.right >= WIDTH:
        score_player1 += 1
        ball.x = WIDTH // 2 -BALL_RADIUS // 2
        ball_speed[0] = -ball_speed[0]

    # Drawing
    screen.fill((38, 38, 38))
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.rect(screen, WHITE, ball)

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"{score_player1} - {score_player2}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    pygame.display.flip()

    clock.tick(FPS)
