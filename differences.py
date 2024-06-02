# Get Name
def getName():
    name = input("What is your name?: ")
    print("Your name is: " + name)
    return name

# getName();

# Reverse it
def reverseIt():
    string = "a man, a plan, a canal, frenemies!"
    reverse = ""
    for letter in string:
        # Here, by having "letter" first we are prepending to the empty string that is "reverse" and as we loop through the array we are going backwards in adding the characters
        reverse = letter + reverse
    print(reverse)

def reverseItSlice():
    string = "a woman, a plan, a project, friends!"
    # Here, we are using python's built-in slice method - The syntax is: sequence[start:stop:step] --> sequence refers to the item of concern (string, list, etc) - start refers to the index position where we begin the slicing (inclusive) - stop refers to the index position where we stop (exclusive) - and step refers to the invterval between characters/elements (If it is -1 we start from the end of the sequence)
    reverse = string[::-1]
    print(reverse)

# reverseIt()
# reverseItSlice()

# Swap Em
def swapEm():
    a = 10
    b = 30
    temp = 0

    temp = b
    b = a
    a = temp
    print("a is now " + str(a) + " and b is now " + str(b))

# swapEm()

# Mulitply Array/List
def multiplyList(list):
    if len(list) == 0:
        return 1
    
    total = 1

    for element in list:
        total = total * element
    print(total)
    return total

# multiplyList([1, 2, 3, 4, 5])

# Fizz Buzzer
def fizzbuzzer(number):
    if number % 3 == 0 and number % 5 != 0:
        print("fizz")
        return "fizz"
    elif number % 5 == 0 and number % 3 != 0:
        print("buzz")
        return "buzz"
    elif number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
        return "fizzbuzz"
    else:
        print("luigi")
        return "luigi"

# fizzbuzzer(15)

# Nth Fibonacci
def nthFibonacciNumber():
    fibs = [1, 1, 2, 3]
    num = int(input("Which fibonacci number do you want?: "))

    while len(fibs) < num:
        length = len(fibs)
        nextFib = fibs[length - 2] + fibs[length - 1]
        fibs.append(nextFib)
        # NOTE: We can use f-string formatting to embed exressions, variables, etc. inside a string --> This is much easier than concactenating a string and it is similar to using template literals with backticks in JavaScript --> The syntax is that we must use the prefix "F" or "f" before the first quotations that contains the string literal and any value or expression not in string format MUST go inside curly braces {}
    print(F"{fibs[num - 1]} is the Fibonacci number at position {num}")

# nthFibonacciNumber()

# Search Array/List
def searchArray(array, value):
    for element in array:
        if element == value:
            return True
    return False  

# print(searchArray([1, 2, 3], 1))

# Palindrome
theArray = [1, 2, 3, 4]
    # Here, we are using the "floor division operator" (//) to divide the length of a list by the operand that comes after --> If the length of the List is an odd number and we want half the length, the result will be rounded DOWN to the nearest integer
# print(len(theArray) // 2)

def isPalindrome(str):
    # Store length of original sequence/string in a variable
    length = len(str)
    # Using for in loop with a range on half of the original string to iterate over the FIRST half of the string
    for character in range(length // 2):
        # Here, we are comparing each character from the first half of the string starting at the begining (left) to the character in the second half starting from the end (syntax for that is str[length - 1 - character])
        if str[character] != str[length - 1 - character]:
            return False
    return True

# print(isPalindrome("huluh"))

# hasDupes
def hasDupes(list):
    obj = {}
    for element in list:
        # Here, we are checking if element exists in the obj --> The word "in" when used with the conditional statement "if" is a membership operator (Definition: It checks whether the value on its LEFT side exists in the collection on its right side)
        if element in obj:
            return True
        else:
            obj[element] = True
    return False

print(hasDupes([1, 2, 3, 4]))
