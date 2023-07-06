num = int(input("Enter an integer: "))
if(num % 2 == 1):
    fact = 1
    for i in range(2, num + 1):
        fact *= i
        digits = len(str(fact))
    print("Factorial of", num, "is:", fact)
    print("Number of digits in the factorial:",digits)
else:
    palindrome = True
    num_str = str(num)
    length = len(num_str)
    for i in range(length // 2):
        if num_str[i] != num_str[length-i- 1]:
            palindrome = False
        break
    if palindrome:
        print(num, "is a palindrome")
    else:
        print(num, "is not a palindrome")
