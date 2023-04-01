def print_formatted(number):
    width=len(bin(number)[2:])
    for i in range(1,number+1):
        print(f"{i}".rjust(width) ,f"{i:o}".rjust(width),f"{i:X}".rjust(width), f"{i:b}".rjust(width))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)