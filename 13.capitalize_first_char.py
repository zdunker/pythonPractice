import sys

input = "kasdjfklj /asakfj ()*()78283 ccxczxcxzlsdjfoaikj"
firstCharchanged = False
output = []
for i in range(len(input)):
    if not firstCharchanged:
        if input[i].isalpha():
            output.append(input[i].upper())
            firstCharchanged = True
        else:
            output.append(input[i])
    elif input[i] == ' ':
        firstCharchanged = False
        output.append(input[i])
    else:
        output.append(input[i])

print "".join(output)