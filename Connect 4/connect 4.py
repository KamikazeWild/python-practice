import numpy as np
import pygame
import sys
import math

ROW_COUNT = 6
COL_COUNT = 7

SQUARESIZE = 80
height = (ROW_COUNT+1) * SQUARESIZE
width = COL_COUNT * SQUARESIZE
size = (width, height)
RADIUS = int(SQUARESIZE/2 - 3)

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

pygame.init()

myfont = pygame.font.SysFont("monospace", 60, bold=True)

def create_board():
    matrix = np.zeros((ROW_COUNT, COL_COUNT))
    return matrix


def draw_board(board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE + SQUARESIZE/2), int(r*SQUARESIZE + SQUARESIZE + SQUARESIZE/2)), RADIUS)
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE + SQUARESIZE/2), height - int(r*SQUARESIZE + SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, GREEN, (int(c*SQUARESIZE + SQUARESIZE/2),height - int(r*SQUARESIZE + SQUARESIZE/2)), RADIUS)


    pygame.display.update()


def print_board(board):
    print(np.flip(board, 0))


def is_valid_location(board, col):
    if board[5][col] == 0:
        return True


def next_empty_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def winning_move(piece):
    # checking horizontally
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    # checking vertically
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    # checking positive slope
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    # checking negative slope
    for c in range(COL_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


board = create_board()
print_board(board)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

turn = 0
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            elif turn == 1:
                pygame.draw.circle(screen, GREEN, (posx, int(SQUARESIZE/2)), RADIUS)

            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            # Player 1 input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                if is_valid_location(board, col):
                    row = next_empty_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(1):
                        label = myfont.render("Player 1 wins!!!", 1, RED)
                        screen.blit(label, (30, 7))
                        game_over = True

            # Player 2 input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
                if is_valid_location(board, col):
                    row = next_empty_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(2):
                        label = myfont.render("Player 2 wins!!!", 1, GREEN)
                        screen.blit(label, (30, 7))
                        game_over = True

            draw_board(board)
            print_board(board)
            turn += 1
            turn %= 2

    if game_over:
        pygame.time.wait(1500)

