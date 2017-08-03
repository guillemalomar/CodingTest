import unittest
from Printer.Printer import Printer


class PrinterTests(unittest.TestCase):
    def test_mins_to_hours(self):
        self.assertEquals(Printer.mins_to_hours(60), '01:00AM ')
        self.assertEquals(Printer.mins_to_hours(750), '12:30AM ')
        self.assertEquals(Printer.mins_to_hours(780), '01:00PM ')
        self.assertEquals(Printer.mins_to_hours(810), '01:30PM ')

