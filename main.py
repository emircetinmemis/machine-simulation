# class named accumulator
class Accumulator:
    def __init__(self, value=0):
        self.value = value

class Register:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Memory:
    def __init__(self, value=0):
        self.value = value

class CPU:
    def __init__(self, registers):
        self.registers = registers

def main():
    acc = Accumulator(value=0)

    opcode = {
        '0000': 'BRZ',
        '0001': 'BRN',
        '0010': 'LDI',
        '0011': 'LDM',
        '0100': 'STR',
        '0101': 'ADD',
        '0110': 'SUB',
        '0111': 'MUL',
        '1000': 'DIV',
        '1001': 'NEG',
        '1010': 'LSL',
        '1011': 'LSR',
        '1100': 'XOR',
        '1101': 'NOT',
        '1110': 'AND',
        '1111': 'ORR'
    }

    amount = {
        'BRZ': 1,
        'BRN': 1,
        'LDI': 1,
        'LDM': 1,
        'STR': 1,
        'ADD': 1,
        'SUB': 1,
        'MUL': 1,
        'DIV': 1,
        'NEG': 1,
        'LSL': 1,
        'LSR': 1,
        'XOR': 1,
        'NOT': 1,
        'AND': 1,
        'ORR': 1
    }

    commands = list()
    with open('data.txt', 'r') as f:
        for line in f:
            # Remove leading and trailing whitespace
            command = line.strip()
            # Remove the comments
            command = command[:command.find('#')]
            # Turn it into a list
            command = command.split()

            if command != []:
                commands.append(command)

    for c in commands:
        print(c)


# check if __name__ is main and run the main function
if __name__ == "__main__":
    main()