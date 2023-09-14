# !/usr/bin/python3
# zbravv binary calc
# sunday 10/09/2023 00:12 Yogyakarta
HEXA = '0123456789abcdef'

def pembalik(text):
    size = len(text)
    result = ''
    while( size > 0):
         result += text[size-1]
         size -= 1
    return result
#
# dec section
class DecTools(object):

    def __init__(self, num):
        self.num = num

    def dec_toBin(self):
        bits = self.num
        _bin = ''
        while(bits > 0):
            bit = bits%2
            _bin  += str(bit)
            bits //= 2
        _bin = pembalik(_bin)
        return _bin # return 8bits => str

    def dec_toHex(self):
        _hex = ''
        bits = self.num
        while(bits > 0):
             bit = bits%16
             _hex += HEXA[bit]
             bits //= 16
        _hex = pembalik(_hex)
        if(len(_hex) < 4):
            result = _hex.zfill(4)
        elif(len(_hex) > 4 and len(_hex) <= 8):
            result = _hex.zfill(8)
        else:
            result = _hex.zfill(16)
        return result


    def dec_toOctal(self):
        oct = ''
        bits = self.num
        while bits > 0:
            bit = bits % 8
            oct += str(bit)
            bits //=8
        result = pembalik(oct)
        return result
#


# bin section

class BinTools(DecTools):

    def __init__(self, bits):
        self.bits = bits
        super().__init__(self.bin_toDec())

    def bin_toDec(self): # bin str
        l_bit = pembalik(self.bits)
        result = 0
        for i in range(len(l_bit)):
            if(l_bit[i] == '1'):
                  result += 2 ** i
        return result

    def bin_toHex(self):
        return self.dec_toHex()

    def bin_toOctal(self):
        return self.dec_toOctal()
    #
    # hex section

class HexTools(BinTools):

    def __init__(self, hexa):
        self.hexa = hexa
        super().__init__(self.hex_toBin())

    def hex_toBin(self):
        _hex = self.hexa
        hex_raw = pembalik(_hex)
        number = 0
        for i in range(len(hex_raw)):
             num = HEXA.find(hex_raw[i])
             number += num *(16**i)
        result = ''
        while(number > 0):
            bit = number%2
            result  += str(bit)
            number //= 2
        result = pembalik(result)
        return result

    def hex_toDec(self):
        return self.bin_toDec()

    def hex_toOctal(self):
        return self.dec_toOctal()

# Octal Section
class OctalTools(HexTools):

    def __init__(self, octal):
        self.octal = octal
        super().__init__(self.oct_toHex())

    def oct_toHex(self):
        _oct = self.octal
        oct_raw = pembalik(_oct)
        number = 0
        for i in range(len(oct_raw)):
              number += int(oct_raw[i]) * (8**i)
        _hex = ''
        while(number > 0):
             bit = number%16
             _hex += HEXA[bit]
             number //= 16
        _hex = pembalik(_hex)
        if(len(_hex) < 4):
            result = _hex.zfill(4)
        elif(len(_hex) > 4 and len(_hex) <= 8):
            result = _hex.zfill(8)
        else:
            result = _hex.zfill(16)
        return result

    def oct_toBin(self):
        return self.hex_toBin()

    def oct_toDec(self):
        return self.hex_toDec()




