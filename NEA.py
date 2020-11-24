# import the pygame module
import pygame
import sys
from pygame.locals import *
import random
import time

# colours
WHITE = 255, 255, 255
GREY = 192, 192, 192
RED = 255, 0, 0
BLUE = 0, 0, 255
GREEN = 0, 255, 0
PLAYER_GREEN = 0, 150, 0
DARK_GREEN = 0, 96, 0
YELLOW = 255, 255, 0
PLAYER_YELLOW = 255, 200, 0

# number of frames per second
FPS = 60

# loads the logo and sets it
logo = pygame.image.load("icon.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("Triumph")

pygame.init()

# loads font
font = pygame.font.SysFont("robotocondensed", 14)
title = pygame.font.SysFont("robotocondensed", 72)
box_font = pygame.font.SysFont("robotocondensed", 22)
money_font = pygame.font.SysFont("robotocondensed", 12)
triumph_font = pygame.font.SysFont("robotocondensed", 50)

# window size depends on size of board
screen = pygame.display.set_mode((10*50+55, 10*50+55))

# renders all money held by different teams and blits this onto the surface
def moneybox(money, X_LENGTH, Y_LENGTH):
    red_money_render = money_font.render("Red: " + str(money[0]), True, RED)
    blue_money_render = money_font.render("Blue: " + str(money[1]), True, BLUE)
    green_money_render = money_font.render("Green: " + str(money[2]), True, PLAYER_GREEN)
    yellow_money_render = money_font.render("Yellow: " + str(money[3]), True, PLAYER_YELLOW)
    screen.blit(red_money_render, (X_LENGTH*50+5, 305))
    screen.blit(blue_money_render, (X_LENGTH*50+5, 315))
    screen.blit(green_money_render, (X_LENGTH*50+5, 325))
    screen.blit(yellow_money_render, (X_LENGTH*50+5, 335))

def addmoney(money, colour_coordinates, X_LENGTH, Y_LENGTH):
    size = [0,0,0,0]
    for x in range(X_LENGTH):
        for y in range(Y_LENGTH):
            if colour_coordinates[x][y][0] == "red":
                money[0] += 1
                size[0] += 1
            
            elif colour_coordinates[x][y][0] == "blue":
                money[1] += 1
                size[1] += 1
            
            elif colour_coordinates[x][y][0] == "green":
                money[2] += 1
                size[2] += 1
           
            elif colour_coordinates[x][y][0] == "yellow":
                money[3] += 1
                size[3] += 1
    
    if size[0] == X_LENGTH * Y_LENGTH:
        p_win = triumph_font.render("Team Red Triumphs!", True, RED)
        screen.blit(p_win, (10, 10))
        pygame.display.update()
        pygame.time.Clock().tick(FPS)
        time.sleep(5)
        menu(10, 10, "small")
    
    elif size[1] == X_LENGTH * Y_LENGTH:
        p_win = triumph_font.render("Team Blue Triumphs!", True, BLUE)
        screen.blit(p_win, (10, 10))
        pygame.display.update()
        pygame.time.Clock().tick(FPS)
        time.sleep(5)
        menu(10, 10, "small")
    
    elif size[2] == X_LENGTH * Y_LENGTH:
        p_win = triumph_font.render("Team Green Triumphs!", True, PLAYER_GREEN)
        screen.blit(p_win, (10, 10))
        pygame.display.update()
        pygame.time.Clock().tick(FPS)
        time.sleep(5)
        menu(10, 10, "small")
    
    elif size[3] == X_LENGTH * Y_LENGTH:
        p_win = triumph_font.render("Team Yellow Triumphs!", True, PLAYER_YELLOW)
        screen.blit(p_win, (10, 10))
        pygame.display.update()
        pygame.time.Clock().tick(FPS)
        time.sleep(5)
        menu(10, 10, "small")


    return money, colour_coordinates

def randomise_coordinates(colour_coordinates, X_LENGTH, Y_LENGTH):
    space = []

    for i in range(X_LENGTH):
        for o in range(Y_LENGTH):
            space.append([i,o])
        
    random.shuffle(space)

    r_start = list.pop(space)
    b_start = list.pop(space)
    g_start = list.pop(space)
    y_start = list.pop(space)

    print(r_start, b_start)

    r_start_x = r_start[0]
    r_start_y = r_start[1]
    b_start_x = b_start[0]
    b_start_y = b_start[1]
    g_start_x = g_start[0]
    g_start_y = g_start[1]
    y_start_x = y_start[0]
    y_start_y = y_start[1]

    colour_coordinates[r_start_x][r_start_y][0] = "red"
    colour_coordinates[b_start_x][b_start_y][0] = "blue"
    colour_coordinates[g_start_x][g_start_y][0] = "green"
    colour_coordinates[y_start_x][y_start_y][0] = "yellow"
    
    return colour_coordinates

# blits the text onto the surface
def textbox(text, Y_LENGTH):
    box_text = box_font.render(text, True, (50, 50, 50))
    screen.blit(box_text, (20, Y_LENGTH*50 + 20))

def button_labels(X_LENGTH):
    next = money_font.render('Next Turn', True, (255, 255, 255))
    exit = money_font.render('Exit', True, (255, 255, 255))
    screen.blit(next, (X_LENGTH*50+5, 40))
    screen.blit(exit, (X_LENGTH*50+5, 290))

def load_unit_coordinates(load_unit):
    f = open(load_unit,"r")
    unit_coordinates = eval(f.read())
    f.close()
    return unit_coordinates

def load_colour_coordinates(load_colour):
    f = open(load_colour,"r")
    colour_coordinates = eval(f.read())
    f.close()
    return colour_coordinates

def reset_unit_coordinates(load_unit_new):
    f = open(load_unit_new,"r")
    unit_coordinates = eval(f.read())
    f.close()
    return unit_coordinates

def reset_colour_coordinates(load_colour_new):
    f = open(load_colour_new,"r")
    colour_coordinates = eval(f.read())
    f.close()
    return colour_coordinates

def load_money():
    f = open("money.txt","r")
    money = eval(f.read())
    f.close()
    return money

def get_team():
    f = open("team.txt","r")
    team = eval(f.read())
    f.close()
    return team

# performs movement of pieces, verifying whether or not a move is valid.
def movement(to_move, to_move_x, to_move_y, move_to, move_to_x, move_to_y, unit_coordinates, colour_coordinates, move_colour_1, move_colour_2, text1, team):
    if (int(move_to_x) == int(to_move_x) - 1 and int(move_to_y) == int(to_move_y)) or (int(move_to_x) == int(to_move_x) + 1 and int(move_to_y) == int(to_move_y) or (int(move_to_y) == int(to_move_y) - 1 and int(move_to_x) == int(to_move_x)) or (int(move_to_y) == int(to_move_y) + 1 and int(move_to_x) == int(to_move_x)) or move_to == to_move):

        if unit_coordinates[move_to_x][move_to_y][0] == 0 and unit_coordinates[to_move_x][to_move_y][2] >= 0 and (unit_coordinates[to_move_x][to_move_y][0] == 'infantry' or unit_coordinates[to_move_x][to_move_y][0] == 'tank') and colour_coordinates[to_move_x][to_move_y][0] == team and colour_coordinates[to_move_x][to_move_y][1] != team:
            
            # performs a swap of the unit to move and the tile in which the unit will be moved
            unit_coordinates[move_to_x][move_to_y][0], unit_coordinates[move_to_x][move_to_y][1], unit_coordinates[move_to_x][move_to_y][2] = unit_coordinates[to_move_x][to_move_y][0], unit_coordinates[to_move_x][to_move_y][1], unit_coordinates[to_move_x][to_move_y][2]
            unit_coordinates[to_move_x][to_move_y][0], unit_coordinates[to_move_x][to_move_y][1], unit_coordinates[to_move_x][to_move_y][2] = 0, 0, 0
            colour_coordinates[move_to_x][move_to_y][0] = move_colour_1

            # deducts a movement point from the unit
            if colour_coordinates[move_to_x][move_to_y][2] == 'snow':
                unit_coordinates[move_to_x][move_to_y][1] -= 2
            
            else:
                unit_coordinates[move_to_x][move_to_y][1] -= 1

        elif unit_coordinates[move_to_x][move_to_y][3] == 0 and unit_coordinates[to_move_x][to_move_y][5] >= 0 and (unit_coordinates[to_move_x][to_move_y][3] == 'bomber' or unit_coordinates[to_move_x][to_move_y][3] == 'fighter') and unit_coordinates[to_move_x][to_move_y][4] > 0:
            unit_coordinates[move_to_x][move_to_y][3], unit_coordinates[move_to_x][move_to_y][4], unit_coordinates[move_to_x][move_to_y][5] = unit_coordinates[to_move_x][to_move_y][3], unit_coordinates[to_move_x][to_move_y][4], unit_coordinates[to_move_x][to_move_y][5]
            unit_coordinates[to_move_x][to_move_y][3], unit_coordinates[to_move_x][to_move_y][4], unit_coordinates[to_move_x][to_move_y][5] = 0, 0, 0
            colour_coordinates[move_to_x][move_to_y][1] = move_colour_2
            colour_coordinates[to_move_x][to_move_y][1] = 0

            #if colour_coordinates[to_move_x][to_move_y][0] == team and unit_coordinates[to_move_x][to_move_y][0] != 0:
            #    unit_coordinates[move_to_x][move_to_y][4] = unit_coordinates[move_to_x][move_to_y][4]
            #else:
            unit_coordinates[move_to_x][move_to_y][4] -= 1

        # the scenario being handled deals with a ground unit attacking another, in different teams
        elif (unit_coordinates[move_to_x][move_to_y][0] != 0) and (colour_coordinates[move_to_x][move_to_y][0] != move_colour_1) and (unit_coordinates[to_move_x][to_move_y][0] == "infantry" or unit_coordinates[to_move_x][to_move_y][0] == "tank") and unit_coordinates[to_move_x][to_move_y][1] > 0:
            
            # sets the attack of infantry and tanks and reducts all movement points off attacking unit
            if unit_coordinates[to_move_x][to_move_y][0] == "infantry":
                attack = 2
            
            elif unit_coordinates[to_move_x][to_move_y][0] == "tank":
                attack = 5
            
            unit_coordinates[to_move_x][to_move_y][1] = 0

            # increased defence for units in jungle or desert means minor reduction of 1 attack for attackers
            if colour_coordinates[move_to_x][move_to_y][2] == 'jungle' or colour_coordinates[move_to_x][move_to_y][2] == 'desert':
                attack -= 1
            
            # much higher defence for snow regions, reduction of 2 attack for attackers
            elif colour_coordinates[move_to_x][move_to_y][2] == 'snow' and (attack - 2) > 0:
                attack -= 2

            # ensures that no matter the circumstance, units will always deal at least 1 damage to opponent
            elif (attack - 2) <= 0 and colour_coordinates[move_to_x][move_to_y][2] == 'snow':
                attack = 1
            
            # shows the outcome of the battle
            unit_coordinates[move_to_x][move_to_y][2] -= attack
            text1 = (unit_coordinates[move_to_x][move_to_y][0].title() + " loses " + str(attack) + " hp! " + str(unit_coordinates[move_to_x][move_to_y][2]) + " hp left.")

            # if the unit being attacked no longer has health points remaining, they are removed from the board and attacking unit moves into the vacated space
            if unit_coordinates[move_to_x][move_to_y][2] <= 0:
                unit_coordinates[move_to_x][move_to_y][0], unit_coordinates[move_to_x][move_to_y][1], unit_coordinates[move_to_x][move_to_y][2] = 0, 0, 0
                unit_coordinates[move_to_x][move_to_y][0], unit_coordinates[move_to_x][move_to_y][1], unit_coordinates[move_to_x][move_to_y][2] = unit_coordinates[to_move_x][to_move_y][0], unit_coordinates[to_move_x][to_move_y][1], unit_coordinates[to_move_x][to_move_y][2]
                unit_coordinates[to_move_x][to_move_y][0], unit_coordinates[to_move_x][to_move_y][1], unit_coordinates[to_move_x][to_move_y][2] = 0, 0, 0
                colour_coordinates[move_to_x][move_to_y][0] = move_colour_1

        elif (unit_coordinates[move_to_x][move_to_y][3] != 0) and (colour_coordinates[move_to_x][move_to_y][1] != move_colour_2) and (unit_coordinates[to_move_x][to_move_y][3] == "bomber" or unit_coordinates[to_move_x][to_move_y][3] == "fighter") and unit_coordinates[to_move_x][to_move_y][4] > 0:
            
            if unit_coordinates[to_move_x][to_move_y][3] == "bomber":
                attack = 2
            
            elif unit_coordinates[to_move_x][to_move_y][3] == "fighter":
                attack = 5
            
            unit_coordinates[to_move_x][to_move_y][4] = 0

            unit_coordinates[move_to_x][move_to_y][5] -= attack
            text1 = (unit_coordinates[move_to_x][move_to_y][3].title() + " loses " + str(attack) + " hp! " + str(unit_coordinates[move_to_x][move_to_y][5]) + " hp left.")
       
            if unit_coordinates[move_to_x][move_to_y][5] <= 0:
                unit_coordinates[move_to_x][move_to_y][3], unit_coordinates[move_to_x][move_to_y][4], unit_coordinates[move_to_x][move_to_y][5] = 0, 0, 0
                unit_coordinates[move_to_x][move_to_y][3], unit_coordinates[move_to_x][move_to_y][4], unit_coordinates[move_to_x][move_to_y][5] = unit_coordinates[to_move_x][to_move_y][3], unit_coordinates[to_move_x][to_move_y][4], unit_coordinates[to_move_x][to_move_y][5]
                unit_coordinates[to_move_x][to_move_y][3], unit_coordinates[to_move_x][to_move_y][4], unit_coordinates[to_move_x][to_move_y][5] = 0, 0, 0
                colour_coordinates[move_to_x][move_to_y][1] = move_colour_2

        elif to_move == move_to and (unit_coordinates[move_to_x][move_to_y][0] == "infantry" or unit_coordinates[move_to_x][move_to_y][0] == "tank") and unit_coordinates[to_move_x][to_move_y][3] == "bomber" and (colour_coordinates[move_to_x][move_to_y][0] != team) and unit_coordinates[to_move_x][to_move_y][4] > 0:

            attack = 5

            unit_coordinates[to_move_x][to_move_y][4] = 0

            unit_coordinates[move_to_x][move_to_y][2] -= attack
            text1 = (unit_coordinates[move_to_x][move_to_y][0].title() + " loses " + str(attack) + " hp! " + str(unit_coordinates[move_to_x][move_to_y][2]) + " hp left.")

            if unit_coordinates[move_to_x][move_to_y][2] <= 0:
                unit_coordinates[move_to_x][move_to_y][0], unit_coordinates[move_to_x][move_to_y][1], unit_coordinates[move_to_x][move_to_y][2] = 0, 0, 0

    return unit_coordinates, colour_coordinates, text1

def main(X_LENGTH, Y_LENGTH, move, new, size, tile, border):
    print(X_LENGTH, Y_LENGTH)
    print(size)
    text1 = ""
    mode = "movement"
    start = True

    if size == "small":
        load_unit = "unit_coordinates_small.txt"
        load_unit_new = "unit_coordinates_small_new.txt"
        load_colour = "colour_coordinates_small.txt"
        load_colour_new = "colour_coordinates_small_new.txt"
    
    elif size == "medium":
        load_unit = "unit_coordinates_medium.txt"
        load_unit_new = "unit_coordinates_medium_new.txt"
        load_colour = "colour_coordinates_medium.txt"
        load_colour_new = "colour_coordinates_medium_new.txt"
    
    elif size == "large":
        load_unit = "unit_coordinates_large.txt"
        load_unit_new = "unit_coordinates_large_new.txt"
        load_colour = "colour_coordinates_large.txt"
        load_colour_new = "colour_coordinates_large_new.txt"

    # loads unit graphics
    infantry = pygame.transform.scale((pygame.image.load("infantry.png")), [45, 45])
    tank = pygame.transform.scale((pygame.image.load("tank.png")), [45, 45])
    bomber = pygame.transform.scale((pygame.image.load("bomber.png")), [45, 45])
    fighter = pygame.transform.scale((pygame.image.load("fighter.png")), [45, 45])

    infantry_b = pygame.transform.scale((pygame.image.load("infantry_b.png")), [45, 45])
    tank_b = pygame.transform.scale((pygame.image.load("tank_b.png")), [45, 45])
    bomber_b = pygame.transform.scale((pygame.image.load("bomber_b.png")), [45, 45])
    fighter_b = pygame.transform.scale((pygame.image.load("fighter_b.png")), [45, 45])
    
    infantry_r = pygame.transform.scale((pygame.image.load("infantry_r.png")), [45, 45])
    tank_r = pygame.transform.scale((pygame.image.load("tank_r.png")), [45, 45])
    bomber_r = pygame.transform.scale((pygame.image.load("bomber_r.png")), [45, 45])
    fighter_r = pygame.transform.scale((pygame.image.load("fighter_r.png")), [45, 45])
    
    infantry_g = pygame.transform.scale((pygame.image.load("infantry_g.png")), [45, 45])
    tank_g = pygame.transform.scale((pygame.image.load("tank_g.png")), [45, 45])
    bomber_g = pygame.transform.scale((pygame.image.load("bomber_g.png")), [45, 45])
    fighter_g = pygame.transform.scale((pygame.image.load("fighter_g.png")), [45, 45])
    
    infantry_y = pygame.transform.scale((pygame.image.load("infantry_y.png")), [45, 45])
    tank_y = pygame.transform.scale((pygame.image.load("tank_y.png")), [45, 45])
    bomber_y = pygame.transform.scale((pygame.image.load("bomber_y.png")), [45, 45])
    fighter_y = pygame.transform.scale((pygame.image.load("fighter_y.png")), [45, 45])

    # creates an array called tile, each which have a button assigned to it
    for x in range(5, X_LENGTH*50+5, 50):
        for y in range(5, (Y_LENGTH)*50+5, 50):
            tile[int((x+45)/50)-1][int((y+45)/50)-1] = pygame.Rect(x, y, 45, 45)
    
    for x in range(3, X_LENGTH*50+3, 50):
        for y in range(3, Y_LENGTH*50+3, 50):
            border[int((x+45)/50)][int((y+45)/50)] = pygame.Rect(x, y, 49, 49)

    # next turn button, and buttons for recruiting units
    next_turn = pygame.Rect(X_LENGTH*50+5, 5, 45, 45)
    infantry_box = pygame.Rect(X_LENGTH*50+5, 55, 45, 45)
    tank_box = pygame.Rect(X_LENGTH*50+5, 105, 45, 45)
    bomber_box = pygame.Rect(X_LENGTH*50+5, 155, 45, 45)
    fighter_box = pygame.Rect(X_LENGTH*50+5, 205, 45, 45)
    exit_game = pygame.Rect(X_LENGTH*50+5, 255, 45, 45)

    move = 1

    # the main loop
    while True:
        if new:
            team = 'red'
            text1 = (team.title() + "'s turn!")
            unit_coordinates = reset_unit_coordinates(load_unit_new)
            colour_coordinates = reset_colour_coordinates(load_colour_new)
            colour_coordinates = randomise_coordinates(colour_coordinates, X_LENGTH, Y_LENGTH)
            money = [10, 10, 10, 10]
            new = False
        
        else:
            unit_coordinates = load_unit_coordinates(load_unit)
            colour_coordinates = load_colour_coordinates(load_colour)
            money = load_money()
            team = get_team()
        
        pygame.init()

        if start == True:
            for x in range(X_LENGTH):
                for y in range(Y_LENGTH):
                    if unit_coordinates[x][y][0] == "infantry" and colour_coordinates[x][y][0] == 'red':
                        unit_coordinates[x][y][1] = 2
                    
                    elif unit_coordinates[x][y][0] == "tank" and colour_coordinates[x][y][0] == 'red':
                        unit_coordinates[x][y][1] = 5

                    elif unit_coordinates[x][y][3] == "bomber" and colour_coordinates[x][y][1] == 'red':
                        unit_coordinates[x][y][4] = 5
                    
                    elif unit_coordinates[x][y][3] == "fighter" and colour_coordinates[x][y][1] == 'red':
                        unit_coordinates[x][y][4] = 5
            start = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit

            for x in range(X_LENGTH):
                for y in range(Y_LENGTH):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos

                        if tile[x][y].collidepoint(mouse_pos):
                            print(unit_coordinates[x][y])
                            print(colour_coordinates[x][y])

                            if move == 1 and ((unit_coordinates[x][y][0] != 0 and unit_coordinates[x][y][1] > 0) or (unit_coordinates[x][y][3] != 0 and unit_coordinates[x][y][4] > 0) and mode == "movement"):
                                to_move, move_to = 0, 0
                                to_move = unit_coordinates[x][y]
                                move_colour_1 = colour_coordinates[x][y][0]
                                move_colour_2 = colour_coordinates[x][y][1]
                                text1 = (str(unit_coordinates[x][y][1]) + " ground movement points. " + str(unit_coordinates[x][y][4]) + " aerial movement points.")
                                print(str(unit_coordinates[x][y][1]) + " ground movement points. " + str(unit_coordinates[x][y][4]) + " aerial movement points.")
                                to_move_x = x
                                to_move_y = y
                                move = 2

                            elif move == 2:
                                move_to = unit_coordinates[x][y]
                                move_to_x = x
                                move_to_y = y
                                unit_coordinates, colour_coordinates, text1 = movement(to_move, to_move_x, to_move_y, move_to, move_to_x, move_to_y, unit_coordinates, colour_coordinates, move_colour_1, move_colour_2, text1, team)
                                #text1 = (str(unit_coordinates[x][y][1]) + " ground movement points left. " + str(unit_coordinates[x][y][4]) + " aerial movement points left.")
                                print(str(unit_coordinates[x][y][1]) + " ground movement points left. " + str(unit_coordinates[x][y][4]) + " aerial movement points left.")
                                move = 1

                            elif mode == "place_infantry" and colour_coordinates[x][y][0] == team and unit_coordinates[x][y][0] == 0:

                                if team == "red" and money[0] >= 2:
                                    money[0] -= 2
                                    unit_coordinates[x][y][0], unit_coordinates[x][y][1], unit_coordinates[x][y][2] = "infantry", 0, 10
                                    colour_coordinates[x][y][0] = team

                                elif team == "blue" and money[1] >= 2:
                                    money[1] -= 2
                                    unit_coordinates[x][y][0], unit_coordinates[x][y][1], unit_coordinates[x][y][2] = "infantry", 0, 10
                                    colour_coordinates[x][y][0] = team

                                elif team == "green" and money[2] >= 2:
                                    money[2] -= 2
                                    unit_coordinates[x][y][0], unit_coordinates[x][y][1], unit_coordinates[x][y][2] = "infantry", 0, 10
                                    colour_coordinates[x][y][0] = team

                                elif team == "yellow" and money[3] >= 2:
                                    money[3] -= 2
                                    unit_coordinates[x][y][0], unit_coordinates[x][y][1], unit_coordinates[x][y][2] = "infantry", 0, 10
                                    colour_coordinates[x][y][0] = team

                                mode = "movement"

                            elif mode == "place_tank" and colour_coordinates[x][y][0] == team and unit_coordinates[x][y][0] == 0:

                                if team == "red" and money[0] >= 20:
                                    money[0] -= 20
                                    unit_coordinates[x][y][0], unit_coordinates[x][y][1], unit_coordinates[x][y][2] = 'tank', 0, 10
                                    colour_coordinates[x][y][0] = team

                                elif team == "blue" and money[1] >= 20:
                                    money[1] -= 20
                                    unit_coordinates[x][y][0], unit_coordinates[x][y][1], unit_coordinates[x][y][2] = 'tank', 0, 10
                                    colour_coordinates[x][y][0] = team

                                elif team == "green" and money[2] >= 20:
                                    money[2] -= 20
                                    unit_coordinates[x][y][0], unit_coordinates[x][y][1], unit_coordinates[x][y][2] = 'tank', 0, 10
                                    colour_coordinates[x][y][0] = team

                                elif team == "yellow" and money[3] >= 20:
                                    money[3] -= 20
                                    unit_coordinates[x][y][0], unit_coordinates[x][y][1], unit_coordinates[x][y][2] = 'tank', 0, 10
                                    colour_coordinates[x][y][0] = team

                                mode = "movement"
                            
                            elif mode == "place_bomber" and colour_coordinates[x][y][0] == team and unit_coordinates[x][y][0] == 0:

                                if team == "red" and money[0] >= 30:
                                    money[0] -= 30
                                    unit_coordinates[x][y][3], unit_coordinates[x][y][4], unit_coordinates[x][y][5] = 'bomber', 0, 10
                                    colour_coordinates[x][y][1] = team

                                elif team == "blue" and money[1] >= 30:
                                    money[1] -= 30
                                    unit_coordinates[x][y][3], unit_coordinates[x][y][4], unit_coordinates[x][y][5] = 'bomber', 0, 10
                                    colour_coordinates[x][y][1] = team
                                    
                                elif team == "green" and money[2] >= 30:
                                    money[2] -= 30
                                    unit_coordinates[x][y][3], unit_coordinates[x][y][4], unit_coordinates[x][y][5] = 'bomber', 0, 10
                                    colour_coordinates[x][y][1] = team

                                elif team == "yellow" and money[3] >= 30:
                                    money[3] -= 30
                                    unit_coordinates[x][y][3], unit_coordinates[x][y][4], unit_coordinates[x][y][5] = 'bomber', 0, 10
                                    colour_coordinates[x][y][1] = team

                                mode = "movement"

                            elif mode == "place_fighter" and colour_coordinates[x][y][0] == team and unit_coordinates[x][y][0] == 0:

                                if team == "red" and money[0] >= 20:
                                    money[0] -= 20
                                    unit_coordinates[x][y][3], unit_coordinates[x][y][4], unit_coordinates[x][y][5] = 'fighter', 0, 10
                                    colour_coordinates[x][y][1] = team

                                elif team == "blue" and money[1] >= 20:
                                    money[1] -= 20
                                    unit_coordinates[x][y][3], unit_coordinates[x][y][4], unit_coordinates[x][y][5] = 'fighter', 0, 10
                                    colour_coordinates[x][y][1] = team

                                elif team == "green" and money[2] >= 20:
                                    money[2] -= 20
                                    unit_coordinates[x][y][3], unit_coordinates[x][y][4], unit_coordinates[x][y][5] = 'fighter', 0, 10
                                    colour_coordinates[x][y][1] = team

                                elif team == "yellow" and money[3] >= 20:
                                    money[3] -= 20
                                    unit_coordinates[x][y][3], unit_coordinates[x][y][4], unit_coordinates[x][y][5] = 'fighter', 0, 10
                                    colour_coordinates[x][y][1] = team

                                mode = "movement"

                            else:
                                text1 = ("0 movement points.")

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                # Next turn fuctionality, causes the movement points of the different units to be reset for a new turn
                if next_turn.collidepoint(mouse_pos):
                    text1 = ("Next turn pressed")

                    if team == 'red':
                        team = 'blue'

                    elif team == 'blue':
                        team = 'green'

                    elif team == 'green':
                        team = 'yellow'

                    elif team == 'yellow':
                        team = 'red'
                        addmoney(money, colour_coordinates, X_LENGTH, Y_LENGTH)

                    for x in range(X_LENGTH):
                        for y in range(Y_LENGTH):
                            movedG = False
                            movedA = False

                            if unit_coordinates[x][y][0] == "infantry" and colour_coordinates[x][y][0] == team:
                                unit_coordinates[x][y][1] = 1
                                movedG = True
                            
                            elif unit_coordinates[x][y][0] == "tank" and colour_coordinates[x][y][0] == team:
                                unit_coordinates[x][y][1] = 5
                                movedG = True

                            if unit_coordinates[x][y][3] == "bomber" and colour_coordinates[x][y][1] == team:
                                unit_coordinates[x][y][4] = 5
                                movedA = True
                            
                            elif unit_coordinates[x][y][3] == "fighter" and colour_coordinates[x][y][1] == team:
                                unit_coordinates[x][y][4] = 5
                                movedA = True
                            
                            if movedG != True and movedA != True:
                                # refreshes the so that other team units can't move whilst its not their turn
                                unit_coordinates[x][y][1] = 0
                                unit_coordinates[x][y][4] = 0
                    
                    text1 = (team.title() + "'s turn!")
                
                elif infantry_box.collidepoint(mouse_pos):
                    text1 = ("infantry to place")
                    # sets mode into place infantry mode, which is a new form of selection in which units may be placed onto the map
                    mode = "place_infantry"

                elif tank_box.collidepoint(mouse_pos):
                    text1 = ("tank to place")
                    mode = "place_tank"

                elif bomber_box.collidepoint(mouse_pos):
                    text1 = ("bomber to place")
                    mode = "place_bomber"

                elif fighter_box.collidepoint(mouse_pos):
                    text1 = ("fighter to place")
                    mode = "place_fighter"

                elif exit_game.collidepoint(mouse_pos):
                    menu(X_LENGTH, Y_LENGTH, size)

        # refreshes screen each turn
        screen.fill(WHITE)

        for x in range(X_LENGTH):
            for y in range(Y_LENGTH):
                if colour_coordinates[x][y][0] == "red":
                    pygame.draw.rect(screen, RED, border[x][y])
                
                elif colour_coordinates[x][y][0] == "blue":
                    pygame.draw.rect(screen, BLUE, border[x][y])
                
                elif colour_coordinates[x][y][0] == "green":
                    pygame.draw.rect(screen, PLAYER_GREEN, border[x][y])
                
                elif colour_coordinates[x][y][0] == "yellow":
                    pygame.draw.rect(screen, PLAYER_YELLOW, border[x][y])

                if colour_coordinates[x][y][2] == 'grass':
                    pygame.draw.rect(screen, GREEN, tile[x][y])
                
                elif colour_coordinates[x][y][2] == 'desert':
                    pygame.draw.rect(screen, YELLOW, tile[x][y])
                
                elif colour_coordinates[x][y][2] == 'snow':
                    pygame.draw.rect(screen, GREY, tile[x][y])

                elif colour_coordinates[x][y][2] == 'jungle':
                    pygame.draw.rect(screen, DARK_GREEN, tile[x][y])

                if unit_coordinates[x][y][0] == "infantry" and unit_coordinates[x][y][2] > 0 and colour_coordinates[x][y][0] == 'blue':
                    screen.blit(infantry_b, (((x+1)*50)-45, ((y+1)*50)-45), infantry_b.get_rect())

                elif unit_coordinates[x][y][0] == "tank" and unit_coordinates[x][y][2] > 0 and colour_coordinates[x][y][0] == 'blue':
                    screen.blit(tank_b, (((x+1)*50)-45, ((y+1)*50)-45), tank_b.get_rect())

                elif unit_coordinates[x][y][0] == "infantry" and unit_coordinates[x][y][2] > 0 and colour_coordinates[x][y][0] == 'red':
                    screen.blit(infantry_r, (((x+1)*50)-45, ((y+1)*50)-45), infantry_r.get_rect())

                elif unit_coordinates[x][y][0] == "tank" and unit_coordinates[x][y][2] > 0 and colour_coordinates[x][y][0] == 'red':
                    screen.blit(tank_r, (((x+1)*50)-45, ((y+1)*50)-45), tank_r.get_rect())
                    
                elif unit_coordinates[x][y][0] == "infantry" and unit_coordinates[x][y][2] > 0 and colour_coordinates[x][y][0] == 'green':
                    screen.blit(infantry_g, (((x+1)*50)-45, ((y+1)*50)-45), infantry_g.get_rect())

                elif unit_coordinates[x][y][0] == "tank" and unit_coordinates[x][y][2] > 0 and colour_coordinates[x][y][0] == 'green':
                    screen.blit(tank_g, (((x+1)*50)-45, ((y+1)*50)-45), tank_g.get_rect())
                
                elif unit_coordinates[x][y][0] == "infantry" and unit_coordinates[x][y][2] > 0 and colour_coordinates[x][y][0] == 'yellow':
                    screen.blit(infantry_y, (((x+1)*50)-45, ((y+1)*50)-45), infantry_y.get_rect())

                elif unit_coordinates[x][y][0] == "tank" and unit_coordinates[x][y][2] > 0 and colour_coordinates[x][y][0] == 'yellow':
                    screen.blit(tank_y, (((x+1)*50)-45, ((y+1)*50)-45), tank_y.get_rect())

                # loading flying units on top of ground units

                if unit_coordinates[x][y][3] == "bomber" and unit_coordinates[x][y][5] > 0 and colour_coordinates[x][y][1] == 'blue':
                    screen.blit(bomber_b, (((x+1)*50)-45, ((y+1)*50)-45), bomber_b.get_rect())

                elif unit_coordinates[x][y][3] == "fighter" and unit_coordinates[x][y][5] > 0 and colour_coordinates[x][y][1] == 'blue':
                    screen.blit(fighter_b, (((x+1)*50)-45, ((y+1)*50)-45), fighter_b.get_rect())

                elif unit_coordinates[x][y][3] == "bomber" and unit_coordinates[x][y][5] > 0 and colour_coordinates[x][y][1] == 'red':
                    screen.blit(bomber_r, (((x+1)*50)-45, ((y+1)*50)-45), bomber_r.get_rect())

                elif unit_coordinates[x][y][3] == "fighter" and unit_coordinates[x][y][5] > 0 and colour_coordinates[x][y][1] == 'red':
                    screen.blit(fighter_r, (((x+1)*50)-45, ((y+1)*50)-45), fighter_r.get_rect())
                
                elif unit_coordinates[x][y][3] == "bomber" and unit_coordinates[x][y][5] > 0 and colour_coordinates[x][y][1] == 'green':
                    screen.blit(bomber_g, (((x+1)*50)-45, ((y+1)*50)-45), bomber_g.get_rect())

                elif unit_coordinates[x][y][3] == "fighter" and unit_coordinates[x][y][5] > 0 and colour_coordinates[x][y][1] == 'green':
                    screen.blit(fighter_g, (((x+1)*50)-45, ((y+1)*50)-45), fighter_g.get_rect())

                elif unit_coordinates[x][y][3] == "bomber" and unit_coordinates[x][y][5] > 0 and colour_coordinates[x][y][1] == 'yellow':
                    screen.blit(bomber_y, (((x+1)*50)-45, ((y+1)*50)-45), bomber_y.get_rect())

                elif unit_coordinates[x][y][3] == "fighter" and unit_coordinates[x][y][5] > 0 and colour_coordinates[x][y][1] == 'yellow':
                    screen.blit(fighter_y, (((x+1)*50)-45, ((y+1)*50)-45), fighter_y.get_rect())

                if unit_coordinates[x][y][0] != 0:
                    health_points = box_font.render(str(unit_coordinates[x][y][2]), True, (0, 0, 0))
                    screen.blit(health_points, (((x+1)*50)-45, ((y+1)*50)-45))
                    movement_points = box_font.render(str(unit_coordinates[x][y][1]), True, (0, 0, 0))
                    screen.blit(movement_points, (((x+1)*50)-45, ((y+1)*50)-13))

                if unit_coordinates[x][y][3] != 0:
                    health_points = box_font.render(str(unit_coordinates[x][y][5]), True, (0, 0, 0))
                    screen.blit(health_points, (((x+1)*50)-17, ((y+1)*50)-45))
                    movement_points = box_font.render(str(unit_coordinates[x][y][4]), True, (0, 0, 0))
                    screen.blit(movement_points, (((x+1)*50)-10, ((y+1)*50)-13))


            # screen.blit(infantry, (5, 5), infantry.get_rect())

        pygame.draw.rect(screen, RED, next_turn)

        pygame.draw.rect(screen, WHITE, infantry_box)
        pygame.draw.rect(screen, WHITE, tank_box)
        pygame.draw.rect(screen, WHITE, bomber_box)
        pygame.draw.rect(screen, WHITE, fighter_box)

        pygame.draw.rect(screen, BLUE, exit_game)

        screen.blit(infantry, (X_LENGTH*50+5, 55), infantry.get_rect())
        screen.blit(tank, (X_LENGTH*50+5, 105), tank.get_rect())
        screen.blit(bomber, (X_LENGTH*50+5, 155), bomber.get_rect())
        screen.blit(fighter, (X_LENGTH*50+5, 205), fighter.get_rect())

        # this bit of code always saves the location of the different units and their hp
        with open(load_unit, 'w') as f:
            f.write("[".rstrip('\n'))
            for x in range(X_LENGTH):
                f.write("[".rstrip('\n'))
                for y in range(Y_LENGTH - 1):
                    f.write((str(unit_coordinates[x][y]) + ",").rstrip('\n'))
                f.write((str(unit_coordinates[x][Y_LENGTH-1])).rstrip('\n'))
                f.write("]".rstrip('\n'))
                if x != X_LENGTH - 1:
                    f.write(",".rstrip('\n'))
            f.write("]".rstrip('\n'))
            f.close()

        # this does the same as the above, however now saves for the team colour of the captured tiles
        with open(load_colour, 'w') as f:
            f.write("[".rstrip('\n'))
            for x in range(X_LENGTH):
                f.write("[".rstrip('\n'))
                for y in range(Y_LENGTH - 1):
                    f.write((str(colour_coordinates[x][y]) + ",").rstrip('\n'))
                f.write((str(colour_coordinates[x][Y_LENGTH-1])).rstrip('\n'))
                f.write("]".rstrip('\n'))
                if x != X_LENGTH - 1:
                    f.write(",".rstrip('\n'))
            f.write("]".rstrip('\n'))
            f.close()

        with open('money.txt', 'w') as f:
            f.write("[".rstrip('\n'))
            for i in range(0,4):
                if i != 3:
                    f.write((str(money[i]) + ",").rstrip('\n'))
                else:
                    f.write((str(money[i])).rstrip('\n'))
            f.write("]".rstrip('\n'))
            f.close()
        
        with open('team.txt', 'w') as f:
            f.write("'" + str(team) + "'")
            f.close()

        button_labels(X_LENGTH)
        textbox(text1, Y_LENGTH)
        moneybox(money, X_LENGTH, Y_LENGTH)
        pygame.display.update()
        pygame.time.Clock().tick(FPS)

def menu(X_LENGTH, Y_LENGTH, size):
    print(X_LENGTH, Y_LENGTH)
    # window size depends on size of board
    screen = pygame.display.set_mode((X_LENGTH*50+55, Y_LENGTH*50+55))

    tile = [[None]*X_LENGTH for _ in range(Y_LENGTH)]
    border = [[None]*X_LENGTH for _ in range(Y_LENGTH)]

    # defines the shape, size and posistion of start, load, settings and quit buttons
    start_button = pygame.Rect(20, 120, 100, 20)
    load_button = pygame.Rect(20, 150, 100, 20)
    settings_button = pygame.Rect(20, 180, 100, 20)
    quit_button = pygame.Rect(20, 210, 100, 20)

    # makes the screen white and draws the previous buttons onto the surface of the screen
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREY, start_button)
    pygame.draw.rect(screen, GREY, load_button)
    pygame.draw.rect(screen, GREY, settings_button)
    pygame.draw.rect(screen, GREY, quit_button)

    # loads the text for the different buttons so users know of their effects
    title_text = title.render("Triumph", True, (0, 0, 0))
    new_game_text = font.render("New Game", True, (0, 0, 0))
    load_text = font.render("Load", True, (0, 0, 0))
    settings_text = font.render("Settings", True, (0, 0, 0))
    quit_text = font.render("Quit", True, (0, 0, 0))

    # draws the loaded text onto the surface of the screen so that they are visible for the user
    screen.blit(title_text, (20, 30))
    screen.blit(new_game_text, (20, 125))
    screen.blit(load_text, (20, 155))
    screen.blit(settings_text, (20, 185))
    screen.blit(quit_text, (20, 215))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                # Verifies in the console whether the user has selected the different buttons
                if start_button.collidepoint(mouse_pos):
                    main(X_LENGTH, Y_LENGTH, 1, True, size, tile, border)

                elif load_button.collidepoint(mouse_pos):
                    main(X_LENGTH, Y_LENGTH, 1, False, size, tile, border)

                elif settings_button.collidepoint(mouse_pos):
                    settings()
                    
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit
        
        pygame.display.update()
        pygame.time.Clock().tick(FPS)

def settings():
    # defines the shape, size and posistion of start, load, settings and quit buttons
    small_button = pygame.Rect(20, 120, 100, 20)
    medium_button = pygame.Rect(20, 150, 100, 20)
    large_button = pygame.Rect(20, 180, 100, 20)

    # makes the screen white and draws the previous buttons onto the surface of the screen
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREY, small_button)
    pygame.draw.rect(screen, GREY, medium_button)
    pygame.draw.rect(screen, GREY, large_button)

    # loads the text for the different buttons so users know of their effects
    settings_text = title.render("Settings", True, (0, 0, 0))
    small_text = font.render("Small Map", True, (0, 0, 0))
    medium_text = font.render("Medium Map", True, (0, 0, 0))
    large_text = font.render("Large Map", True, (0, 0, 0))

    # draws the loaded text onto the surface of the screen so that they are visible for the user
    screen.blit(settings_text, (20, 30))
    screen.blit(small_text, (20, 125))
    screen.blit(medium_text, (20, 155))
    screen.blit(large_text, (20, 185))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                # Verifies in the console whether the user has selected the different buttons
                if small_button.collidepoint(mouse_pos):
                    menu(10, 10, "small")

                elif medium_button.collidepoint(mouse_pos):
                    menu(15, 15, "medium")

                elif large_button.collidepoint(mouse_pos):
                    menu(20, 20, "large")
        
        pygame.display.update()
        pygame.time.Clock().tick(FPS)

if __name__ == "__main__": 
    menu(10, 10, "small")