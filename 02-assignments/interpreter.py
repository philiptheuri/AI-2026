#Prompt user for an expression
expr = input("Expression: ").split()

#Extract values
x = float(expr[0])
y = expr[1]
z = float(expr[2])

#Perform calculation
if y == "+":
    result = x + z

elif y =="-":
    result = x - z

elif y =="*":
    result = x * z

elif y =="/":
    result = x / z

#Output results formatted to 1 dp
print(f"{result:.1f}")
