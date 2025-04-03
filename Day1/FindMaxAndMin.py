def findMaxAndMin(a):
    for i in range(len(a)):
        max=a[0]
        min=a[0]
        if a[i]>max :
            max=a[i]
        if a[i]<min :
            min=a[i]

    print(max)
    print(min)

a=[1,2,6,3,9,23]
findMaxAndMin(a)


