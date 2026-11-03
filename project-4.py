# FIBONACCI SERIES USING RECURSION

def fibonacci(a, b, n):
    if n == 0:
        return

    print(a, end=" ")
    fibonacci(b, a + b, n - 1)


print("================================")
print("       FIBONACCI SERIES")
print("================================")

terms = int(input("Enter the number of terms: "))

if terms <= 0:
    print("Please enter a positive number.")
else:
    print("\nFibonacci Series:")
    fibonacci(0, 1, terms)

print("\n\n================================")
print("       PROGRAM COMPLETED")
print("================================")