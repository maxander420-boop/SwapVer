def swapbin(char):
    if char == "0":
        return "1"
    elif char == "1":
        return "0"
    else:
        return None
    


def crypt(key,string):
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


if __name__ == "__main__":
    print(crypt(key="110",string="101"))
