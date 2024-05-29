def armstrong(num : int) -> int :
    sum = 0
    while num > 0 : 
        rem = num % 10
        sum = sum + rem**3
        num = num // 10
    return sum

try:
    num = int(input("Enter a number: "))
    print(armstrong(num))
except ValueError:
    print("Enter a valid positive number.")