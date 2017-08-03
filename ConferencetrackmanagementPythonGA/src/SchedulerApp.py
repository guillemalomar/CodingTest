from Scheduler.Scheduler import Scheduler
from Printer.Printer import Printer
import sys


# Print method for the first message
def presentation():
    print "-------------------------- Welcome to the Conference Track Management app --------------------------\n" \
          "The default path to the data file is this one:\n" \
          "        ConferencetrackmanagementPythonGA/data/input.txt\n" \
          "If you would like to use another data file, insert the path to it as a parameter of the application.\n"


# Method used to read the input_data
def process_input(input_path_var):
    with open(input_path_var, 'r') as f:
        read_data = f.read()
    return read_data.split(', ')


# Method called to do a 'clear', just for application visualization purposes
def clean_screen():
    print(chr(27) + "[2J")


if __name__ == '__main__':

    clean_screen()
    presentation()

    if len(sys.argv) == 1:
        input_path = 'ConferencetrackmanagementPythonGA/data/input.txt'
    else:
        input_path = sys.argv[1]

    input_data = process_input(input_path)
    my_scheduler = Scheduler()
    times = my_scheduler.calculate_times(input_data)
    track1morning, track1afternoon, track2morning, track2afternoon, left_sessions = Scheduler.calculate_tracks(times)
    Printer.show_tracks(track1morning, track1afternoon, track2morning, track2afternoon)
