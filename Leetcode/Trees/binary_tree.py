import re

def reverseString(s):
    if len(s) == 0:
        return ""
    print(s)
    return reverseString(s[1:])+s[0]

s = "2947829001284829"

def convertStringtoInt(s):
    #determine base ascii value of 0
    c = '0'
    rtr = 0
    print(ord(c))
    for char in s:
        rtr = rtr*10 + ord(char) - ord(c)
    return rtr

def reverseStringIter(s):
    if len(s) == 0:
        return ""
    pointer1 = 0
    pointer2 = len(s)-1
    s = list(s)
    while True:
        if pointer1<pointer2:
            temp = s[pointer1]
            s[pointer1] = s[pointer2]
            s[pointer2] = temp
            pointer1+=1
            pointer2-=1
        else:
            return "".join(s)


print(reverseStringIter("bruh"))

txt = "The rain in Spain"
x = re.findall("The .",txt)
print(x)