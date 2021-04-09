valor = int(input("insert the value of the house. "))
salary = int(input("insert your salary. "))
years = int(input("insert how many years. "))

month = years * 12
installment = valor / month

print(f'{installment:.2f}' if installment <= salary * 0.3 else "your loan wasn't accepted")
