import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# gameboard shape 
m = 20
n = 60


# LOST VARIABLE
Lost = False

# Buildings
max_health_townhall = 101
max_health_huts = 42
max_health_wall = 15
max_health_canon = 30
max_health_wizard_tower = 30


canon_damage = 8
wizard_tower_damage = 8




# Characters
max_health_king = 100
max_health_barbarians = 40
max_health_archer_queen = 100
max_health_archers = 20
max_health_balloons = 40


attack_power_king = 6
attack_power_barbarians = 3
attack_power_nuke = 101
attack_power_archers = 1.5
attack_power_balloons = 6
attack_power_archer_queen = 5

range_archer = 8



#spells
Rage_spell = False
Rage_step = 10

# weapon
Nuke = False
Nuke_count = 0
Nuke_isdestroyed = False


# replays
replay = []