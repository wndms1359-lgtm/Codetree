N = input()

cnt1 = 0
cnt2 = 0
for i in range(len(N)-1):
    if (N[i] + N[i+1] == "ee"):
        cnt1 += 1
    if (N[i] + N[i+1] == "ab"):
        cnt2 += 1

if cnt1 > 0 and cnt2 > 0 :
    print("Yes Yes")
elif cnt1 > 0 and cnt2 == 0:
    print("Yes No")
elif cnt1 == 0 and cnt2 > 0:
    print("No Yes")
else:
    print("No No")
