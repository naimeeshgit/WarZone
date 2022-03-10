import global_variable as gv
import building as b
from initialise import Game_Map, townhall, list_hut, canon_list, wall


class Character:

    def move(self, direction, array, pseudo_array):
        old_x = self.x_coor
        old_y = self.y_coor

        if self.type == "king":
            if direction == "w":
                if(self.x_coor > 0):
                    if(array[self.x_coor-1][self.y_coor] != " "):
                        array[self.x_coor][self.y_coor] = "K"
                    else:
                        self.x_coor -= 1
                        array[old_x][old_y] = " "
                        pseudo_array[old_x][old_y] = " "
                        array[self.x_coor][self.y_coor] = "K"
                        pseudo_array[self.x_coor][self.y_coor] = "K"

                self.last_move = "w"
            elif direction == "s":
                if(self.x_coor < gv.m-1):
                    if(array[self.x_coor+1][self.y_coor] != " "):
                        array[self.x_coor][self.y_coor] = "K"
                    else:
                        self.x_coor += 1
                        array[old_x][old_y] = " "
                        pseudo_array[old_x][old_y] = " "
                        array[self.x_coor][self.y_coor] = "K"
                        pseudo_array[self.x_coor][self.y_coor] = "K"

                self.last_move = "s"
            elif direction == "a":
                if(self.y_coor > 0):
                    if(array[self.x_coor][self.y_coor-1] != " "):
                        array[self.x_coor][self.y_coor] = "K"
                    else:
                        self.y_coor -= 1
                        array[old_x][old_y] = " "
                        pseudo_array[old_x][old_y] = " "
                        array[self.x_coor][self.y_coor] = "K"
                        pseudo_array[self.x_coor][self.y_coor] = "K"

                self.last_move = "a"
            elif direction == "d":
                if(self.y_coor < gv.n-1):
                    if(array[self.x_coor][self.y_coor+1] != " "):
                        array[self.x_coor][self.y_coor] = "K"
                    else:
                        self.y_coor += 1
                        array[old_x][old_y] = " "
                        pseudo_array[old_x][old_y] = " "
                        array[self.x_coor][self.y_coor] = "K"
                        pseudo_array[self.x_coor][self.y_coor] = "K"

                self.last_move = "d"

        elif self.type == "barbarians":
            pass

    def damage():
        pass

    def attack(self, array, pseudo_array):
        # print(self.x_coor, self.y_coor)
        curr_X = self.x_coor
        curr_Y = self.y_coor
        if self.last_move == "w":
            # print("we can attack")
            if(pseudo_array[curr_X-1][curr_Y] != ' '):
                code = pseudo_array[curr_X-1][curr_Y]
                # parse code into letter and number
                if code[0] == 'T':
                    townhall.damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'H':
                    code = code[1:len(code):1]
                    list_hut[int(code)].damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'C':
                    code = code[1:len(code):1]
                    canon_list[int(code)].damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'W':
                    code = code[1:len(code):1]
                    code = int(code)
                    wall[code].damage(self.attack_power, array, pseudo_array)

        elif self.last_move == "s":
            if(pseudo_array[curr_X+1][curr_Y] != ' '):
                code = pseudo_array[curr_X+1][curr_Y]
                # parse code into letter and number
                if code[0] == 'T':
                    townhall.damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'H':
                    code = code[1:len(code):1]
                    list_hut[int(code)].damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'C':
                    code = code[1:len(code):1]
                    canon_list[int(code)].damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'W':
                    code = code[1:len(code):1]
                    code = int(code)
                    wall[code].damage(self.attack_power, array, pseudo_array)
        elif self.last_move == "a":
            if(pseudo_array[curr_X][curr_Y-1] != ' '):
                code = pseudo_array[curr_X][curr_Y-1]
                # parse code into letter and number
                if code[0] == 'T':
                    townhall.damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'H':
                    code = code[1:len(code):1]
                    list_hut[int(code)].damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'C':
                    code = code[1:len(code):1]
                    canon_list[int(code)].damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'W':
                    code = code[1:len(code):1]
                    code = int(code)
                    wall[code].damage(self.attack_power, array, pseudo_array)
        elif self.last_move == "d":
            if(pseudo_array[curr_X][curr_Y+1] != ' '):
                code = pseudo_array[curr_X][curr_Y+1]
                # parse code into letter and number
                if code[0] == 'T':
                    townhall.damage(self.attack_power, array, pseudo_array)
                elif code[0] == 'H':
                    code = code[1:len(code):1]
                    list_hut[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'C':
                    code = code[1:len(code):1]
                    canon_list[int(code)].damage(
                        self.attack_power, array, pseudo_array)
                elif code[0] == 'W':
                    code = code[1:len(code):1]
                    code = int(code)
                    wall[code].damage(self.attack_power, array, pseudo_array)


class king(Character):
    def __init__(self, x_coor, y_coor, array, pseudo_array):
        self.type = "king"
        self.x_coor = x_coor
        self.y_coor = y_coor
        array[self.x_coor][self.y_coor] = "K"
        pseudo_array[self.x_coor][self.y_coor] = "K"
        self.health = gv.max_health_king
        self.last_move = " "
        self.attack_power = gv.attack_power_king


class barbarians(Character):
    def __init__(self, x_coor, y_coor, array, pseudo_array):
        self.type = "barbarians"
        self.x_coor = x_coor
        self.y_coor = y_coor
        array[self.x_coor][self.y_coor] = "B"
        pseudo_array[self.x_coor][self.y_coor] = "B"
        self.health = gv.max_health_barbarians
        self.last_move = " "
        self.attack_power = gv.attack_power_barbarians
