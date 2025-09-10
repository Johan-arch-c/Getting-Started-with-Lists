start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
squares = [x**2 for x in range(start, end + 1)]
print("List of square values:")
print(squares)
