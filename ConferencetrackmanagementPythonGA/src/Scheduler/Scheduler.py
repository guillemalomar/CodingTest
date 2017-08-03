

# Class that contains all the logic and methods related to reading the
# input data to obtain the times of the talks, and assign the talks to
# the available sessions
class Scheduler:

    def __init__(self):
        pass

    # Method used to obtain the times of the talks from the input_data
    @staticmethod
    def calculate_times(times_input_data):
        schedule_times = []
        for row in times_input_data:
            lines = row.split('\n')
            for line in lines:
                if line.split(' ')[-1][-3:] == 'min':
                    schedule_times.append((line, int(line.split(' ')[-1][:-3])))
                else:
                    schedule_times.append((line, 5))
        return sorted(schedule_times, key=lambda x: x[1], reverse=True)

    # Method that assigns the different talks to the available sessions
    @staticmethod
    def calculate_tracks(tracks_times):
        calculated_track1morning = {}
        track1morning_time = 0
        calculated_track2morning = {}
        track2morning_time = 0
        calculated_track1afternoon = {}
        track1afternoon_time = 0
        calculated_track2afternoon = {}
        track2afternoon_time = 0
        calculated_left_sessions = 0
        for ind, entry in enumerate(tracks_times):
            if ind % 2 == 1:
                if track1afternoon_time + entry[1] == 240:
                    calculated_track1afternoon[track1afternoon_time] = entry
                    track1afternoon_time += entry[1]
                elif track1morning_time + entry[1] == 180:
                    calculated_track1morning[track1morning_time] = entry
                    track1morning_time += entry[1]
                elif track2afternoon_time + entry[1] == 240:
                    calculated_track2afternoon[track2afternoon_time] = entry
                    track2afternoon_time += entry[1]
                elif track2morning_time + entry[1] == 180:
                    calculated_track2morning[track2morning_time] = entry
                    track2morning_time += entry[1]
                elif track2afternoon_time + entry[1] <= 210:
                    calculated_track2afternoon[track2afternoon_time] = entry
                    track2afternoon_time += entry[1]
                elif track2morning_time + entry[1] <= 150:
                    calculated_track2morning[track2morning_time] = entry
                    track2morning_time += entry[1]
                elif track1afternoon_time + entry[1] <= 210:
                    calculated_track1afternoon[track1afternoon_time] = entry
                    track1afternoon_time += entry[1]
                elif track1morning_time + entry[1] <= 150:
                    calculated_track1morning[track1morning_time] = entry
                    track1morning_time += entry[1]
                else:
                    calculated_left_sessions += 1
            else:
                if track1morning_time + entry[1] == 180:
                    calculated_track1morning[track1morning_time] = entry
                    track1morning_time += entry[1]
                elif track1afternoon_time + entry[1] == 240:
                    calculated_track1afternoon[track1afternoon_time] = entry
                    track1afternoon_time += entry[1]
                elif track2morning_time + entry[1] == 180:
                    calculated_track2morning[track2morning_time] = entry
                    track2morning_time += entry[1]
                elif track2afternoon_time + entry[1] == 240:
                    calculated_track2afternoon[track2afternoon_time] = entry
                    track2afternoon_time += entry[1]
                elif track2afternoon_time + entry[1] <= 210:
                    calculated_track2afternoon[track2afternoon_time] = entry
                    track2afternoon_time += entry[1]
                elif track2morning_time + entry[1] <= 150:
                    calculated_track2morning[track2morning_time] = entry
                    track2morning_time += entry[1]
                elif track1afternoon_time + entry[1] <= 210:
                    calculated_track1afternoon[track1afternoon_time] = entry
                    track1afternoon_time += entry[1]
                elif track1morning_time + entry[1] <= 150:
                    calculated_track1morning[track1morning_time] = entry
                    track1morning_time += entry[1]
                else:
                    calculated_left_sessions += 1

        return calculated_track1morning,\
               calculated_track1afternoon,\
               calculated_track2morning, \
               calculated_track2afternoon,\
               calculated_left_sessions
