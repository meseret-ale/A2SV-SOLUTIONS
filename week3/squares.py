the_input=input()
alist=the_input.split()
m=int(alist[0])
n=int(alist[1])
a=int(alist[2])
def squares(m,n,a):#n is len
    cnt=(m//a) 
    if n%a==0:
        row=n/a
    else:
        row=(n//a) +1
    row_area=a*m
    area_left=row_area-(m//a)*(a*a)
    while area_left>0:
        area_left-=(a*a)
        cnt+=1
    return int(row*cnt)

print(squares(m,n,a))
    
