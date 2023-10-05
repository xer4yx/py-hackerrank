class Queen:
    def myFunc(N):
        if (N == 1):
            print(N)
        elif (N == 2):
            print(N // 2)
        elif (N % 2 == 0):
            print(N)
        else:
            print((N // 2) + 1)

if __name__ == "__main__":
    N = int(input())
    run = Queen
    run.myFunc(N)