if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    A = list(dict.fromkeys(A))
    A.sort()
    A.remove(max(A))
    print(max(A))