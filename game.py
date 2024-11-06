import pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pokemon battle game')



# Constants
MAX_CHAR = 15

font = pygame.font.Font(None, 40)
print(pygame.display.get_surface().get_size())

# Colours
GREY = '#DDDDDD'

# Input box


def main_game(username):
    while True:
        main_text = font.render(f'Welcome {username}, to the wonderful battle of the pokemon', True, 'black')
        screen.blit(main_text, (300,300))


def welcome_screen():
    input_username = pygame.Rect(300, 400, 200, 50)
    username = ''
    input_username_active_ = False
    while True:
        screen.fill('white')
        welcome_text = font.render('Welcome to the battle', True, 'black')
        user_text = font.render('Enter your name and press enter', True, 'black')
        screen.blit(welcome_text, (300, 200))
        screen.blit(user_text, (300, 300))

        pygame.draw.rect(screen, GREY, input_username)

        # Render and display current text in the input box
        username_input_text = font.render(username, True, 'black')
        screen.blit(username_input_text, (320, 420))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if input_username_active_:
                    if event.key == pygame.K_RETURN:
                        if len(username) == 0:
                            username = 'user didn\'t comply and enter their username so this is what it is'
                        main_game(username)
                    elif event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        if len(username) <= MAX_CHAR:
                            username += event.unicode

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if input box is clicked
                if input_username.collidepoint(event.pos):
                    input_username_active_ = True

            pygame.display.flip()



welcome_screen()


