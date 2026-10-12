#Evaluate AND, OR, XOR logic gates after validating 0 or 1 inputs
A = int(input("Enter A:"))
B = int(input("Enter B:"))
if A not in (0,1) or B not in (0,1):
    print("BITS MUST BE 0 OR 1")
else:
    and_result = A & B
    or_result = A | B
    xor_result = A ^ B
print("AND RESULT:",and_result)
print("OR RESULT:",or_result)
print("XOR RESULT:",xor_result)
