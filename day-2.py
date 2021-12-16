read_data = None
with open(r'K:\Downloads\input2.txt') as f:
    read_data = f.readlines()

position, depth = 0, 0
for command in read_data:
    X = int(command.split()[1])
    if command.startswith('f'):
        position += X
    elif command.startswith('d'):
        depth += X
    elif command.startswith('u'):
        depth -= X
print(position * depth)

position, depth, aim = 0, 0, 0
for command in read_data:
    X = int(command.split()[1])
    if command.startswith('f'):
        position += X
        depth += (aim * X)
    elif command.startswith('d'):
        aim += X
    elif command.startswith('u'):
        aim -= X
print(position * depth)
