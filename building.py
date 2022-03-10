import colorama
from colorama import Fore, Back, Style
from matplotlib import offsetbox
colorama.init(autoreset=True)
# import global_var
# import util
import math
import numpy as np
import global_variable as gv
import scenery

class Building:
    
    def __init__(self, type, X_coor, Y_coor, health):
        pass

    def damage(self, damage, array, pseudo_array):
        self.health -= damage
        if self.health <= 0:
            for i in range(self.X_coor, self.X_coor+self.len):
                for j in range(self.Y_coor, self.Y_coor+self.width):
                    array[i][j] = ' '
                    pseudo_array[i][j] = ' ' 
        else :
            if self.health >= 0.5*self.max_health:
                self.color = Fore.GREEN
            elif self.health >= 0.2*self.max_health:
                self.color = Fore.YELLOW
            elif self.health > 0:
                self.color = Fore.RED
            
            if self.type == 'townhall':
                char = 'T'
            elif self.type == 'huts':
                char = 'H'
            elif self.type == 'canon':
                char = 'C'
            elif self.type == 'wall':
                char = 'W'

            for i in range(self.X_coor, self.X_coor+self.len):
                for j in range(self.Y_coor, self.Y_coor+self.width):
                    array[i][j] = self.color + char + Style.RESET_ALL
        
    
        
class Townhall(Building):
    def __init__(self, array, pseudo_array):
        self.type = "townhall"
        self.X_coor = int(gv.m/2)
        self.Y_coor = int(gv.n/2)
        self.len = 4
        self.width = 3
        self.max_health = gv.max_health_townhall
        self.health = self.max_health
        self.color = Fore.GREEN


        for i in range(self.X_coor, self.X_coor+self.len):
            for j in range(self.Y_coor, self.Y_coor+self.width):
                array[i][j] = self.color + 'T' + Style.RESET_ALL 
                pseudo_array[i][j] = 'T'

        
class Huts(Building):
    def __init__(self, X_coor, Y_coor, array, pseudo_array, hut_id):
        self.type = "huts"
        self.len = 1
        self.width = 1
        self.X_coor = X_coor
        self.Y_coor = Y_coor
        self.max_health = gv.max_health_huts
        self.health = self.max_health
        self.color = Fore.GREEN
        self.hut_id = hut_id
        

        for i in range(self.X_coor, self.X_coor+self.len):
            for j in range(self.Y_coor, self.Y_coor+self.width):
                array[i][j] =  self.color + 'H' + Style.RESET_ALL 
                pseudo_array[i][j] = 'H' + str(self.hut_id)
        

class Canon(Building):
    def __init__(self, X_coor, Y_coor, array, pseudo_array, canon_id):
        self.type = "canon"
        self.len = 1
        self.width = 1
        self.X_coor = X_coor
        self.Y_coor = Y_coor
        self.max_health = gv.max_health_canon
        self.health = self.max_health
        self.color = Fore.GREEN
        self.canon_id = canon_id

        array[self.X_coor][self.Y_coor] =  self.color + 'C' + Style.RESET_ALL 
        pseudo_array[self.X_coor][self.Y_coor] = 'C' + str(self.canon_id)


class Wall(Building):
    def __init__(self, X_coor, Y_coor, array, pseudo_array, wall_id):
        self.type = "wall"
        self.max_health = gv.max_health_wall
        self.health = self.max_health
        self.X_coor = X_coor
        self.Y_coor = Y_coor
        self.color = Fore.GREEN
        self.wall_id = wall_id
        self.len = 1
        self.width = 1
        
        array[X_coor][Y_coor] =  self.color + 'W' + Style.RESET_ALL
        pseudo_array[X_coor][Y_coor] = 'W' + str(self.wall_id)


        
        

        
        

    




        





    

    
    