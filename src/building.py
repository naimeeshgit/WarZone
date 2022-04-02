import colorama
from colorama import Fore, Back, Style
from matplotlib import offsetbox
colorama.init(autoreset=True)
import src.global_variable as gv


class Building:
    
    def __init__(self, type, X_coor, Y_coor, health):
        pass

    def damage(self, damage, array, pseudo_array):
        self.health -= damage
        if self.health <= 0:
            old_X = self.X_coor 
            old_Y = self.Y_coor
            for i in range(old_X, old_X+self.len):
                for j in range(old_Y, old_Y+self.width):
                    array[i][j] = ' '
                    pseudo_array[i][j] = ' ' 
                    self.X_coor = 1000
                    self.Y_coor = 1000
                    self.attack_power = 0
    
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
        self.attack_power = 0


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
        self.attack_power = 0
        

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
        self.attack_power = gv.canon_damage

        array[self.X_coor][self.Y_coor] =  self.color + 'C' + Style.RESET_ALL 
        pseudo_array[self.X_coor][self.Y_coor] = 'C' + str(self.canon_id)

    def attack(self, array, pseudo_array, king, barbarians):
        if(((self.X_coor-king.x_coor)**2 + (self.Y_coor - king.y_coor)**2 <= 36) and (king.x_coor != -1 and king.y_coor != -1) and king.health > 0):
                array[self.X_coor][self.Y_coor] = Back.RED + 'C' + Style.RESET_ALL
                king.health -= self.attack_power
                if(king.health <=0):
                    king.destroy(array, pseudo_array)
        else:
            for i in barbarians:
                if(i.x_coor > 0 and i.y_coor > 0 and i.health > 0):
                    if((self.X_coor-i.x_coor)**2 + (self.Y_coor - i.y_coor)**2 <= 25):
                        array[self.X_coor][self.Y_coor] = Back.RED + 'C' + Style.RESET_ALL
                        i.health -= self.attack_power
                        if i.health <= 0:
                            i.destroy(array, pseudo_array)
                        break
        

        


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
        self.attack_power = 0
        
        array[X_coor][Y_coor] =  self.color + 'W' + Style.RESET_ALL
        pseudo_array[X_coor][Y_coor] = 'W' + str(self.wall_id)


        
        

        
        

    




        





    

    
    