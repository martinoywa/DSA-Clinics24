from math import log2


def power_of_two(n):
    return log2(n) == int(log2(n))


if __name__ == "__main__":
    print(f"8 => {power_of_two(8)}")
    print(f"6 => {power_of_two(6)}")
