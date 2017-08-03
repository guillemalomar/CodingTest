import re


_assign_sentence = re.compile('([A-Za-z]+) is ([A-Za-z]+)')

def process_input(input_path):
    with open(input_path, 'r') as f:
        read_data = f.read()
    return read_data.split(', ')

if __name__ == '__main__':
    input_data = process_input('../data/input.txt')
    assignings = {}
    for row in input_data:
        lines = row.split('\n')
        for line in lines:
            m = _assign_sentence.match(line)
            if m is None:
                pass
            else:
                key, val = m.groups()
                assignings[key] = val
    a = 0