# Components of the Machine
from util import boundary_check, sign_op, reverse_sign_op, summation, extraction
from colorama import Fore, Style, Back

UNSIGNED_MAX_LEN = 7
SIGNED_MAX_LEN = 1 + UNSIGNED_MAX_LEN

class ALU:
    def add(acc_value, ram_value):
        result = ''
        if acc_value[0] == '1' and ram_value[0] == '1':
            result = summation(acc_value[1:], ram_value[1:])
            result = '1' + result

        if acc_value[0] == '0' and ram_value[0] == '0':
            result = summation(acc_value[1:], ram_value[1:])
            result = '0' + result

        if acc_value[0] == '1' and ram_value[0] == '0':
            if int(acc_value[1:], 2) > int(ram_value[1:], 2):
                result = extraction(acc_value[1:], ram_value[1:])
                result = '1' + result

            else:
                result = extraction(ram_value[1:], acc_value[1:])
                result = '0' + result
                
        if acc_value[0] == '0' and ram_value[0] == '1':
            if int(acc_value[1:], 2) >= int(ram_value[1:], 2):
                result = extraction(acc_value[1:], ram_value[1:])
                result = '0' + result

            else:
                result = extraction(ram_value[1:], acc_value[1:])
                result = '1' + result

        return result

    def sub(acc_value, ram_value):
        result =  ''
        if acc_value[0] == '1' and ram_value[0] == '1':
            if int(acc_value[1:], 2) > int(ram_value[1:], 2):
                result = extraction(acc_value[1:], ram_value[1:])
                result = '1' + result

            else:
                result = extraction(ram_value[1:], acc_value[1:])
                result = '0' + result

        if acc_value[0] == '0' and ram_value[0] == '0':
            if int(acc_value[1:], 2) >= int(ram_value[1:], 2):
                result = extraction(acc_value[1:], ram_value[1:])
                result = '0' + result

            else:
                result = extraction(ram_value[1:], acc_value[1:])
                result = '1' + result

        if acc_value[0] == '1' and ram_value[0] == '0':
            result = summation(acc_value[1:], ram_value[1:])
            result = '1' + result

        if acc_value[0] == '0' and ram_value[0] == '1':
            result = summation(acc_value[1:], ram_value[1:])
            result = '0' + result

        return result

    def mul(acc_value, ram_value):
        sign = str((int(acc_value[0], 2) + int(ram_value[0], 2)) % 2)
        acc_value = acc_value[1:]
        ram_value = ram_value[1:]

        ram_value = int(reverse_sign_op(ram_value), 16)
        if ram_value == 0:
            return '00000000'
        
        if ram_value == 1:
            return acc_value

        temp = ALU.summation(acc_value, acc_value)
        for i in range(ram_value - 2): 
            temp = summation(temp, acc_value)

        result = sign + temp
        
        return result

    def div(acc_value, ram_value):
        sign = str((int(acc_value[0], 2) + int(ram_value[0], 2)) % 2)
        acc_value = acc_value[1:]
        ram_value = ram_value[1:]

        acc_value = int(reverse_sign_op(acc_value), 16)
        ram_value = int(reverse_sign_op(ram_value), 16)

        if ram_value == 0:
            return '00000000'

        if acc_value < ram_value:
            return '00000000'
            
        result = sign + str(sign_op(hex(acc_value // ram_value)))[1:]
        return result

    def neg(acc_value):
        result = '1' if acc_value[0] == '0' else '0'
        result += acc_value[1:]
        return result

    def lsl(acc_value, value):
        if value[0] == '1' or int(value[1:], 2) < 1:
            return acc_value

        sign_bit = acc_value[0]
        acc_value = acc_value[1:]

        result = ""
        for i in range(int(value, 2)):
            acc_value = acc_value[1:] + '0'
        
        result = sign_bit + acc_value
        return result

    def lsr(acc_value, value):   
        if value[0] == '1' or int(value[1:], 2) < 1:
            return acc_value

        sign_bit = acc_value[0]
        acc_value = acc_value[1:]

        result = ""
        for i in range(int(value, 2)):
            acc_value = '0' + acc_value[:7]
        
        result = sign_bit + acc_value
        return result

    def xor(acc_value, ram_value):
        result = ""
        for i in range(8):
            if acc_value[i] == ram_value[i]:
                result += '0'
            else:
                result += '1'
        return result

    def not_(acc_value, value):
        result = ""
        for i in range(SIGNED_MAX_LEN):
            result = (result + '1') if acc_value[i] == '0' else (result + '0')
        return result

    def and_(acc_value, ram_value):
        result = ""
        for i in range(8):
            if acc_value[i] == '1' and ram_value[i] == '1':
                result += '1'
            else:
                result += '0'
        return result

    def or_(acc_value, ram_value):    
        result = ""
        for i in range(8):
            if acc_value[i] == '1' or ram_value[i] == '1':
                result += '1'
            else:
                result += '0'
        return result

    

class RAM:
    class MemoryCell:
        def __init__(self, address, value='00000000'):
            self.address = address
            self.value = value

        def __str__(self):
            return '{}:{}'.format(self.address, reverse_sign_op(self.value))

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

        HORIZONTAL_CHAR = '=' # old
        VERTICAL_CHAR = ' ' + '|' + ' ' # old
        #HORIZONTAL_CHAR = '█'
        #VERTICAL_CHAR = ' ' + '█' + ' '

        HORIZONTAL_CHAR_START = HORIZONTAL_CHAR * 2
        VERTICAL_CHAR_START = VERTICAL_CHAR[1:]

        col_amount = 16 if display_as_hex else 8
        dash_amount = (col_amount * 13 - 1) if display_as_hex else (col_amount * 17 - 1)
        print('\n' + HORIZONTAL_CHAR_START, HORIZONTAL_CHAR * dash_amount, sep='')
        for i in range(0, self.amount, col_amount):
            print(VERTICAL_CHAR_START, sep='', end='')
            for j in range(0, col_amount):
                ram_address = 'x' + self.registers[i+j].address[2:].upper()
                if display_as_hex:
                    ram_value = reverse_sign_op(self.registers[i+j].value)
                    if ram_value[0] == '-':
                        ram_value = '-' + ram_value[2:]
                    else:
                        ram_value = ram_value[1:]
                else:
                    ram_value = self.registers[i+j].value
                if self.registers[i+j].value != '00000000':
                    print(Fore.GREEN, end='')
                    #print(Back.LIGHTBLACK_EX, end='')
                print('{:4s}: {:4s}'.format(ram_address, ram_value), sep='', end='')
                print(Style.RESET_ALL, end='')
                print(VERTICAL_CHAR, sep='', end='')
            print('\n' + HORIZONTAL_CHAR_START, HORIZONTAL_CHAR * dash_amount, sep='')
            
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

    def brz(self, acc_value, value):
        if acc_value == '00000000' or acc_value == '10000000':
            self.value += int(reverse_sign_op(value), 16) - 1

    def brn(self, acc_value, value):
        if acc_value[0] == '1':
            self.value += int(reverse_sign_op(value), 16) - 1
    
    def increment(self):
        self.value += 1
        
    def get(self):
        return self.value
