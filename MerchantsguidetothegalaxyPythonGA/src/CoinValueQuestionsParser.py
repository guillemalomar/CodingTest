from MerchantTool.MerchantTool import MerchantTool
import sys
import re

_value_question = re.compile('how much is ([A-Za-z ]+) +?')
_credits_question = re.compile('how many Credits is ([A-Za-z ]+) +?')


# Print method for the first message
def presentation():
    print "-------------------------- Welcome to the Merchants Guide to the Galaxy app --------------------------\n" \
          "The default path to the data file is this one:\n" \
          "        MerchantsguidetothegalaxyPythonGA/data/input.txt\n" \
          "If you would like to use another data file, insert the path to it as a parameter of the application.\n"


# Method used to read the input_data
def process_input(input_path):
    with open(input_path, 'r') as f:
        read_data = f.read()
    return read_data.split(', ')


# Method called to do a 'clear', just for application visualization purposes
def clean_screen():
    print(chr(27) + "[2J")


if __name__ == '__main__':

    clean_screen()
    presentation()

    if len(sys.argv) == 1:
        input_path = 'MerchantsguidetothegalaxyPythonGA/data/input.txt'
    else:
        input_path = sys.argv[1]
    input_data = process_input(input_path)

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
