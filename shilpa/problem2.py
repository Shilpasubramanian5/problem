a = int(input("Enter a number: "))

output = []
for i in range(a):
    output.append(2 * i + 1)

print(", ".join(map(str, output)))
