phrase1 = list(input())
phrase2 = list(input())

proof = []


def ast_len(phrase):
    acc = 0
    for i in range(len(phrase)):
        if phrase[i] == '*':
            acc += 1
    return acc


for letter in phrase1:
    for letter_ in phrase2:
        print(letter, letter_)
        if letter == letter_:
            phrase2.remove(letter)
            print(phrase1, phrase2)
            

if len(phrase2) == 0 or len(phrase2) - ast_len(phrase2) == 0:
    print("yes!")
else:
    print("no!")