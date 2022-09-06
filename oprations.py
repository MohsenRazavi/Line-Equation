import os
from unicodedata import name
import objects

def clear_screen():
    os.system('cls')


def choose_opration(valid_choices):
    while True:
        print("Choose opration:\n>>> ", end='')
        user_input = input()
        if user_input in valid_choices:
            return user_input
        print("Invalid input. Try again")


def welcome():
    clear_screen()
    print(10*"-", 'Welcome to this line equation app', 10*'-')
    print("\nPress 'H' to see help and list of features or 'S'(Enter) to start")
    opr = choose_opration(['', 'h', 'H', 's', 'S'])
    if opr in ['h', 'H']:
        help()
    else:
        start_app()


def help():
    clear_screen()
    print(10*'-','HELP', 10*'-')
    print("how to use :")
    print('1- give 2 points to the program')
    print('finished !')
    print('you can see all informations about the line which is between these 2 points')
    # method names
    choose_opration(['', 'Q', 'q'])
    start_app()


def get_point_info():
    while True:
        point_position = input().split()
        if point_position[0].isdigit() and point_position[1].isdigit():
            print('Enter point name (optional) or press Enter to continue:\n>>> ', end='')
            point_name = input()
                 
            return tuple(int(p) for p in point_position)+(point_name, )
        else :
            print('Invalid input. Try again')


def get_points():
    list_of_points = ()
    for counter in ['first', 'second']:
            print(f'Enter position of {counter} point(x y) :\n>>> ', end='')
            point_info = get_point_info()
            point = objects.Point(x=point_info[0], y=point_info[1], name=point_info[2])
            list_of_points += (point, )
    return list_of_points



def start_app():
    clear_screen()
    print(10*'-','LINE EQUATION', 10*'-')
    points = get_points()


    