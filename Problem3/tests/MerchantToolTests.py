import unittest
from src.MerchantTool.MerchantTool import MerchantTool
from CoinValueQuestionsParser import process_input


class MerchantToolTests(unittest.TestCase):
    def test_calculate_assigns(self):
        input_data = process_input('Problem3/tests/test_input.txt')
        my_merchant = MerchantTool()
        my_merchant.calculate_assigns(input_data)
        self.assertEquals(my_merchant.assigns, {'fifty': 'L',
                                                'five': 'V',
                                                'ten': 'X',
                                                'one': 'I'})
        self.assertEquals(my_merchant.complex_assigns, {'ten fifty one one one Gold': '86',
                                                        'ten fifty one one one Silver': '43',
                                                        'ten fifty one one one Iron': '129'})
        self.assertEquals(my_merchant.questions, ['how much is fifty five one one one ?',
                                                  'how many Credits is five one one Silver ?',
                                                  'how many Credits is ten one Gold ?',
                                                  'how many Credits is fifty one Iron ?',
                                                  'how much wood could a woodchuck chuck if a woodchuck could chuck wood ?'])

    def test_calculate_assigns_exc(self):
        input_data = process_input('Problem3/tests/test_input_2.txt')
        my_merchant = MerchantTool()
        raisenError = False
        try:
            my_merchant.calculate_assigns(input_data)
        except SyntaxError:
            raisenError = True
        self.assertEqual(raisenError, True)

    def test_calculate_coin_values(self):
        input_data = process_input('Problem3/tests/test_input.txt')
        my_merchant = MerchantTool()
        my_merchant.calculate_assigns(input_data)
        my_merchant.calculate_coin_values()
        self.assertEquals(my_merchant.assigns['Gold'], 2.0)
        self.assertEquals(my_merchant.assigns['Silver'], 1.0)
        self.assertEquals(my_merchant.assigns['Iron'], 3.0)

    def test_process_value_question(self):
        input_data = process_input('Problem3/tests/test_input.txt')
        my_merchant = MerchantTool()
        my_merchant.calculate_assigns(input_data)
        my_merchant.calculate_coin_values()
        self.assertEquals(my_merchant.process_value_question(['one', 'five']), 4)
        self.assertEquals(my_merchant.process_value_question(['fifty', 'five']), 55)
        self.assertEquals(my_merchant.process_value_question(['fifty', 'ten', 'five', 'one', 'one']), 67)

    def test_process_credits_question(self):
        input_data = process_input('Problem3/tests/test_input.txt')
        my_merchant = MerchantTool()
        my_merchant.calculate_assigns(input_data)
        my_merchant.calculate_coin_values()
        self.assertEquals(my_merchant.process_credits_question(['one', 'five', 'Silver']), 4.0)
        self.assertEquals(my_merchant.process_credits_question(['fifty', 'five', 'Iron']), 165.0)
        self.assertEquals(my_merchant.process_credits_question(['fifty', 'ten', 'five', 'one', 'one', 'Gold']), 134.0)
