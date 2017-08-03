from Train.Train import Train
import re


_acceptable_path = re.compile('([A-Z]+)')
_acceptable_strip = re.compile('([A-Z]{2})')
_acceptable_value = re.compile('([0-9]{0,2})')


def presentation():
    print "This application has 4 main modes:\n" \
          "1) Calculate distance between 2 given stations\n" \
          "2) Calculate the number of different paths available to go from a station to another, " \
          "with a max nr. of stops\n" \
          "3) The length of the shortest route from a station to another station\n" \
          "4) Calculate the number of different paths from a station to another one in a specified max distance"


def insert_mode():
    correct_mode = False
    chosen_mode = 0
    while not correct_mode:
        chosen_mode = raw_input("Please enter a mode: ")
        if chosen_mode not in ['1', '2', '3', '4']:
            print "Please, specify an available mode"
        else:
            correct_mode = True
    return chosen_mode


def insert_path():
    correct_path = False
    chosen_path = ''
    while not correct_path:
        chosen_path = raw_input("Please enter a path: ")
        m = _acceptable_path.match(chosen_path)
        if m is None:
            print "Please, specify avalid"
        else:
            correct_path = True
    return chosen_path


def insert_strip():
    correct_strip = False
    chosen_strip = ''
    while not correct_strip:
        chosen_strip = raw_input("Please enter a strip: ")
        m = _acceptable_strip.match(chosen_strip)
        if m is None:
            print "Please, specify a XY path between stations"
        else:
            correct_strip = True
    return chosen_strip


def insert_max_stops():
    correct_num_stops = False
    chosen_max_stops = 0
    while not correct_num_stops:
        chosen_max_stops = raw_input("Please enter the max number of stops: ")
        m = _acceptable_value.match(chosen_max_stops)
        if m is None:
            print "Please, specify a correct max number of stops"
        else:
            correct_num_stops = True
    return chosen_max_stops


def specify_stops():
    correct_specified_stops = False
    specified_stops = ''
    while not correct_specified_stops:
        specified_stops = raw_input("Do you want it to be the only possible nr of stops? (Y/N): ")
        if specified_stops != 'Y' and specified_stops != 'N':
            print "Please, specify 'Y'(yes) or 'N'(no)"
        else:
            correct_specified_stops = True
    return specified_stops


def insert_max_dist():
    correct_max_dist = False
    max_dist = 0
    while not correct_max_dist:
        max_dist = raw_input("Please enter the max distance: ")
        m = _acceptable_value.match(max_dist)
        if m is None:
            print "Please, specify a correct maximum distance"
        else:
            correct_max_dist = True
    return max_dist


def process_input(input_path):
    with open(input_path, 'r') as f:
        read_data = f.read()
    input_data = read_data.split(', ')
    train_graph = {}
    for entry in input_data:
        train_graph[entry[0:2]] = int(entry[2:])
    return train_graph


if __name__ == '__main__':
    myTrainInfo = Train()
    myTrainInfo.assign_graph(process_input('TrainsPythonGA/data/input.txt'))

    presentation()

    mode = insert_mode()
    if mode == '1':
        print myTrainInfo.calculate_distance(insert_path())
    elif mode == '2':
        print myTrainInfo.calculate_strips(insert_strip(), int(insert_max_stops()), specify_stops())
    elif mode == '3':
        print myTrainInfo.calculate_shortest_route(insert_strip())
    else:
        print myTrainInfo.routes_in_distance(insert_strip(), int(insert_max_dist()))
