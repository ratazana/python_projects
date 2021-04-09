base10 = int(input("insert the value in base 10: "))
basechange = int(input("select the base you want: "))

basemod = []
biggerbases = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
#biggersbases works until hex, for bases bigger than that, add more letters to it

while base10 >= 1:
    if base10 % basechange < 10:
        basemod.append(base10 % basechange); base10 //= basechange
#we divide the number until it's integer part is zero
#and we save the remainder on the list
    else:
        basemod.append(biggerbases[int((base10 % basechange) % 10)]); base10 //= basechange
#for bases bigger than 10, we use letters for digits bigger than 9

basemod.reverse()
basemod = "".join(map(str, basemod)) #transform the list into a string

print(basemod)


