# Write a function to print even numbers between two numbers
def evens(number1,number2):
    number1, number2
    for i in range(number1+1, number2):
        if i % 2 == 0:
            print(i, " ")

evens(10,20)
