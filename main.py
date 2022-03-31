names = []
while True:  # Infinite loop
    name = input("What's the name of this person? ")
    if name == "":
        break
    names.append(name)

# print("\n---------- Persons list ----------")
# print(*names)  # Display Persons list
sortedNames = names
sortedNames.sort()

print("Initial list :\n")
for name in names:
    print(name)

print("Sorted list :\n")
for name in sortedNames:
    print(name)


