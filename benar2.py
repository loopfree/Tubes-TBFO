# Function to print binary number using recursion
def convertToBinary(n):
   if n > 1:
       convertToBinary(n//2)
   print(n % 2)

# decimal number
dec = 34

convertToBinary(dec)
print()