# Components of the Machine
from util import boundary_check, sign_op, reverse_sign_op

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

    def lsl(acc_value, value):
        if int(value, 16) < 1:
            return acc_value
        
        acc_value = sign_op(acc_value)
        result = ""

        sign_bit = acc_value[0]
        acc_value = acc_value[1:]

        result = ""
        for i in range(int(value, 16)):
            acc_value = acc_value[1:] + '0'
        
        result = sign_bit + acc_value
        result = reverse_sign_op(result)
        return result

    def lsr(acc_value, value):   
        if int(value, 16) < 1:
            return acc_value
        
        acc_value = sign_op(acc_value)
        result = ""

        sign_bit = acc_value[0]
        acc_value = acc_value[1:]

        result = ""
        for i in range(int(value, 16)):
            acc_value = '0' + acc_value[:7]
        
        result = sign_bit + acc_value
        result = reverse_sign_op(result)
        return result

    def xor(acc_value, ram_value):
        acc_value = sign_op(acc_value)
        ram_value = sign_op(ram_value)
        
        result = ""
        for i in range(8):
            if acc_value[i] == ram_value[i]:
                result += '0'
            else:
                result += '1'

        result = reverse_sign_op(result)
        return result

    def not_(acc_value, value):
        acc_value = sign_op(acc_value)
        result = ""
        for i in range(8):
            result = (result + '1') if acc_value[i] == '0' else (result + '0')

        result = reverse_sign_op(result)
        return result

    def and_(acc_value, ram_value):
        acc_value = sign_op(acc_value)
        ram_value = sign_op(ram_value)
        
        # AND ops
        result = ""
        for i in range(8):
            if acc_value[i] == '1' and ram_value[i] == '1':
                result += '1'
            else:
                result += '0'

        result = reverse_sign_op(result)
        return result

    def or_(acc_value, ram_value):
        acc_value = sign_op(acc_value)
        ram_value = sign_op(ram_value)
        
        # OR ops
        result = ""
        for i in range(8):
            if acc_value[i] == '1' or ram_value[i] == '1':
                result += '1'
            else:
                result += '0'

        result = reverse_sign_op(result)
        return result

class RAM:
    class MemoryCell:
        def __init__(self, address, value='00000000'):
            self.address = address
            self.value = value

    def __init__(self, amount=256):
        self.amount = amount
        self.registers = [self.MemoryCell(hex(i)) for i in range(amount)]

    def write(self, address, value):
        address = int(('0b' + address), 2)
        self.registers[address].value = value

    def read(self, address):
        address = int(('0b' + address), 2)
        return self.registers[address].value

    def display(self, display_as_hex=False):
        col_amount = 16 if display_as_hex else 8
        dash_amount = (col_amount * 13 - 1) if display_as_hex else (col_amount * 17 - 1)
        print('\n', '-' * dash_amount, sep='')
        for i in range(0, self.amount, col_amount):
            for j in range(0, col_amount):
                if display_as_hex:
                    ram_address = self.registers[i+j].address
                    ram_value = hex(int(self.registers[i+j].value, 2))
                else:
                    ram_address = self.registers[i+j].address
                    ram_value = self.registers[i+j].value
                print('{:4s}: {:4s}'.format(ram_address, ram_value), sep='', end=' | ')
            print('\n', '-' * dash_amount, sep='')
            

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
    def __init__(self, value='00000000'):
        self.value = value

    def get_hex(self):
        return reverse_sign_op(self.value)

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