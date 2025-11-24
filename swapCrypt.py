def swapbin(char):
    if char == "0":
        return "1"
    elif char == "1":
        return "0"
    else:
        return None
    


def swapcrypt(key,string):
    temptf = "0"
    cryptedtext = ""
    for i in range(len(string)):
        if key[i] == "1":
            temptf = swapbin(temptf)
        else:
            pass
        if temptf == "1":
            cryptedtext += swapbin(string[i])
        else:
            cryptedtext += string[i]
    return cryptedtext
def swapdecrypt(key,string):
    return swapcrypt(key=key,string=string)
def genkey(string):
    return swapcrypt(key=swapcrypt(key=string,string=string),string=string)
def chartobinstring(char):
    bi = bin(ord(char))
    return bi[2:len(bi)]
def stringtobin(string):
    bintext = ""
    for i in string:
        bintext += chartobinstring(i)
    return bintext
def cryptstring(key,string):
    print(f"string1: {string},Key1:{key}")
    string = swapcrypt(stringtobin(key),stringtobin(string))
    if len(string) < 8:
        string = "0"+string
        
    print(f"string1: {string},Key1:{key}")
    text = ''.join(chr(int(b, 2)) for b in string.split())
    print(f"string1: {string},Key1:{key}")
    print(f"text:{text}")
    return text
def decracptstring(key,string):
    print(f"Key:{key} String:{string}")
    return swapcrypt(stringtobin(key),stringtobin(string))
if __name__ == "__main__":
    print(swapcrypt(key="110",string="101"))
    print(genkey("010010101010001"))
    print(cryptstring("f","h"))
    print(decracptstring("e","e"))