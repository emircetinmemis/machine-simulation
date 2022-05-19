# Components of the Machine
from util import boundary_check

class ALU:
    def add(acc_value, ram_value):
        result =  int(acc_value, 16) + int(ram_value, 16)
        return boundary_check(result)

    def sub(acc_value, ram_value):
        result =  int(acc_value, 16) - int(ram_value, 16)
        return boundary_check(result)

    def mul(acc_value, ram_value):
        result =  int(acc_value, 16) * int(ram_value, 16)
        return boundary_check(result)

    def div(acc_value, ram_value):
        result =  int(acc_value, 16) // int(ram_value, 16)
        return boundary_check(result)

    def neg(acc_value):
        result = -acc_value
        return boundary_check(result)

    def lsl(acc_value, ram_value):
        return acc_value << ram_value

    def lsr(acc_value, ram_value):   
        return acc_value >> ram_value

    def xor(acc_value, ram_value):
        return acc_value ^ ram_value

    def not_(acc_value):
        return ~acc_value

    def and_(acc_value, ram_value):
        return acc_value & ram_value

    def or_(acc_value, ram_value):
        return acc_value | ram_value

class RAM:
    class MemoryCell:
        def __init__(self, address, value=hex(0)):
            self.address = address
            self.value = value

    def __init__(self, amount=256):
        self.amount = amount
        self.registers = [self.MemoryCell(hex(i)) for i in range(amount)]

    def write(self, address, value):
        self.registers[int(address, 16)].value = value

    def read(self, address):
        return self.registers[int(address, 16)].value

    def display(self):
        col_amount = 16
        print('\n', '-' * (col_amount * 13 - 1), sep='')
        for i in range(0, self.amount, col_amount):
            for j in range(0, col_amount):
                ram_address = self.registers[i+j].address
                ram_value = self.registers[i+j].value
                print('{:4s}: {:4s}'.format(ram_address, ram_value), sep='', end=' | ')
            print('\n', '-' * (col_amount * 13 - 1), sep='')
            

class InstructionMemory:
    class MemoryCell:
        def __init__(self, address, instruction, value):
            self.address = address
            self.instruction = instruction 
            self.value = value

    def __init__(self, instructions):
        self.amount = len(instructions)
        self.registers = [self.MemoryCell(i, instructions[i][0], instructions[i][1]) for i in range(self.amount)]

    def read(self, address):
        return self.registers[address].instruction, self.registers[address].value

    def display(self):
        for i in range(self.amount):
            print(self.registers[i])

class Accumulator:
    def __init__(self, value=0):
        self.value = value

    def get(self):
        return self.value

    def set(self, value):
        self.value = value

class ProgramCounter:
    def __init__(self, value=0):
        self.value = value

    def get(self):
        return self.value

    def modify(self, value):
        self.value += value