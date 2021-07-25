from shutil import get_terminal_size
from os import system
from time import sleep

# menu element class
class gui():

    # start
    def __init__(self):

        self.size = [0, 0]
        self.visible = True
        self.eventList = []
        self.mas = []

        while self.visible:
            self.eventUpdate()
            self.generateFrame()

    # update (generating) frame
    def generateFrame(self):

        col, row = self.size[0], self.size[1]

        # print(self.eventList)
        if len(self.eventList) != 0:

            self.clr()

            if 'size' in self.eventList:
                self.mas = [[' ' for x in range(col)] for y in range(row)]
                self.draw(col, row)

            self.pprint()
            self.eventList = []


    def draw(self, col, row):

        mas = self.mas

        def drawAll():
            borders()

        def borders(offset=1):

            vertical, horizontal = '║', '═'
            ul, ur, dr, dl = '╔', '╗', '╝', '╚'

            # vertical borders
            xl, xr = 0 + offset, col - 1 - offset

            for i in range(offset + 1, row - offset):
                mas[i][xl] = vertical; mas[i][xr] = vertical

            # horizontal borders
            yu, yd = 1 + offset, row - 1 - offset

            for i in range(offset + 1, col - offset):
                mas[yu][i] = horizontal; mas[yd][i] = horizontal

            mas[xl+1][yu-1] = ul # upper  left  border
            mas[yd][xl] = dl # down   left  border
            mas[yu][xr] = ur # upper  right border
            mas[yd][xr] = dr # down   right border

        self.mas = mas
        drawAll()

    # ------------------ EVENTS OF CONSOLE ------------------ #

    def eventUpdate(self, offset=0.1):

        # ------ CONSOLE SIZE EVENT ------- #
        # storing the value of the console  #
        temp = self.size                    #
        self.nowSize()                      #
        #                                   #
        # differ them beetween each other   #
        if temp != self.size:               #
            self.eventList.append('size')   #
        # --------------------------------- #

        sleep(offset)

    # ------------------ SERVICE FUNCTIONS -------------------#

    # pretty print of the doubled massive
    def pprint(self):
        print('\n'.join([''.join(row) for row in self.mas]))

    # clear console
    def clr(self):
        system('cls')

    # update size of the console
    def nowSize(self):
        column, rows = get_terminal_size()
        self.size = [column, rows]

    # adding border type
    def addBorderType(self, name, borders):
        self.borders[name] = borders

    #---------------------------------------------------------#

# block object
class block():

    def __init__(self):

        self.properties = {

        }

test = gui()