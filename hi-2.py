string = input()
stringLen = len(string)
charToFind = 'c'

for i in range(0, stringLen - 1):
    if i != 3:
        print(string[i])

if charToFind in string:
    print(f'{string} contains {charToFind}')

#that's what's good
