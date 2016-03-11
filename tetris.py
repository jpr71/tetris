import sys
from random import randint
import pyautogui

def build_block(block):
    return "*" if block == 1 else " "


def join(generator):
    return ''.join(list(generator))


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def reverse(matrix):
    return [list(reversed(row)) for row in matrix]


class Block(object):
    """
    Block object
    """
    

    def __init__(self, top=None, left=None):
        """
        name_of_the_block = block,width and height 
        """
        block1=[[[1,1,1,1]],4,1]  
        block2=[[[0,1],[0,1],[1,1]],2,3]
        block3=[[[1,0],[1,0],[1,1]],2,3]
        block4=[[[0,1],[1,1],[1,0]],2,3]
        block5=[[[1,1],[1,1]],2,2]
        
        
        blocks = [block1,block2,block3,block4,block5]
        index = randint(0,100000)%5
        print index
        chosen_one = blocks[index]
        self.top = top
        self.left = left
        self.height =chosen_one[2]
        self.width = chosen_one[1]
        self.matrix = chosen_one[0]

    def rotate_clockwise(self):
        self.matrix = reverse(transpose(self.matrix)) #rotating clock-wise

    def rotate_counter_clockwise(self):
        self.matrix = transpose(reverse(self.matrix)) #rotate counter-clock-wise


class Screen(object):
    """
    Screen Object
    """

    def __init__(self, height=20, width=20):
        self.height = height
        self.width = width
        self.matrix = [
            [1] + [0 for _ in range(width)] + [1]
            for __ in range(height)] + [[1 for _ in range(width + 2)]]

    def __str__(self):
        """
        Defining what to draw on screen
        """
        string = join(build_block(block) for block in self.matrix[0])
        for row in self.matrix[1:-1]:
            string += "\n"
            string += join(build_block(block) for block in row)
        string += "\n"
        string += join(build_block(block) for block in self.matrix[-1])
        return string

    def does_fit(self, block, row, col):
        """
        Checks the availability of the move
        """
        try:
            return all(c + self.matrix[row + row_index][col + col_index] in (0, 1)
                       for row_index, new_row in enumerate(block.matrix)
                       for col_index, c in enumerate(new_row))
        except IndexError:
            return False

    def place(self, block, y, x):
        for row_index, new_row in enumerate(block.matrix):
            for col_index, c in enumerate(new_row):
                self.matrix[y + row_index][x + col_index] += c
        block.top = y
        block.left = x

    def delete(self, block, y, x):
        for row_index, new_row in enumerate(block.matrix):
            for col_index, c in enumerate(new_row):
                self.matrix[y + row_index][x + col_index] -= c
        block.top = y
        block.left = x


def new_block_coming(screen, block):
    top = 0
    left = randint(1, screen.width-block.width)
    if screen.does_fit(block, top, left):
        screen.place(block, top, left)
    else:
        raise Exception

def right(screen, block):
    screen.delete(block, block.top, block.left)
    if screen.does_fit(block, block.top, block.left+1):
        screen.place(block, block.top, block.left+1)
    else:
        screen.place(block, block.top, block.left)
        print "Invalid Move!"


def left(screen, block):
    screen.delete(block, block.top, block.left)
    if screen.does_fit(block, block.top, block.left-1):
        screen.place(block, block.top, block.left-1)
    else:
        screen.place(block, block.top, block.left)
        print "Invalid Move!"

def down(screen, block):
    screen.delete(block, block.top, block.left)
    if screen.does_fit(block, block.top+1, block.left):
        screen.place(block, block.top+1, block.left)
    else:
        screen.place(block, block.top, block.left)
        raise Exception
        

def rotate_clockwise(screen, block):
    screen.delete(block, block.top, block.left)
    block.rotate_clockwise()
    if screen.does_fit(block, block.top, block.left):
        screen.place(block, block.top, block.left)
    else:
        block.rotate_counter_clockwise()
        screen.place(block, block.top, block.left)
        print "Invalid Move!"


def rotate_counter_clockwise(screen, block):
    screen.delete(block, block.top, block.left)
    block.rotate_counter_clockwise()
    if screen.does_fit(block, block.top, block.left):
        screen.place(block, block.top, block.left)
    else:
        block.rotate_clockwise()
        screen.place(block, block.top, block.left)
        print "Invalid Move!"


moves = {
        'a': left,
        'd': right,
        'w': rotate_counter_clockwise,
        's': rotate_clockwise
    }





if __name__ == '__main__':
    height = 20
    width = 20
    screen = Screen(height, width)
    block = Block()
    new_block_coming(screen, block)
    
    print screen

    pyautogui.press('return')
    commands = raw_input()
    pyautogui.keyDown('enter')

    while commands != 'EOF':
        try:
            down(screen, block)

        except:
            block = Block()

            try:
                new_block_coming(screen, block)
            except:
                print "GAME OVER"
                pyautogui.hotkey('ctrl', 'c')

        for command in commands:
            if command in moves:
                moves[command](screen,block)

        print screen
        commands = raw_input()
        pyautogui.PAUSE = 0.5
        pyautogui.press('return')