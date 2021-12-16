read_data = None
with open(r'K:\Downloads\input3.txt') as f:
    read_data = f.readlines()

pos_count = [0 for _ in read_data[0].strip()]
for binary_num in read_data:
    for index, bit in enumerate(binary_num.strip()):
        if bit == '1':
            pos_count[index] += 1
        else:
            pos_count[index] -= 1
gamma_bits = [int(x > 0) for x in pos_count]
gamma = int(''.join(map(str, gamma_bits)), 2)
epsilon_bits = [1 - bit for bit in gamma_bits]
epsilon = int(''.join(map(str, epsilon_bits)), 2)
print(gamma * epsilon)

to_consider = read_data[:]
index = 0
while len(to_consider) > 1:
    pos_count = 0
    zeros = []
    ones = []
    for binary_num in to_consider:
        bit = binary_num.strip()[index]
        if bit == '1':
            pos_count += 1
            ones.append(binary_num)
        else:
            pos_count -= 1
            zeros.append(binary_num)
    if pos_count >= 0:
        to_consider = ones
    else:
        to_consider = zeros
    index += 1
oxygen_generator_rating = int(to_consider[0].strip(), 2)

to_consider = read_data[:]
index = 0
while len(to_consider) > 1:
    pos_count = 0
    zeros = []
    ones = []
    for binary_num in to_consider:
        bit = binary_num.strip()[index]
        if bit == '1':
            pos_count += 1
            ones.append(binary_num)
        else:
            pos_count -= 1
            zeros.append(binary_num)
    if pos_count < 0:
        to_consider = ones
    else:
        to_consider = zeros
    index += 1
co2_scrubber_rating = int(to_consider[0].strip(), 2)

print(oxygen_generator_rating * co2_scrubber_rating)
