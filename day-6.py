from typing import List


read_data = None
with open(r'K:\Downloads\input6.txt') as f:
    read_data = f.readlines()


def solve(init: List[str], iterations: int) -> int:
    counter = [0]*9
    for num in init:
        counter[int(num)] += 1
    for _ in range(iterations):
        counter = counter[1:7] + [counter[0] +
                                  counter[7]] + [counter[8]] + [counter[0]]
    return sum(counter)


print(solve(read_data[0].strip().split(','), 256))
