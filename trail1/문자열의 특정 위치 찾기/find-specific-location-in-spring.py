N, tc = input().split()


cnt = -1
for i in range(len(N)):
    if N[i] == tc:
        cnt += 1
        print(i)
        break

if cnt == -1:
    print("No")