



# if operator == '+':
#     result = A + B
#     print(f"Sum: {A} + {B} = {result}")

# elif operator == "-":
#     result = A - B
#     print(f"Difference: {A} - {B} = {result}")

# elif operator == "*":
#     result = A * B
#     print(f"Product: {A} * {B} = {result}")

# elif operator == "/":
#     if B != 0: # Avoid division by zero
#         result = A / B
#         print(f"Division: {A} / {B} = {result}")
#     else:
#         print("Error: Division by zero is not allowed")

# else:
#     print("Invalid operator")


# A = float(input("Enter your first num: "))
# B = float(input("Enter your second num: "))
# operator = input("Enter operator (+ - * /): ").strip()

# if operator in "+-/*":
#     if operator == "/" and B == 0:
#         print("Error: Division by zero is not allowed")
    
#     else:
#         result = eval(str(A) + operator + str(B))
#         print(f"A {operator} B = {result}")

# else:
#     print("Invalid operator")



question = "5+6"
result = eval(question)
print(result)