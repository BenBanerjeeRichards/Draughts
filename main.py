import pygame
import GameObjects
import GameBoard
import Checker
import Resource
import BoardState
import Teams
import GameAnalyser
import Menu
import Overlay
import CheckerType

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
    run()


def add_checker(team, location):
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

    game_objects.state.move_checker((4, 5), (3, 4))
    game_objects.state.move_checker((3, 2), (4, 3))
    game_objects.state.remove_checker((5, 2))
    game_objects.state.remove_checker((3, 0))
    game_objects.state.remove_checker((7, 0))

    print GameAnalyser.check_move_is_valid([(3, 4), (5, 2), (3, 1)], game_objects.state, Teams.black())

    while 1:
        board_coord = game_objects.board.get_padding()
        size = game_objects.board.get_dimentions()
        pygame.display.get_surface().fill((255, 255, 255))

        update()
        render()
        pygame.display.flip()

        if game_objects.menu.is_visible():
            game_objects.menu.set_current_mouse_pos(pygame.mouse.get_pos())

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONUP:

                pos = pygame.mouse.get_pos()
                print game_objects.board.coord_to_square(pos)
                if game_objects.menu.is_visible():
                    clicked = game_objects.menu.coord_to_item(pos)

                    if not clicked == -1:
                        game_objects.menu.toggle()

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