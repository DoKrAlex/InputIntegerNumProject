"""
Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered,
print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a
try/except and put out an appropriate message and ignore the number.
"""

largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        num = int(num)
        if largest is None or largest < num:
            largest = num
        elif smallest == None or smallest > num:
            smallest = num

    except:
        print("Invalid input:")
        continue

    #print(num)

print("Maximum is ", largest)
print("Minimum is ", smallest)

'''
Results:
Enter a number: 10
Enter a number: 1
Enter a number: 9
Enter a number: 124
Enter a number: 23
Enter a number: done
Maximum is  124
Minimum is  1
'''