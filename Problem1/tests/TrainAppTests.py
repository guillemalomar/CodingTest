import unittest
from TrainApp import *
from Train import Train


class TrainTests(unittest.TestCase):
    def test_1(self):
        myTrainInfo = Train()
        myTrainInfo.assign_graph(process_input('../data/input.txt'))
        self.assertEquals(myTrainInfo.calculate_distance('ABC'), 9)

    def test_2(self):
        myTrainInfo = Train()
        myTrainInfo.assign_graph(process_input('../data/input.txt'))
        self.assertEquals(myTrainInfo.calculate_distance('AD'), 5)

    def test_3(self):
        myTrainInfo = Train()
        myTrainInfo.assign_graph(process_input('../data/input.txt'))
        self.assertEquals(myTrainInfo.calculate_distance('ADC'), 13)

    def test_4(self):
        myTrainInfo = Train()
        myTrainInfo.assign_graph(process_input('../data/input.txt'))
        self.assertEquals(myTrainInfo.calculate_distance('AEBCD'), 22)

    def test_5(self):
        myTrainInfo = Train()
        myTrainInfo.assign_graph(process_input('../data/input.txt'))
        self.assertEquals(myTrainInfo.calculate_distance('AED'), 'NO SUCH ROUTE')

    def test_6(self):
        myTrainInfo = Train()
        myTrainInfo.assign_graph(process_input('../data/input.txt'))
        self.assertEquals(myTrainInfo.calculate_strips('CC', 3, 'N'), 2)

    def test_7(self):
        myTrainInfo = Train()
        myTrainInfo.assign_graph(process_input('../data/input.txt'))
        self.assertEquals(myTrainInfo.calculate_strips('AC', 4, 'Y'), 3)

    def test_8(self):
        myTrainInfo = Train()
        myTrainInfo.assign_graph(process_input('../data/input.txt'))
        self.assertEquals(myTrainInfo.calculate_shortest_route('AC'), 9)

    def test_9(self):
        myTrainInfo = Train()
        myTrainInfo.assign_graph(process_input('../data/input.txt'))
        self.assertEquals(myTrainInfo.calculate_shortest_route('BB'), 9)

    def test_10(self):
        myTrainInfo = Train()
        myTrainInfo.assign_graph(process_input('../data/input.txt'))
        self.assertEquals(myTrainInfo.routes_in_distance('CC', 30), 7)
