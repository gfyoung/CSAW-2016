import base64
import binascii

filename = 'sleepingdata.txt'
data = open(filename, 'r').read()

filename = 'sleeping.png'
_bytes = base64.b64decode(data)

def add_pad(msg):
    l = 12 - len(msg)%12
    msg += (chr(l)*l).encode('utf-8')
    return msg

def xor(s1, s2):
    res = [chr(0)]*12
    for i in range(len(res)):
        q = ord(s1[i])
        #q = s1[i]
        d = ord(s2[i])
        k = q ^ d
        res[i] = chr(k)
    res = ''.join(res)
    return res

header = '89504e470d0a1a0a'
_newbytes = binascii.hexlify(_bytes[:12])
key = xor(_newbytes.decode('utf-8'), header)

_bytes = add_pad(_bytes)

target = open(filename, 'wb')
text = ''
#print(type(key))
for i in range(0, len(_bytes), 12):
        _newbytes = binascii.hexlify(_bytes[i:i+12])
        _xordata = xor(_newbytes.decode('utf-8'), key)
        #target.write(_xordata.encode('utf-8'))
        text += _xordata
#target.write(binascii.unhexlify(header))
target.write(text)
target.close()

