fruits = ["apple", "banana", "cherry"]
print()
print("---------------------------")
choice = int(input("pick a number between 1 and "+str(len(fruits))+": "))
print()
print('I spy, with my little eye, a fruit beginning with... "' + fruits[choice - 1][0] + '"!')
print()
answer = input("and your guess is...? ")

print()

if answer == fruits[choice - 1]:
    print("CORRECT!")
else:
    print("...wrong, sorry... :(")

print()
print("---------------------------")
print()

