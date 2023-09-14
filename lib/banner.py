# !/usr/bin/python3
# Banner
import os

def banner():
     os.system('clear')
     print('<[X] Binary Calculator [X]>')
     print('1. DecimalTools')
     print('2. BinaryTools')
     print('3. HexaTools')
     print('4. OctalTools')
     print('5. Exit')
     print('')


def decimalBanner():
     print('<[1] Decimal Tools [1]>')
     print('1. Decimal To Binary')
     print('2. Decimal To Hexa')
     print('3. Decimal To Octal')
     print('4. All')
     print('5. Back\n')
     d_input = int(input('[+][choose]> '))
     return d_input


def binaryBanner():
     print('<[2] Binary Tools [2]>')
     print('1. Binary To Decimal')
     print('2. Binary To Hexa')
     print('3. Binary To Octal')
     print('4. All')
     print('5. Back\n')
     b_input = int(input('[+][choose]> '))
     return b_input


def hexaBanner():
     print('<[3] Hexa Tools [3]>')
     print('1. Hexa To Binary')
     print('2. Hexa To Decimal')
     print('3. Hexa To Octal')
     print('4. All')
     print('5. Back\n')
     h_input = int(input('[+][choose]> '))
     return h_input

def octalBanner():
     print('<[4] Octal Tools [4]>')
     print('1. Octal To Binary')
     print('2. Octal To Decimal')
     print('3. Octal To Hexa')
     print('4. All')
     print('5. Back\n')
     o_input = int(input('[+][choose]> '))
     return o_input
