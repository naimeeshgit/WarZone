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
            elif self.type == 'wizard_tower':
                char = 'Y'
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

    def attack(self, array, pseudo_array, king, barbarians, archers):
        if(((self.X_coor-king.x_coor)**2 + (self.Y_coor - king.y_coor)**2 <= 36) and (king.x_coor != -1 and king.y_coor != -1) and king.health > 0):
                array[self.X_coor][self.Y_coor] = self.color + Back.RED + 'C' + Style.RESET_ALL
                king.health -= self.attack_power
                if(king.health <=0):
                    king.destroy(array, pseudo_array)
        else:
            troop = []
            troop.append(barbarians)
            troop.append(archers)
            for i in range(len(troop)):
                for j in troop[i]:
                    if(((self.X_coor-j.x_coor)**2 + (self.Y_coor - j.y_coor)**2 <= 25) and (j.x_coor != -1 and j.y_coor != -1) and j.health > 0):
                        array[self.X_coor][self.Y_coor] = self.color + Back.RED + 'C' + Style.RESET_ALL
                        j.health -= self.attack_power
                        if(j.health <=0):
                            j.destroy(array, pseudo_array)
                        break
            


class Wizard_tower(Building):
    def __init__(self, X_coor, Y_coor, array, pseudo_array, wizard_tower_id):
        self.type = "wizard_tower"
        self.len = 1
        self.width = 1
        self.X_coor = X_coor
        self.Y_coor = Y_coor
        self.max_health = gv.max_health_wizard_tower
        self.health = self.max_health
        self.color = Fore.GREEN
        self.wizard_tower_id = wizard_tower_id
        self.attack_power = gv.wizard_tower_damage

        array[self.X_coor][self.Y_coor] =  self.color + 'Y' + Style.RESET_ALL 
        pseudo_array[self.X_coor][self.Y_coor] = 'Y' + str(self.wizard_tower_id)

    def attack(self, array, pseudo_array, king, barbarians, archers, balloons):
        if(((self.X_coor-king.x_coor)**2 + (self.Y_coor - king.y_coor)**2 <= 25) and (king.x_coor != -1 and king.y_coor != -1) and king.health > 0):
                array[self.X_coor][self.Y_coor] = self.color + Back.RED + 'Y' + Style.RESET_ALL
                king.health -= self.attack_power
                if(king.health <=0):
                    king.destroy(array, pseudo_array)
        else:
            troop = []
            troop.append(barbarians)
            troop.append(archers)
            troop.append(balloons)
            target = []
            found = False
            for i in range(len(troop)):
                for j in troop[i]:
                    if(((self.X_coor-j.x_coor)**2 + (self.Y_coor - j.y_coor)**2 <= 25) and (j.x_coor != -1 and j.y_coor != -1) and j.health > 0):
                        target.append(j)
                        found = True
                        break
                if(found):
                    break
            # troops in 3*3 area should also be targetted
            # print(target)
            if(found):
                for k in range(len(troop)):
                    for l in troop[k]:
                        abs_man_x = abs(l.x_coor - j.x_coor)
                        abs_man_y = abs(l.y_coor - j.y_coor)

                        if(abs_man_x <= 3/2 and abs_man_y <= 3/2):
                            target.append(l)
                
                for targ in target:
                    array[self.X_coor][self.Y_coor] = self.color + Back.RED + 'Y' + Style.RESET_ALL
                    targ.health -= self.attack_power
                    if(targ.health <=0):
                        targ.destroy(array, pseudo_array)
                        
                    
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


        


        
        

    




        





    

    
    