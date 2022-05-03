from util import opcode, hextobin

# Parts of the machine
#   Memory ->Data Memory, Instruction Memory
#   Register -> Accumulator, Program Counter(maybe list of registers)
#   ALU -> Add, Subtract, Multiply, Divide, Negate, Shift Left, Shift Right, XOR, Not, And, Or
#   Control Circuit
#   
#   INC(?) & Control Word(?=control signals)
#
#   Input Output Components!!!!!!!

class Clock:
    def __init__(self):
        self.time = 0
        self.clock_frequency = 1
        self.clock_period = 1 / self.clock_frequency
        self.time_step = 0.1
        self.time_step_count = 0

    def tick(self):
        self.time += self.time_step
        self.time_step_count += 1
        if self.time_step_count >= self.clock_period:
            self.time_step_count = 0
            return True
        else:
            return False

    def getTime(self):
        return self.time

# Cache may not be valid, only memory and one register might be the valid setup
class Cache:
    class Register:
        def __init__(self, address, value=0):
            self.address = address
            self.value = value

    def __init__(self, amount=8):
        self.amount = amount
        self.registers = [self.Register(i, 0) for i in range(amount)]
        self.register = self.Register(0, 1)

    def display(self):
        for i in range(self.amount):
            print(self.registers[i].address, self.registers[i].value)

class Memory:
    def __init__(self, value=0):
        self.value = value

class CPU:
    def __init__(self, registers):
        self.registers = registers

class ALU:
    def __init__(self, value):
        self.value = value

def main():

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

    instructions = list()

    instructions.append(opcode[commands[2][0]])

    print(instructions)

    test = Cache()
    test.display()


    #accumulator = Register(0)
    #program_counter = Register() # first address location of instruction memory 

    while True:
        stopSimulation = input('Press \'q\' to exit or press \'Enter\' to cycle once.\n')
        if stopSimulation == 'q' or stopSimulation == 'Q':
            print('Simulation stopped.')
            break

        
        



# check if __name__ is main and run the main function
if __name__ == "__main__":
    main()