for i in range(9):
    for j in range(9):
        print((i+1)*(j+1),end=" ")
        if (j+1)%9==0 :
            print("")

#解答
for i in range(1, 10):
    for j in range(1, 10):
        if j == 9:
            print(i * j,end="\n")
        else:
            print(i * j, end=" ")