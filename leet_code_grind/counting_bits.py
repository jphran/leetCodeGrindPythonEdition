from typing import List


def count_bits(self, num: int) -> List[int]:
    container = [0]
    for i in range(1, num + 1):
        container.append(container[i & (i-1)] + 1)
        # first attempt
        # container.append(sum([int(num, base=16) for num in bin(i)[2:]]))

    return container

