userString = input("Please enter some string")

normalisedString = userString.upper()
removeSpaces = normalisedString.strip()

print(removeSpaces)

originalString = len(userString)
newString = len(removeSpaces)

print("Your original string was {} characters. We've removed {} characters.".format(originalString, newString))