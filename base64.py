alphabet = b'ABCDEFGHIJKLMOPQRSTUVWXYZabcdefghijklmopqrstuvwxyz0123456789+/'
print(alphabet)
src = 'abcd'
def base64encode(src:str):
    ret = bytearray