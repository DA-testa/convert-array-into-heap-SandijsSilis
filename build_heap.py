# python3


def build_heap(data):
    swap = []
    for i in range(len(data)//2-1,-1,-1):
        while 1:
            min = i
            rightn=2+2*i
            leftn =1+2*i
            if len(data) > leftn and data[min] > data[leftn]:
                min = leftn
            if len(data) > rightn and data[min] > data[rightn]:
                min = rightn

            if min != i:
                data[min], data[i] = data[i], data[min]
                swap.append((i, min))
                i = min
            else:
                break
    return swap


def main():
    # n = 5
    # data = list(map(int, '5 4 3 2 1'.split()))
    n = input()
    data = list(map(int, input().split()))
    if 'I' in n:
        n = int(input())
        data = list(map(int, input().split()))
    if 'F' in n:
        filename = "./tests/" + input()     
        with open(filename, mode="r") as fails:
            n = int(fails.readline())
            data = list(map(int, fails.readline().split()))
    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
