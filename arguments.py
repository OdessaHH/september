import sys

n = len(sys.argv)
print("Total arguments passed:",n)

print("Name of Python Script:", sys.argv[0])

sum_of_integers = 0

for i in range(1,n):
    sum_of_integers += int(sys.argv[i])

print("Result:", sum_of_integers)