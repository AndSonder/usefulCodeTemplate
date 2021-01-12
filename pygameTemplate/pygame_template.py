import pygame
import pygame.freetype
import sys


class MyPygame:
    def __init__(self):
        pygame.init()
        self.width = 500  # the width of the screen
        self.height = 500  # the height of the screen
        self.screen_name = 'Power by coronaPolvo'
        self.background_image = 'aaa.png'  # the background image's file path
        self.fclock = pygame.time.Clock()
        self.screen = self.__init_screen()
        self.__draw_background()

    # create a screen and set the size of it
    def __init_screen(self):
        # set the size of the screen
        size = self.width, self.height
        # set the color of the background
        screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        # set the total of the screen
        pygame.display.set_caption(self.screen_name)
        return screen

    def __draw_background(self):
        background = pygame.image.load(self.background_image)
        background_rect = background.get_rect()
        self.screen.blit(background, background_rect)

    def __write_words(self, word_size, content, background_color, word_color, x, y, word_style='GB2313.ttf'):
        """
        write words on the screen
        :param word_size: the size of the words
        :param content: content
        :param background_color: background color  such as (255,255,255) => write background
        :param word_color: word color such as (0,0,0) => black words
        :param x: x coordinate
        :param y: y coordinate
        :param word_style: you can choose word style by change this parameter
        """
        font = pygame.font.Font(word_style, word_size)
        text_surface_obj = font.render(content, True, word_color, background_color)
        text_rect_obj = text_surface_obj.get_rect()
        text_rect_obj.center = (x, y)
        self.screen.blit(text_surface_obj, text_rect_obj)

    def main(self):
        while True:
            for event in pygame.event.get():
                # exit
                if event.type == pygame.QUIT:
                    sys.exit()
                # KEYDOWN
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pass
                # KEYUP
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        pass
                elif event.type == pygame.MOUSEBUTTONDOWN:  # MOUSEBUTTONDOWN
                    x = event.pos[0]
                    y = event.pos[1]
                elif event.type == pygame.MOUSEBUTTONUP:  # MOUSEBUTTONUP
                    x = event.pos[0]
                    y = event.pos[1]
                elif event.type == pygame.MOUSEMOTION:  # MOUSEBUTTONON
                    x = event.pos[0]
                    y = event.pos[1]
            self.__draw_background()
            pygame.display.update()
            self.fclock.tick(300)


if __name__ == '__main__':
    my_pygame = MyPygame()
    my_pygame.main()
