so_nguyen_duong=int(input("nhap vao 1 so nguyen duong: "))

i=2
flag=1
if (so_nguyen_duong>=2):
    while (i<so_nguyen_duong):
        if so_nguyen_duong%i==0:
            flag=0
            break
        i+=1
    if flag==1:
        print ("%i là so nguyen to" %so_nguyen_duong)
    else:
        print ("%i khong phai la so nguyen to"%so_nguyen_duong)
else:
    print ("%i khong phai la so nguyen to"%so_nguyen_duong)
