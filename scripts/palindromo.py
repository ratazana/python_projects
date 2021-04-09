phrase = input("insert the phrase. ").replace(" ", "")
if phrase == phrase[::-1]:
    print("yes")
else:
    print("no")

