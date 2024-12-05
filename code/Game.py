import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:  #NEW GAME 1P
                pass
            elif menu_return == MENU_OPTION[len(MENU_OPTION)-1]: #EXIT
                pygame.quit() #close window
                quit() #end pygame
            else:
                pass



