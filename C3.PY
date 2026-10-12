#Convert a positive decimal number to a binary string using repeated division by 2
def decimal_to_binary(n):
    if n == 0:
        return"0"
    binary_str = ""
    while n>0:
        remainder = n%2
        binary_str = str(remainder) + binary_str
        n = n//2
    return binary_str
ans1=decimal_to_binary(10)
ans2=decimal_to_binary(25)
print("Decimal to binary (10):",ans1)
print("Decimal to binary (25):",ans2)
