

def process_input(input_path):
    with open(input_path, 'r') as f:
        read_data = f.read()
    return read_data.split(', ')


def calculate_times(input_data):
    times = []
    for row in input_data:
        lines = row.split('\n')
        for line in lines:
            if line.split(' ')[-1][-3:] == 'min':
                times.append((line, int(line.split(' ')[-1][:-3])))
            else:
                times.append((line, 5))
    return sorted(times, key=lambda x: x[1], reverse=True)


def calculate_tracks(times):
    track1morning = {}
    track1morning_time = 0
    track2morning = {}
    track2morning_time = 0
    track1afternoon = {}
    track1afternoon_time = 0
    track2afternoon = {}
    track2afternoon_time = 0
    left_sessions = 0
    for ind, entry in enumerate(times):
        if ind % 2 ==1:
            if track1afternoon_time + entry[1] == 240:
                track1afternoon[track1afternoon_time] = entry
                track1afternoon_time += entry[1]
            elif track1morning_time + entry[1] == 180:
                track1morning[track1morning_time] = entry
                track1morning_time += entry[1]
            elif track2afternoon_time + entry[1] == 240:
                track2afternoon[track2afternoon_time] = entry
                track2afternoon_time += entry[1]
            elif track2morning_time + entry[1] == 180:
                track2morning[track2morning_time] = entry
                track2morning_time += entry[1]
            elif track2afternoon_time + entry[1] <= 210:
                track2afternoon[track2afternoon_time] = entry
                track2afternoon_time += entry[1]
            elif track2morning_time + entry[1] <= 150:
                track2morning[track2morning_time] = entry
                track2morning_time += entry[1]
            elif track1afternoon_time + entry[1] <= 210:
                track1afternoon[track1afternoon_time] = entry
                track1afternoon_time += entry[1]
            elif track1morning_time + entry[1] <= 150:
                track1morning[track1morning_time] = entry
                track1morning_time += entry[1]
            else:
                left_sessions += 1
        else:
            if track1morning_time + entry[1] == 180:
                track1morning[track1morning_time] = entry
                track1morning_time += entry[1]
            elif track1afternoon_time + entry[1] == 240:
                track1afternoon[track1afternoon_time] = entry
                track1afternoon_time += entry[1]
            elif track2morning_time + entry[1] == 180:
                track2morning[track2morning_time] = entry
                track2morning_time += entry[1]
            elif track2afternoon_time + entry[1] == 240:
                track2afternoon[track2afternoon_time] = entry
                track2afternoon_time += entry[1]
            elif track2afternoon_time + entry[1] <= 210:
                track2afternoon[track2afternoon_time] = entry
                track2afternoon_time += entry[1]
            elif track2morning_time + entry[1] <= 150:
                track2morning[track2morning_time] = entry
                track2morning_time += entry[1]
            elif track1afternoon_time + entry[1] <= 210:
                track1afternoon[track1afternoon_time] = entry
                track1afternoon_time += entry[1]
            elif track1morning_time + entry[1] <= 150:
                track1morning[track1morning_time] = entry
                track1morning_time += entry[1]
            else:
                left_sessions += 1
    return track1morning, track1afternoon, track2morning, track2afternoon, left_sessions

def mins_to_hours(mins):
    hours = mins / 60
    minutes = mins % 60
    if hours > 12:
        hours = hours - 12
        sufix = 'PM '
    else:
        sufix = 'AM '
    if hours < 10:
        hours = '0' + str(hours)
    if minutes < 10:
        minutes = '0' + str(minutes)
    return str(hours) + ":" + str(minutes) + sufix


def show_tracks(track1morning_toshow, track1afternoon_toshow, track2morning_toshow, track2afternoon_toshow):
    print "Track 1:"
    show_result(track1morning_toshow, 540)
    print "12:00PM Lunch"
    show_result(track1afternoon_toshow, 780)
    print "05:00PM Networking Event\n"
    print "Track 2:"
    show_result(track2morning_toshow, 540)
    print "12:00PM Lunch"
    show_result(track2afternoon_toshow, 780)
    print "05:00PM Networking Event\n"

def show_result(track, from_time):
    prev_time = 0
    for ind, entry in enumerate(track.itervalues()):
        time_to_print = mins_to_hours(from_time + prev_time)
        time_to_print += entry[0]
        print time_to_print
        prev_time += entry[1]


if __name__ == '__main__':
    input_data = process_input('../data/input.txt')
    times = calculate_times(input_data)
    track1morning, track1afternoon, track2morning, track2afternoon, left_sessions = calculate_tracks(times)
    show_tracks(track1morning, track1afternoon, track2morning, track2afternoon)