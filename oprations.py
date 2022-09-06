import os
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
    print("Enter 'Q' or press Enter to start :\n>>> ", end='')
    choose_opration(['', 'Q', 'q'])
    start_app()


def get_point_info():
    status = True
    while True:
        point_position = input('>>> ').split()
        if not point_position[0].isalpha() and not point_position[1].isalpha():
            for s in """!@#$%^&*()=/*|\\}{]['"`<>?""":
                if s in point_position[0] or s in point_position[1]:
                    status = False
                    print('Invalid input. Try again')
                    break
            else :
                status = True

            if status:
                break
                        
        else :
            print('Invalid input. Try again')

    print('Enter point name (optional) or press Enter to continue:')
    point_name = input('>>> ')     
    return tuple(float(p) for p in point_position)+(point_name, )


def get_points():
    clear_screen()
    print(10*'-','GETTING POINTS', 10*'-')
    
    list_of_points = ()
    for counter in ['first', 'second']:
            print(f'Enter position of {counter} point(x y) :')
            point_info = get_point_info()
            point = objects.Point(x=point_info[0], y=point_info[1], name=point_info[2])
            list_of_points += (point, )
    
    if list_of_points[0] == list_of_points[1]:
        print("WARNING no line exists between same points")
    return list_of_points


def print_points(points):
    for point in points:
        print(point)


def line_length(line):
    print(line.__len__())

def line_gradient(line):
    print(line.get_gradient())

def area_between_line_and_x_axis(line):
    print(line.area_between_line_and_x_axis())

def check_point_in_line(line, points):
    clear_screen()
    print(10*'-','CHECK POINTS IN LINE', 10*'-', sep='')
    print('Given points : ')
    print_points(points)
    print(25*'=')
    print(f'Line Equation : {line.get_equation()}')
    print(25*'-')
    while True:
        print(f'Enter position of point(x y) :')
        point_info = get_point_info()
        point = objects.Point(x=point_info[0], y=point_info[1], name=point_info[2])
        status = line.is_point_on_line(point)
        if status:
            print(f"The line {line} contaions the point {point}")
        else:
            print(f"The point {point} is not on The line {line}")
        print("Enter 'I' to see line info. Press Enter or enter 'A' to test another point")
        opr = choose_opration(['I', 'i', 'A', 'a', ''])
        if opr in ['I', 'i']:
            break
    line_information(line, points)


def quit():
    print('thanks for using this app')


def line_options(line, points):
    print("Enter 'L' to see length of line, 'G' to see gradient of line, 'A' to see area between line and x axis and if you want to check if a special point is on line or not enter 'P' :")
    print("Enter 'N' to check new line, or 'Q' to quit app :")
    while True:
        opt = choose_opration(['L', 'l', 'G', 'g', 'A', 'a', 'P', 'p', 'N', 'n', 'Q', 'q'])

        if opt in ['L', 'l']:
            line_length(line)
        elif opt in ['G', 'g']:
            line_gradient(line)
        elif opt in ['A', 'a']:
            area_between_line_and_x_axis(line)
        elif opt in ['P', 'p']:
            check_point_in_line(line, points)
        elif opt in ['N', 'n']:
            points = get_points()
            line_name = get_line_name()
            line = objects.Line(name = line_name, start_point = points[0], end_point = points[1])
        elif opt in ['Q', 'q']:
            quit()
        else:
            print("SOME THING WENT WRONG")

def get_line_name():
    print('Enter line name (optional) or press Enter to continue:')
    line_name = input('>>> ') 
    return line_name


def line_information(line, points):
    clear_screen()
    print('<',10*'-','LINE INFORMATION', 10*'-','>', sep='')
    print('Given points : ')
    print_points(points)
    print(25*'=')
    print(f'Line Equation : {line.get_equation()}')
    print(25*'-')
    line_options(line, points)

def start_app():
    points = get_points()
    line_name = get_line_name()
    line = objects.Line(name = line_name, start_point = points[0], end_point = points[1])
    line_information(line, points)



    