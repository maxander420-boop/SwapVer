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
if __name__ == "__main__":
    print(swapcrypt(key="110",string="101"))
    print(genkey("010101001010"))
