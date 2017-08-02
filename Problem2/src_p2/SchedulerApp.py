from Scheduler.Scheduler import Scheduler
from Printer.Printer import Printer


def process_input(input_path):
    with open(input_path, 'r') as f:
        read_data = f.read()
    return read_data.split(', ')


if __name__ == '__main__':
    input_data = process_input('../data/input.txt')
    my_scheduler = Scheduler()
    times = my_scheduler.calculate_times(input_data)
    track1morning, track1afternoon, track2morning, track2afternoon, left_sessions = Scheduler.calculate_tracks(times)
    Printer.show_tracks(track1morning, track1afternoon, track2morning, track2afternoon)
