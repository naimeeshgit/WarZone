# make a class for gameboard in green color
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import global_variable as gv
import numpy as np
import os


class GameBoard:
    def __init__(self):
        # self.array = np.empty((gv.m, gv.n), dtype=str) 
        self.array=[[' ' for i in range(gv.n)] for j in range(gv.m)]
        self.pseudo_array = [[' ' for i in range(gv.n)] for j in range(gv.m)]

        # add a 'X' to the boundary of the gameboard
        for i in range(gv.m):
            self.array[i][0] = 'X'
            self.array[i][gv.n-1] = 'X'    

        for j in range(gv.n):
            self.array[0][j] = 'X'
            self.array[gv.m-1][j] = 'X'    

    def print_board(self):
        os.system("cls" if os.name == "nt" else "clear")
        for i in range(gv.m):
            for j in range(gv.n):
                print(self.array[i][j], end="")
            print()
        # print()
    def print_pseudo_array(self):
        for i in range(gv.m):
            for j in range(gv.n):
                print(self.pseudo_array[i][j], end="")
            print()


        





