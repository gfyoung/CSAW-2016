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

ords = [137, 80, 78, 71, 13, 10, 26, 10]
enc_ords = [ord(x) for x in _bytes[:8]]
last = [ord(x) for x in _bytes[-12:]]
key = []
for i in range(0, len(ords)):
    for x in range(255):
        if ords[i] ^ x == enc_ords[i]:
            key.append(x)
            break

# pad = 4
# for i in range(8, 12):
#     for x in range(255):
#         if x ^ pad == last[i]:
#             key.append(x)

_bytes = add_pad(_bytes)
for y in range(255):
    n = chr(y)
    full_key = ''.join([chr(x) for x in key])+'ey!'+n

    text = ''
    for i in range(0, len(_bytes), 12):
        _xordata = xor(_bytes[i:i+12], full_key)
        text += _xordata

    if 'Orientation' in text:
        print full_key
        break

target = open(filename, 'wb')
#target.write(binascii.unhexlify(header))
target.write(text)
target.close()

