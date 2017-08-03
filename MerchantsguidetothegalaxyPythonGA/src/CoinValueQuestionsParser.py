from MerchantTool.MerchantTool import MerchantTool
import re

_value_question = re.compile('how much is ([A-Za-z ]+) +?')
_credits_question = re.compile('how many Credits is ([A-Za-z ]+) +?')


def process_input(input_path):
    with open(input_path, 'r') as f:
        read_data = f.read()
    return read_data.split(', ')


if __name__ == '__main__':

    input_data = process_input('MerchantsguidetothegalaxyPythonGA/data/input.txt')

    my_merchant = MerchantTool()
    my_merchant.calculate_assigns(input_data)
    my_merchant.calculate_coin_values()

    for line in my_merchant.questions:
        m = _value_question.match(line)
        if m is not None:
            coins = m.groups()[0].split(' ')
            print ' '.join(coins) + " is " + str(MerchantTool.process_value_question(coins))
        else:
            n = _credits_question.match(line)
            if n is not None:
                coins = n.groups()[0].split(' ')
                print ' '.join(coins) + " is " + str(int(MerchantTool.process_credits_question(coins))) + ' Credits'
            else:
                print "I have no idea what you are talking about"
