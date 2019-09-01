import pygame
import field
import ball
import random

# colors (r,g,b)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
pink = (255, 0, 255)
cyan = (0, 255, 255)
gray = (200, 200, 200)
dark_gray = (100, 100, 100)

colors = [blue, red, green, pink, cyan]


def rand_color():
    return colors[random.randrange(len(colors))]


class Game:
    def __init__(self):
        self.rect_number = 9
        self.display = pygame.display.get_surface()
        self.dimensions = pygame.display.get_window_size()
        self.rect_size = int(self.dimensions[0]/self.rect_number * 0.85)
        self.padding = int(self.dimensions[0]/self.rect_number * 0.15)
        self.full_rect = self.rect_size + self.padding
        self.field_list = []

        self.display.fill(dark_gray)      # background
        for i in range(self.rect_number):
            for j in range(self.rect_number):
                self.field_list.append(field.Field((self.padding + i*self.full_rect, self.padding + j*self.full_rect),self.rect_size, self.padding, gray).draw())
        pygame.display.update()

    '''
        player's move
    '''
    def play(self):
        player_round = True
        player_choice = 0
        while player_round:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if player_choice == 0:  # first click
                        position = pygame.mouse.get_pos()
                        selected_field = self.search_for_field(position)
                        if selected_field is not None:
                            selected_field.ball.highlight()
                            player_choice = 1
                        break
                    elif player_choice == 1:    # second click
                        player_round = False

                if event.type == pygame.QUIT:
                    quit()  # TODO: not pretty (fix it!)

    '''
        creating new balls in between rounds
    '''
    def mid_round(self):
        for i in range(3):
            self.rand_field().take(rand_color())

    '''
        random field that isn't taken
    '''
    def rand_field(self):
        i = random.randrange(len(self.field_list))
        while self.field_list[i].ball is not None:
            i = random.randrange(len(self.field_list))
        return self.field_list[i]

    def search_for_field(self, position):
        for i in self.field_list:
            if position[0] >= i.position[0] and position[1] >= i.position[1] and position[0] <= i.position[0] + i.dimensions and position[1] <= i.position[1] + i.dimensions:
                return i
        return None
