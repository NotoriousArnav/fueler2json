
# https://usamaejaz.com/cloudflare-email-decoding/

def cfDecodeEmail(encodedString):
    r = int(encodedString[:2],16)
    email = ''.join([chr(int(encodedString[i:i+2], 16) ^ r) for i in range(2, len(encodedString), 2)])
    return email

def fueler_filter(stri):
    email , _ = stri.split('?')
    return email
