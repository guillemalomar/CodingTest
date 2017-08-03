import unittest
import SchedulerApp
from Scheduler.Scheduler import Scheduler


class SchedulerTests(unittest.TestCase):
    def test_calculate_times(self):
        input_data = SchedulerApp.process_input('Problem2/tests/test_input.txt')
        my_scheduler = Scheduler()
        self.assertEquals(my_scheduler.calculate_times(input_data), [('talk2 60min', 60),
                                                                     ('talk3 45min', 45),
                                                                     ('talk5 30min', 30),
                                                                     ('talk1 25min', 25),
                                                                     ('talk4 lightning', 5)])

    def test_calculate_tracks(self):
        input_data = SchedulerApp.process_input('Problem2/tests/test_input2.txt')
        my_scheduler = Scheduler()
        times = my_scheduler.calculate_times(input_data)
        self.assertEquals(my_scheduler.calculate_tracks(times), ({0: ('talk12 60min', 60),
                                                                  120: ('talk14 60min', 60),
                                                                  60: ('talk13 60min', 60)},
                                                                 {0: ('talk8 60min', 60),
                                                                  120: ('talk10 60min', 60),
                                                                  180: ('talk11 60min', 60),
                                                                  60: ('talk9 60min', 60)},
                                                                 {0: ('talk5 60min', 60),
                                                                  120: ('talk7 60min', 60),
                                                                  60: ('talk6 60min', 60)},
                                                                 {0: ('talk1 60min', 60),
                                                                  120: ('talk3 60min', 60),
                                                                  180: ('talk4 60min', 60),
                                                                  60: ('talk2 60min', 60)},
                                                                 0))
        input_data = SchedulerApp.process_input('Problem2/tests/test_input3.txt')
        my_scheduler = Scheduler()
        times = my_scheduler.calculate_times(input_data)
        self.assertEquals(my_scheduler.calculate_tracks(times), ({0: ('talk12 60min', 60),
                                                                  120: ('talk14 60min', 60),
                                                                  60: ('talk13 60min', 60)},
                                                                 {0: ('talk8 60min', 60),
                                                                  120: ('talk10 60min', 60),
                                                                  180: ('talk11 60min', 60),
                                                                  60: ('talk9 60min', 60)},
                                                                 {0: ('talk5 60min', 60),
                                                                  120: ('talk7 60min', 60),
                                                                  60: ('talk6 60min', 60)},
                                                                 {0: ('talk1 60min', 60),
                                                                  120: ('talk3 60min', 60),
                                                                  180: ('talk4 60min', 60),
                                                                  60: ('talk2 60min', 60)},
                                                                 1))
