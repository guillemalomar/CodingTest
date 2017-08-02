

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


if __name__ == '__main__':
    with open('../data/input.txt', 'r') as f:
        read_data = f.read()
    input_data = read_data.split(', ')
    times = []
    for row in input_data:
        lines = row.split('\n')
        for line in lines:
            if line.split(' ')[-1][-3:] == 'min':
                times.append((line, int(line.split(' ')[-1][:-3])))
            else:
                times.append((line, 5))
    times = sorted(times, key=lambda x: x[1], reverse=True)
    track1morning = {}
    track1morning_time = 0
    track2morning = {}
    track2morning_time = 0
    track1afternoon = {}
    track1afternoon_time = 0
    track2afternoon = {}
    track2afternoon_time = 0
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

    print "Track 1:"
    prev_time = 0
    for ind, entry in enumerate(track1morning.itervalues()):
        time_to_print = mins_to_hours(540 + prev_time)
        time_to_print += entry[0]
        print time_to_print
        prev_time += entry[1]
    print "12:00PM Lunch"
    prev_time = 0
    for ind, entry in enumerate(track1afternoon.itervalues()):
        time_to_print = mins_to_hours(780 + prev_time)
        time_to_print += entry[0]
        print time_to_print
        prev_time += entry[1]
    print "05:00PM Networking Event\n"

    print "Track 2:"
    prev_time = 0
    for ind, entry in enumerate(track2morning.itervalues()):
        time_to_print = mins_to_hours(540 + prev_time)
        time_to_print += entry[0]
        print time_to_print
        prev_time += entry[1]
    print "12:00PM Lunch"
    prev_time = 0
    for ind, entry in enumerate(track2afternoon.itervalues()):
        time_to_print = mins_to_hours(780 + prev_time)
        time_to_print += entry[0]
        print time_to_print
        prev_time += entry[1]
    print "05:00PM Networking Event"