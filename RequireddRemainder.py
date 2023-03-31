x = int(input())

for i in range(0,x):
    y = str(input()).split()
    z = int(y[2]) - int(y[1])
    l = int(z/int(y[0]))
    answer = l*(int(y[0]))+int(y[1])
    print(answer)