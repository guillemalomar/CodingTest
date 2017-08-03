import re


class MerchantTool:

    conversions = {'X': 10, 'I': 1, 'V': 5, 'L': 50}
    assigns = {}
    complex_assigns = {}
    materials = []
    questions = []

    _assign_sentence = re.compile('([A-Za-z ]+) is ([A-Za-z]+)$')
    _assign_sentence_2 = re.compile('([A-Za-z ]+) is ([0-9]+) Credits$')

    def __init__(self):
        pass

    @staticmethod
    def process_value_question(coins):
        initial = True
        total_val = 0
        prev_val = None
        for coin in coins:
            value = MerchantTool.conversions[MerchantTool.assigns[coin]]
            if not initial:
                if value > prev_val:
                    total_val = value - total_val
                else:
                    total_val += value
            else:
                total_val = value
            initial = False
            prev_val = value
        return total_val

    @staticmethod
    def process_credits_question(coins):
        coins_to_process = []
        coin_material = None
        for coin in coins:
            if coin not in MerchantTool.materials:
                coins_to_process.append(coin)
            else:
                coin_material = coin

        value = MerchantTool.process_value_question(coins_to_process)
        total_value = value * MerchantTool.assigns[coin_material]
        return total_value

    @staticmethod
    def calculate_assigns(input_data):
        for row in input_data:
            lines = row.split('\n')
            for line in lines:
                m = MerchantTool._assign_sentence.match(line)
                if m is not None:
                    key, val = m.groups()
                    MerchantTool.assigns[key] = val
                else:
                    n = MerchantTool._assign_sentence_2.match(line)
                    if n is not None:
                        key, val = n.groups()
                        MerchantTool.materials.append(key.split(' ')[-1])
                        MerchantTool.complex_assigns[key] = val
                    else:
                        MerchantTool.questions.append(line)

    @staticmethod
    def calculate_coin_values():
        for key_assign, val_assign in MerchantTool.complex_assigns.iteritems():
            coin = key_assign.split(' ')[-1]
            quantity = key_assign.split(' ')[0: -1]
            total_quantity = MerchantTool.process_value_question(quantity)
            MerchantTool.assigns[coin] = float(val_assign) / float(total_quantity)
