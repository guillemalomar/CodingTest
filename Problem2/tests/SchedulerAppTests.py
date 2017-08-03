import unittest
import SchedulerApp


class SchedulerAppTests(unittest.TestCase):
    def test_process_input(self):
        input_data = SchedulerApp.process_input('Problem2/tests/test_input.txt')
        self.assertTrue(type(input_data), list)
        self.assertEquals(len(input_data), 1)
