import pygame
import sys

pygame.init()

# Game Variables
GAME_STATE = True

#colors
WHITE = (255,255,255)
GRAY = (25,25,25)
LIGHT_GRAY = (95,95,95)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

# Global variables
USER_RACKET_SİZE = [10,80]
COMP_RACKET_SİZE = [10,80]
USER_POINT_VALUE = 0
COMP_POINT_VALUE = 0

# Fonts
font = pygame.font.Font('freesansbold.ttf', 40)

# Window Proterties
windows_size = (800,450)
HEIGHT = windows_size[1]
WIDTH = windows_size[0]

window = pygame.display.set_mode(windows_size)
pygame.display.set_caption("Pin-Pong !")

# Game Finish Variables
WHO_WON = ""
USER_SCORE = ""
COMP_SCORE = ""


# Ball variables
BALL_X = WIDTH / 2
BALL_Y = HEIGHT / 2 

BALL_DIRECTION_X = 1
BALL_DIRECTION_Y = 1

#BALL_SPEED = 0.14
BALL_SPEED = 0.9

COMP_RACKET_Y = 1
while GAME_STATE:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()

    window.fill(GRAY)
 
    USER_POINT = font.render(str(USER_POINT_VALUE), True, GREEN, GRAY)
    USER_POINT_RECT = USER_POINT.get_rect()
    USER_POINT_RECT.center = ((WIDTH / 2) - 60 , 40)

    COMP_POINT = font.render(str(COMP_POINT_VALUE), True, BLUE, GRAY)
    COMP_POINT_RECT = COMP_POINT.get_rect()
    COMP_POINT_RECT.center = ((WIDTH / 2) + 60 , 40)

    window.blit(USER_POINT, USER_POINT_RECT)
    window.blit(COMP_POINT, COMP_POINT_RECT)

    MOUSE_POS_Y = pygame.mouse.get_pos()[1]    

    MAP_DES_CIRCLE = pygame.draw.circle(window, LIGHT_GRAY, (WIDTH / 2  , HEIGHT / 2 ), 100, 3)
    MAP_DES_LINE = pygame.draw.line(window, LIGHT_GRAY, (WIDTH / 2 , 0), (WIDTH / 2 , HEIGHT), 3)

    COMP_RACKET_Y = BALL_Y * 0.85

    USER_RACKET = pygame.draw.rect(window, GREEN, (10, ((MOUSE_POS_Y) - (USER_RACKET_SİZE[1] / 2)), USER_RACKET_SİZE[0], USER_RACKET_SİZE[1]))
    COMP_RACKET = pygame.draw.rect(window, BLUE, (WIDTH - 20, (COMP_RACKET_Y - (COMP_RACKET_SİZE[1] / 2)), COMP_RACKET_SİZE[0], COMP_RACKET_SİZE[1]))    
    

    if (BALL_X > WIDTH - 10):
        USER_POINT_VALUE += 1
        BALL_X = WIDTH / 2
        BALL_Y = HEIGHT / 2
        BALL_DIRECTION_X *= -1
        BALL_SPEED = 0.14

    if (BALL_X < 0):
        COMP_POINT_VALUE += 1
        BALL_X = WIDTH / 2
        BALL_Y = HEIGHT / 2
        BALL_DIRECTION_X *= -1
        BALL_SPEED = 0.14
    
    if (BALL_Y > HEIGHT - 10 or BALL_Y < 0):
        BALL_DIRECTION_Y *= -1

    BALL_X += BALL_SPEED * BALL_DIRECTION_X
    BALL_Y += BALL_SPEED * BALL_DIRECTION_Y

    BALL = pygame.draw.circle(window, WHITE, (BALL_X , BALL_Y), 10, 0)

    if (pygame.Rect.colliderect(USER_RACKET, BALL)):
        BALL_DIRECTION_X *= -1
        BALL_SPEED += 0.02

    if (pygame.Rect.colliderect(COMP_RACKET, BALL)):
        BALL_DIRECTION_X *= -1
        BALL_SPEED += 0.02

    if (USER_POINT_VALUE == 3):
        WHO_WON = "usr"
        USER_SCORE = USER_POINT_VALUE
        COMP_SCORE = COMP_POINT_VALUE
        GAME_STATE = False
        
    if (COMP_POINT_VALUE == 3):
        WHO_WON = "comp"
        USER_SCORE = USER_POINT_VALUE
        COMP_SCORE = COMP_POINT_VALUE
        GAME_STATE = False
        
    
    pygame.display.update()

if (GAME_STATE == False):
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
    
        pygame.display.update()

        if WHO_WON == "usr":
            win_text = font.render("You Win!", True, GREEN, GRAY)
        else:
            win_text = font.render("Computer Wins!", True, BLUE, GRAY)

        win_text_rect = win_text.get_rect()
        win_text_rect.center = (WIDTH / 2, HEIGHT / 2 - 50)

        user_score_text = font.render("Your Score: " + str(USER_SCORE), True, GREEN, GRAY)
        user_score_text_rect = user_score_text.get_rect()
        user_score_text_rect.center = (WIDTH / 2, HEIGHT / 2)

        comp_score_text = font.render("Computer Score: " + str(COMP_SCORE), True, BLUE, GRAY)
        comp_score_text_rect = comp_score_text.get_rect()
        comp_score_text_rect.center = (WIDTH / 2, HEIGHT / 2 + 50)

        window.blit(win_text, win_text_rect)
        window.blit(user_score_text, user_score_text_rect)
        window.blit(comp_score_text, comp_score_text_rect)
