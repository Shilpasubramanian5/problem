
a = int(input("Enter a number: "))
if a % 2 == 0:
    a -= 1
output = []
for i in range(a):
    output.append(2 * i + 1)
print(", ".join(map(str, output)))
