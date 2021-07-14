import sys
import pygame as pg
import time

pg.init()
screen_sz = 750, 850
screen = pg.display.set_mode(screen_sz)
font = pg.font.SysFont('Corbel', 60)
smallfont = pg.font.SysFont('Corbel', 25)
superscriptfont = pg.font.SysFont('Corbel', 20)

superscripts = [[0] * 9 for i in range(9)]


# DRAW BACKGROUND FUNCTION
def draw_bg():
    screen.fill(pg.Color((50, 50, 50)))

    board_area = pg.Surface([720, 720])
    board_area.fill(pg.Color((200, 200, 200)))

    screen.blit(board_area, (15, 65))

    pg.draw.rect(screen, pg.Color('black'), pg.Rect(15, 65, 720, 720), 5)

    line_thickness = 0

    i = 1
    while (i * 80) < 720:
        if i % 3 == 0:
            line_thickness = 3
        else:
            line_thickness = 1
        
        pg.draw.line(screen, pg.Color('black'), pg.Vector2((i * 80 + 15), 65), pg.Vector2((i * 80 + 15), 785), line_thickness)
        i += 1

    j = 1
    while (j * 80) < 720:
        if j % 3 == 0:
            line_thickness = 3
        else:
            line_thickness = 1
        pg.draw.line(screen, pg.Color('black'), pg.Vector2(15, (j * 80 + 65)), pg.Vector2(735, (j * 80 + 65)), line_thickness)
        j += 1


# DRAW VALUES FUNCTION
def draw_vals(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                output = font.render(str(board[row][col]), True, pg.Color('black'))
                screen.blit(output, pg.Vector2(col * 80 + 43, row * 80 + 75))
            if superscripts[row][col] != 0:
                output = superscriptfont.render(str(superscripts[row][col]), True, pg.Color('black'))
                screen.blit(output, pg.Vector2(col * 80 + 80, row * 80 + 70))

# button colors
hovered_color = (200, 200, 200)
nothovered_color = (100, 100, 100)
# button text
solve_text = smallfont.render('solve', True, pg.Color('black'))
easy_text = smallfont.render('easy', True, pg.Color('black'))
med_text = smallfont.render('med', True, pg.Color('black'))
hard_text = smallfont.render('hard', True, pg.Color('black'))

# DRAW BUTTONS FUNCTION
def draw_buttons(mouse):
    button_area = pg.Surface([80, 30])
    button_area.fill(pg.Color(nothovered_color))

    if 15 <= mouse[0] <= 95 and 20 <= mouse[1] <= 50:
        button_area.fill(pg.Color(hovered_color))

    screen.blit(button_area, (15, 20))
    screen.blit(solve_text, (30, 22))

    button_area.fill(pg.Color(nothovered_color))

    if 150 <= mouse[0] <= 230 and 20 <= mouse[1] <= 50:
        button_area.fill(pg.Color(hovered_color))

    screen.blit(button_area, (150, 20))
    screen.blit(easy_text, (165, 22))

    button_area.fill(pg.Color(nothovered_color))

    if 245 <= mouse[0] <= 325 and 20 <= mouse[1] <= 50:
        button_area.fill(pg.Color(hovered_color))

    screen.blit(button_area, (245, 20))
    screen.blit(med_text, (260, 22))

    button_area.fill(pg.Color(nothovered_color))

    if 340 <= mouse[0] <= 420 and 20 <= mouse[1] <= 50:
        button_area.fill(pg.Color(hovered_color))

    screen.blit(button_area, (340, 20))
    screen.blit(hard_text, (355, 22))

    button_area.fill(pg.Color(nothovered_color))



# BUTTON CLICK FUNCTION
def button_click(mouse):
    if 15 <= mouse[0] <= 95 and 20 <= mouse[1] <= 50:
        return 0

    if 150 <= mouse[0] <= 230 and 20 <= mouse[1] <= 50:
        return 1

    if 245 <= mouse[0] <= 325 and 20 <= mouse[1] <= 50:
        return 2

    if 340 <= mouse[0] <= 420 and 20 <= mouse[1] <= 50:
        return 3

    return -1


def board_click(mouse):
    for i in range(9):
        for j in range(9):
            if j * 80 + 15 <= mouse[0] <= (j + 1) * 80 + 15 and i * 80 + 65 <= mouse[1] <= (i + 1) * 80 + 65:
                return (i, j)




def select_number(puzzle, box, button, key, board):
    row, col = box

    if button == 1:
        if key != 0:
            oldval = board[row][col]
            board[row][col] = key

            if not puzzle.isValid(board, row, col):
                timer = time.time()

                while timer + 0.5 >= time.time():
                    decorate_square(row, col, 'red')

                board[row][col] = oldval
        else:
            board[row][col] = key

    elif button == 3:
        superscripts[row][col] = key
        draw_vals(board)



# SQUARE DECORATE FUNCTION
def decorate_square(row, col, state):
    if state == 'insert':
         pg.draw.rect(screen, pg.Color('green'), pg.Rect((col * 80 + 15), (row * 80 + 65), 80, 80), 5)
    else:
        pg.draw.rect(screen, pg.Color('red'), pg.Rect((col * 80 + 15), (row * 80 + 65), 80, 80), 5)

    pg.display.flip()



# CLEAR SUPERSCRIPTS
def hintsClear():
    for i in range(9):
        for j in range(9):
            superscripts[i][j] = 0



# SOME GLOBAL VARS
box = None
mouseButton = None
clear = 0

# MAIN FUNCTION
def main_loop(puzzle, board, eventEnable):
    global box
    global mouseButton
    global clear

    if not eventEnable and clear == 0:
        hintsClear()
        clear += 1
    elif eventEnable:
        clear = 0

    option = -1
    
    mouse = pg.mouse.get_pos()

    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN:
            option = button_click(mouse)
            box = board_click(mouse)
            if box != None:
                mouseButton = event.button
        
        if eventEnable:
            if box != None:
                if event.type == pg.KEYDOWN:
                    if puzzle.clues[box[0]][box[1]] == 0:
                        if(48 <= event.key <= 57):
                            select_number(puzzle, box, mouseButton, event.key - 48, board)
                            box = None
                            mouseButton = None

    draw_bg()
    draw_buttons(mouse)
        
    draw_vals(board)

    pg.display.flip()

    return option