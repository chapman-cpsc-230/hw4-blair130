numbers = []
response = " "

while (response == " "):
    numbers.append((int)(raw_input("Please enter a number!")))
    response = raw_input("Hit spacebar and enter to input another number. Hit only enter to print.")

def Histogram(number):
    asterisks = ""
    for i in range(number):
        asterisks += "*"
    print asterisks

for i in range(len(numbers)):
    Histogram(numbers[i])
