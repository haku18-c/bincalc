# !/usr/bin/python3
# repo https://github.org/zbravv/bincalc
# mail => zbravv@protonmail.com

from lib.tools import DecTools
from lib.tools import BinTools
from lib.tools import OctalTools
from lib.tools import HexTools
from lib.banner import banner
from lib.banner import decimalBanner
from lib.banner import binaryBanner
from lib.banner import hexaBanner
from lib.banner import octalBanner
import os

def entering():
    print('\n\n')
    input('press any key to continue...')

def clear():
     os.system('clear')


def decRunner(num):
    while True:
       clear()
       decimal = DecTools(num)
       choice = decimalBanner()
       print('\n')
       print(f'#Decimal => {num}\n')
       if choice == 1:
          print('#Binary => ', decimal.dec_toBin())
       elif choice == 2:
          print('#Hexa =>  ', decimal.dec_toHex())
       elif choice == 3:
          print('#Octal => ', decimal.dec_toOctal())
       elif choice == 4:
          print('#Binary => ', decimal.dec_toBin())
          print('#Hexa   => ', decimal.dec_toHex())
          print('#Octal  => ', decimal.dec_toOctal())
       elif choice == 5:
          del decimal
          break
       else:
          print(f'no options for {choice} numbers!')
       entering()

def binRunner(bit):
    while True:
       clear()
       binary = BinTools(bit)
       choice = binaryBanner()
       print('\n')
       print(f'#Binary => {bit}\n')
       if choice == 1:
          print('#Decimal => ', binary.bin_toDec())
       elif choice == 2:
          print('#Hexa =>  ', binary.bin_toHex())
       elif choice == 3:
          print('#Octal => ',binary.bin_toOctal())
       elif choice == 4:
          print('#Decimal => ', binary.bin_toDec())
          print('#Hexa    => ', binary.bin_toHex())
          print('#Octal   => ', binary.bin_toOctal())
       elif choice == 5:
          del binary
          break
       else:
          print(f'no options for {choice} numbers!')
       entering()

def hexRunner(hexa):
    while True:
       clear()
       hexas = HexTools(hexa)
       choice = hexaBanner()
       print('\n')
       print(f'#Hexa => {hexa}\n')
       if choice == 1:
          print('#Binary  => ', hexas.hex_toBin())
       elif choice == 2:
          print('#Decimal => ', hexas.hex_toDec())
       elif choice == 3:
          print('#Octal   => ', hexas.hex_toOctal())
       elif choice == 4:
          print('#Decimal => ', hexas.hex_toDec())
          print('#Hexa    => ', hexas.hex_toBin())
          print('#Octal   => ', hexas.hex_toOctal())
       elif choice == 5:
          del hexas
          break
       else:
          print(f'no options for {choice} numbers!')
       entering()

def octalRunner(oct):
    while True:
       clear()
       octal = OctalTools(oct)
       choice = octalBanner()
       print('\n')
       print(f'#Octal => {oct}\n')
       if choice == 1:
          print('#Binary  => ', octal.oct_toBin())
       elif choice == 2:
          print('#Decimal => ', octal.oct_toDec())
       elif choice == 3:
          print('#Hexa    => ', octal.oct_toHex())
       elif choice == 4:
          print('#Decimal => ', octal.oct_toDec())
          print('#Binary  => ', octal.oct_toBin())
          print('#Hexa    => ', octal.oct_toHex())
       elif choice == 5:
          del octal
          break
       else:
          print(f'no options for {choice} numbers!')
       entering()

def main():
    while True:
       banner()
       try:
          ch = int(input('[+][choose]> '))
       except ValueError:
           print('Must Be Number !')
           entering()
           continue

       print('')
       if ch  == 1:
           dec = int(input('[Decimal]> '))
           decRunner(dec)
       elif ch == 2:
           bit = input('[Binary]> ')
           binRunner(bit)
       elif ch == 3:
           hexas = input('[Hexas]> ')
           hexRunner(hexas)
       elif ch == 4:
           oct = input('[Octal]> ')
           octalRunner(oct)
       elif ch == 5:
           print('Quit!')
           break
       else:
           print(f'no options for {ch} numbers !')

main()
