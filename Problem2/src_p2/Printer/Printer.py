

class Printer:

    def __init__(self):
        pass

    @staticmethod
    def mins_to_hours(mins):
        hours = mins / 60
        minutes = mins % 60
        if hours > 12:
            hours -= 12
            sufix = 'PM '
        else:
            sufix = 'AM '
        if hours < 10:
            hours = '0' + str(hours)
        if minutes < 10:
            minutes = '0' + str(minutes)
        return str(hours) + ":" + str(minutes) + sufix

    @staticmethod
    def show_tracks(track1morning_toshow, track1afternoon_toshow, track2morning_toshow, track2afternoon_toshow):
        print "Track 1:"
        Printer.show_result(track1morning_toshow, 540)
        print "12:00PM Lunch"
        Printer.show_result(track1afternoon_toshow, 780)
        print "05:00PM Networking Event\n"
        print "Track 2:"
        Printer.show_result(track2morning_toshow, 540)
        print "12:00PM Lunch"
        Printer.show_result(track2afternoon_toshow, 780)
        print "05:00PM Networking Event\n"

    @staticmethod
    def show_result(track, from_time):
        prev_time = 0
        for ind, entry in enumerate(track.itervalues()):
            time_to_print = Printer.mins_to_hours(from_time + prev_time)
            time_to_print += entry[0]
            print time_to_print
            prev_time += entry[1]