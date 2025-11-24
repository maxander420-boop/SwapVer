def swapbin(char):
    if char == "0":
        return "1"
    elif char == "1":
        return "0"
    else:
        return None
    

#The main funktion that is needed to crypt an bin string with an bin key
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

#funktion zum entschlüsseln von bin string
def swapdecrypt(key,string):
    return swapcrypt(key=key,string=string)

#funktion zum generieren von einem key nur der key wird durch den string generiert indem der bin string mit sich selbst verschlüsselt wird
def genkey(string):
    return swapcrypt(key=swapcrypt(key=string,string=string),string=string)

#funktion die einen char to einen byte string convertiert
def chartobinstring(char):
    bi = bin(ord(char))
    return bi[2:len(bi)]

#funktion die mithilfe vin chartobin einen string in einen bin string convertiert
def stringtobin(string):
    bintext = ""
    for i in string:
        bintext += chartobinstring(i)
    return bintext

#funktion die einen string verschlüsselt mithilfe eines strings die ausgabe ist ein verschlüsselter string
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

#funktion die einen verschlüsselten string entschlüsselt
def decrycptstring(key,string):
    print(f"Key:{key} String:{string}")
    return cryptstring(key,string)

#testet jede wichtige funktion
if __name__ == "__main__":
    print(swapcrypt(key="110",string="101"))
    print(genkey("010010101010001"))
    print(cryptstring("f","h"))
    print(decrycptstring("e","e"))