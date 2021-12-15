read_data = None
with open(r'K:\Downloads\input1.txt') as f:
    read_data = list(map(int, f.readlines()))
prev = read_data[0]
count = 0
for num in read_data[1:]:
    if num > prev:
        count += 1
    prev = num
print(count)

prev = sum(read_data[:3])
count = 0
for index, num in enumerate(read_data[3:]):
    new_sum = prev - read_data[index] + num
    if new_sum > prev:
        count += 1
    prev = new_sum
print(count)
