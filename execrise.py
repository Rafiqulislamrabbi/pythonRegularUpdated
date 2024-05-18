# check the number is prime or not

# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, (num // 2) + 1):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")


# print 1 to 20 prime numbers

# for num in range(1, 21):
#     if num > 1:
#         is_prime = True
#         for i in range(2, int(num //2) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(num)


# print the Fibonacci numbers

# n_terms = int(input("How many terms : "))
#
# a, b = 0, 1
#
# if n_terms <= 0:
#     print("Please enter a positive integer")
# elif n_terms == 1:
#     print("Fibonacci sequence up to", n_terms, "term:")
#     print(a)
# else:
#     print("Fibonacci sequence:")
#     for _ in range(n_terms):
#         print(a, end=' ')
#         a, b = b, a + b


# check the mobile number operator

# n=str(input("Enter Your Number :"))
# a="017"
# b="018"
# c="019"
# d="016"
# e="015"
# if a==n[:3]:
#     print("number is Grameenphone")
# elif b==n[:3]:
#     print("Number is Robi")
# elif c==n[:3]:
#     print("Number is Banglalink")
# elif d==n[:3]:
#     print("Number is Airtel")
# elif e==n[:3]:
#     print("Number is Telitalk")
# else:
#     print("Please Input a Valid Number")


num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)
