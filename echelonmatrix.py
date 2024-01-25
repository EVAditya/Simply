#I am trying hard to make a reduced echelon matrix using the given augmented matrix

#First I make the regular echelon matrix

def swap(r1):
    rr=a.pop(r1)
    a.append(rr)


a=[[1,2,3,1],[4,5,6,2],[7,8,9,3]]

row=len(a)
col=len(a[0])

print('initializing')

k=0
p=-1
while k<=row:
    if a[k][0]==0:
        swap(k)
        k+=1
    elif p!=-1:
        a[k]=[x/a[k][0] for x in a[k]]
        p=k
    else:
        a[k]=[x-a[p][ind] for ind,x in enumerate(a[k])]


print(a)
print('the process is done')







