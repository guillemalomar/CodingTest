import unittest
import CoinValueQuestionsParser


class ParserTests(unittest.TestCase):
    def test_process_input(self):
        input_data = CoinValueQuestionsParser.process_input('test_input.txt')
        self.assertTrue(type(input_data), list)
        self.assertEquals(len(input_data), 1)