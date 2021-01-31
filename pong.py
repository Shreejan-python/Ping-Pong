import pygame
import sys
import random

def ball_animation():
    global ball_speedx, ball_speedy, player_speed, oppo_speed, score_time, oppo_score, player_score
    ball.x += ball_speedx
    ball.y += ball_speedy

    if ball.top <=0 or ball.bottom >= screen_height:
        ball_speedy *= -1
    if ball.left <= 0:
        oppo_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        player_score += 1
        score_time = pygame.time.get_ticks()



    if ball.colliderect(player) or ball.colliderect(oppo):
        ball_speedx *= -1
def player_ani():
    global ball_speedx, ball_speedy, player_speed, oppo_speed
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
def oppo_ai():
    global ball_speedx, ball_speedy, player_speed, oppo_speed
    if oppo.top < ball.y:
        oppo.top += oppo_speed
    if oppo.bottom > ball.y:
        oppo.bottom -= oppo_speed
    if oppo.top <= 0:
        oppo.top = 0
    if oppo.bottom >= screen_height:
        oppo.bottom = screen_height

def ball_restart():
    global ball_speedx, ball_speedy, player_speed, oppo_speed
    ball.center = (screen_width/2, screen_height/2)
    ball_speedy *= random.choice((1, -1))
    ball_speedx *= random.choice((1, -1))

def ball_start():
    global ball_speedx, ball_speedy, score_time, black

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2)

    if current_time - score_time < 700:
        number_three = game_font.render("3", False, black)
        screen.blit(number_three,(screen_width/2 -10, screen_height/2 + 20))
    
    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2", False, black)
        screen.blit(number_two,(screen_width/2 -10, screen_height/2 + 20))
    
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1", False, black)
        screen.blit(number_one,(screen_width/2 -10, screen_height/2 + 20))

    if current_time - score_time < 2100:
        ball_speedx, ball_speedy = 0, 0
    else:
        ball_speedy = 7 * random.choice((1, -1))
        ball_speedx = 7 * random.choice((1, -1))
        score_time = None

#initializing pygame
pygame.init()
clock = pygame.time.Clock()



#main window
screen_width = 1290
screen_height = 780
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ping Pong')

#game main characters
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 -15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
oppo = pygame.Rect(10, screen_height/2 - 70, 10, 140)

bg_color = pygame.Color('yellow')
red = (250, 0, 0)
black = (0, 0, 0)

ball_speedx=7 * random.choice((1, -1))
ball_speedy=7 * random.choice((1, -1))
player_speed = 0
oppo_speed = 7

#scores
player_score = 0
oppo_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 20)

score_time = True

#gameloop
while True:
    #input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_ani()
    oppo_ai()


    ball.x += ball_speedx
    ball.y += ball_speedy

    #vertical and horizontal
    

    screen.fill(bg_color)
    pygame.draw.rect(screen, red, player)
    pygame.draw.rect(screen, red, oppo)
    pygame.draw.ellipse(screen, red, ball)
    pygame.draw.aaline(screen, black, (screen_width/2,0), (screen_width/2, screen_height))

    if score_time:
        ball_start()


    player_text = game_font.render(f"{player_score}", False, black)
    screen.blit(player_text, (600, 470))

    oppo_text = game_font.render(f"{oppo_score}", False, black)
    screen.blit(oppo_text, (660, 470))
    
    #updating window
    pygame.display.flip()
    clock.tick(40)