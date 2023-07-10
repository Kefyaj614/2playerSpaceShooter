import pygame , sys, os
from config import *
from sprites import *
from button import *
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.freetype.init()




WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("BEST GAME !")
def ship_movementp1(keys_pressed, player):
    if keys_pressed[pygame.K_a] and player.x - SPEED > 0:
        player.x -= SPEED 
    if keys_pressed[pygame.K_d] and player.x + SPEED + player.width < BORDER.x + 35:
        player.x += SPEED 
    if keys_pressed[pygame.K_w] and player.y - SPEED > 0:
        player.y -= SPEED 
    if keys_pressed[pygame.K_s] and player.y + SPEED + player.width < HEIGHT:
        player.y += SPEED 
def ship_movementp2(keys_pressed, player):
    if keys_pressed[pygame.K_LEFT]  and player.x - SPEED > BORDER.x + BORDER.width - 9:
        player.x -= SPEED 
    if keys_pressed[pygame.K_RIGHT] and player.x + SPEED + player.width < WIDTH:
        player.x += SPEED 
    if keys_pressed[pygame.K_UP] and player.y - SPEED > 0 :
        player.y -= SPEED 
    if keys_pressed[pygame.K_DOWN] and player.y + SPEED + player.width < HEIGHT:
        player.y += SPEED 
def handle_bullets(p1Bullets,p2Bullets,player1,player2):
   for bullet in p1Bullets:
    bullet.x += BULLET_SPEED
    if player2.colliderect(bullet):
        pygame.event.post(pygame.event.Event(P2_HIT))
        BULLET_HIT.play()
        p1Bullets.remove(bullet)
    elif bullet.x >= WIDTH:
        p1Bullets.remove(bullet)

   for bullet in p2Bullets:
    bullet.x -= BULLET_SPEED
    if player1.colliderect(bullet):
        pygame.event.post(pygame.event.Event(P1_HIT))
        BULLET_HIT.play()
        p2Bullets.remove(bullet)
    elif bullet.x <0:
        p2Bullets.remove(bullet)
def draw(player1,player2, p1Bullets, p2Bullets, p1health, p2health):
    # WIN.fill((SPACEBACKGROUND))
    WIN.blit(SPACEBACKGROUND, (0,0))
    pygame.draw.rect(WIN,MIDDLECOLOR,BORDER)



    p1_health_text = D_HEALTHFONT.render("Health: " +str(p1health), 1, COLOR) 
    p2_health_text = D_HEALTHFONT.render("Health: " +str(p2health), 1, COLOR)
    WIN.blit(p2_health_text, (WIDTH - p2_health_text.get_width() - 10, 10))
    WIN.blit(p1_health_text, (10, 10))

    WIN.blit(SPACESHIP1, (player1.x,player1.y))
    WIN.blit(SPACESHIP2, (player2.x,player2.y))
    for bullet in p1Bullets:
        pygame.draw.rect(WIN, BULLET_COLOR, bullet)
    for bullet in p2Bullets:
        pygame.draw.rect(WIN, BULLET_COLOR, bullet)
    pygame.display.update()
class GameState():
    def __innit__(self):
        self.state = "main"
        pass
    def intro(self):
        self.state = "intro"
        INTRO = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('GAME INTRO SCREEN!!')
        intro_start = True
        while intro_start:

            INTRO.fill((202, 228, 241))
            #event handler
            for event in pygame.event.get():
        

                if event.type == pygame.QUIT:
                    intro_start = False
                    pygame.quit()

            pygame.display.update()

        

        pass     
    def pause_state(self):
        self.state = "paused"
        PAUSE = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('PAUSED')
        game_paused = True

        # button Sprites
        play_b = pygame.image.load(os.path.join('All Code/Pygame_projects/TestGame/assets','play_button.png'))
        setting_b = pygame.image.load(os.path.join('All Code/Pygame_projects/TestGame/assets','settings_button.png'))
        exit_b = pygame.image.load(os.path.join('All Code/Pygame_projects/TestGame/assets','exit_button.png'))

        play_b_button = button.Button(
            (WIDTH - play_b.get_width()) // 2,
            100,
            play_b,10)
        setting_button = button.Button(
            (WIDTH - setting_b.get_width()) // 2,
            250,
            setting_b,10)
        exit_button = button.Button(
            (WIDTH - exit_b.get_width()) // 2,
            (HEIGHT - exit_b.get_height()) // 2,
            exit_b,10)


        while game_paused:

            #event handler
            for event in pygame.event.get():

                PAUSE.fill((202, 228, 241))
                if play_b_button.draw(PAUSE):
                    print("start")
                    game_paused = False
                if setting_button.draw(PAUSE):
                    print("testing button needs functions")
                if exit_button.draw(PAUSE):
                    print("This exits the program")
                    pygame.quit()
                if event.type == pygame.QUIT:
                    game_paused = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if show_pause_text == False:
                            show_pause_text = True



            pygame.display.update()
    def main(self):
        self.state = "main"
        P1_HEALTH = 10
        P2_HEALTH = 10
        pausing = False
        clock = pygame.time.Clock()
        run=True
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LCTRL and len(p1Bullets) < MAX_BULLETS:
                        bullet = pygame.Rect(player1.x + player1.width, player1.y + player1.height//2 - 2, 10, 5)
                        p1Bullets.append(bullet)
                        BULLET_FIRE.play()
            
                if event.type == pygame.KEYDOWN and len(p2Bullets) < MAX_BULLETS:
                    if event.key == pygame.K_RCTRL:
                        bullet = pygame.Rect(player2.x , player2.y + player2.height//2 - 2, 10, 5)
                        p2Bullets.append(bullet)
                        BULLET_FIRE.play()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if pausing == False:
                            pausing = True
                            self.state = "paused"
                            self.state_manager()

                if event.type==P1_HIT:
                    P1_HEALTH -= 1
                
                if event.type==P2_HIT:
                    P2_HEALTH -= 1
                

             

            winner_text = ""
            if P1_HEALTH <=0:
                winner_text="Player 2 Won!"
            if P2_HEALTH <=0:
                winner_text="Player 1 Won!"
            if winner_text!="":
                winner_text = ""
                break


            keys_pressed = pygame.key.get_pressed()
            ship_movementp1(keys_pressed, player1)
            ship_movementp2(keys_pressed, player2)
            handle_bullets(p1Bullets,p2Bullets,player1,player2)
            draw(player1,player2, p1Bullets, p2Bullets, P1_HEALTH, P2_HEALTH)
        gameState.main()
    def state_manager(self):
        if self.state == "main":
            self.main()
        if self.state == "paused":
            self.pause_state()
        
#METHODS ABOVE ^

gameState = GameState()






if __name__ == "__main__":
            gameState.main()

