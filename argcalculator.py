import sys
if len(sys.argv)<4:
    print("you have less arguments than necessary!")
a = int(sys.argv[1])
b = int(sys.argv[3])
op = sys.argv[2]
if op == '+':
    res = a + b
elif op == '-':
    res = a - b
elif op == '*':
    res = a * b
elif op == '/':
    res = a / b
else:
    print("Invalid operator: '{}'".format(op))
    exit()
print(res)










