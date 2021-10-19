fruits = ["apple", "banana", "cherry", "avocado", "blueberry", "apricot"]
print()
print("---------------------------")
choice = int(input("pick a number between 1 and "+str(len(fruits))+": "))
print()
print("I'm thinking of a fruit beginning with... " + '"' + fruits[choice - 1][0].upper() + '"!')
print()
answer = input("and your guess is...? ")

print()

if answer.upper() == fruits[choice - 1].upper():
    print("CORRECT!")
else:
    print("...wrong, sorry... :(")

print()
print("---------------------------")
print()

