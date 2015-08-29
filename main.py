import BoardState
import Checker
import CheckerType
import Game
import GameBoard
import GameMode
import GameObjects
import Menu
import Overlay
import Resource
import Teams

import pygame

game_objects = GameObjects.GameObjects()		# TODO doesn't need to be global


def main():
    init()


def init():
    screen = pygame.display.set_mode((1600, 900), pygame.DOUBLEBUF)
    board = GameBoard.GameBoard(screen, (8, 8))
    game_objects.menu = Menu.Menu(["Player vs Player", "Player vs Computer", "Quit"], screen)

    game_objects.board = board

    game_objects.state = BoardState.BoardState(board)
    game_objects.overlay = Overlay.Overlay(screen, game_objects.board, False)
    game_objects.overlay = Overlay.Overlay(screen, game_objects.board, False)


    for i in range(3):
        for j in range(8):

            if (i % 2) == 0:
                if not (j % 2) == 1:
                    add_checker(Teams.black(), (j, i + 5))
                    continue

            if not (i % 2) == 0:
                if (j % 2) == 1:
                    add_checker(Teams.black(), (j, i + 5))
                    continue

            add_checker(Teams.red(), (j, i))
    game_objects.game = Game.Game(game_objects.state, game_objects.board)
    game_objects.game.new_game(GameMode.player_v_player())
    run()


def add_checker(team, location):
    if location == (4, 0) or location == (7, 0):
        return
    red_checker = Resource.Resource("res/checker_red.png")
    black_checker = Resource.Resource("res/checker_black.png")
    res = None

    if team == Teams.red():
        res = red_checker
    else:
        res = black_checker

    checker = Checker.Checker(pygame.display.get_surface(), game_objects.board, res)
    checker.location = location
    checker.team = team
    checker.type = CheckerType.men()
    game_objects.state.add_checker(checker)


def run():
    MOUSE_BUTTON_LEFT = 1
    MOUSE_BUTTON_RIGHT = 3

    while 1:
        pygame.display.get_surface().fill((255, 255, 255))

        update()
        render()
        pygame.display.flip()

        if game_objects.menu.is_visible():
            game_objects.menu.set_current_mouse_pos(pygame.mouse.get_pos())

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONUP and event.button == MOUSE_BUTTON_LEFT:

                pos = pygame.mouse.get_pos()
                coord = game_objects.board.coord_to_square(pos)
                game_objects.game.left_click(coord)

                if game_objects.menu.is_visible():
                    clicked = game_objects.menu.coord_to_item(pos)

                    if not clicked == -1:
                        game_objects.menu.toggle()

            if event.type == pygame.MOUSEBUTTONUP and event.button == MOUSE_BUTTON_RIGHT:
                game_objects.game.right_click()



            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_objects.menu.toggle()


def render():
    game_objects.board.render()

    checkers = game_objects.state.checkers

    for c in checkers:
        c.render()


    game_objects.menu.render()
    game_objects.overlay.render()


def update():
    game_objects.menu.update()
    checkers = game_objects.state.checkers

    for c in checkers:
        c.update()

    game_objects.menu.render()
    game_objects.overlay.update()


if __name__=="__main__":main()