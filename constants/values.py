
UNSIGNED_MAX_LEN = 7
SIGNED_MAX_LEN = 1 + UNSIGNED_MAX_LEN

opcode = {
    'BRZ': '0x0',
    'BRN': '0x1',
    'LDI': '0x2',
    'LDM': '0x3',
    'STR': '0x4',
    'ADD': '0x5',
    'SUB': '0x6',
    'MUL': '0x7',
    'DIV': '0x8',
    'NEG': '0x9',
    'LSL': '0xa',
    'LSR': '0xb',
    'XOR': '0xc',
    'NOT': '0xd',
    'AND': '0xe',
    'ORR': '0xf'
}

menomic = {
    '0x0': 'BRZ',
    '0x1': 'BRN',
    '0x2': 'LDI',
    '0x3': 'LDM',
    '0x4': 'STR',
    '0x5': 'ADD',
    '0x6': 'SUB',
    '0x7': 'MUL',
    '0x8': 'DIV',
    '0x9': 'NEG',
    '0xa': 'LSL',
    '0xb': 'LSR',
    '0xc': 'XOR',
    '0xd': 'NOT',
    '0xe': 'AND',
    '0xf': 'ORR'
}

hextobin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111'
}