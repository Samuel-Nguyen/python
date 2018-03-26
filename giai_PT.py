import math
def GPTBHai (a, b, c):
    ketqua=''
    if a==0:
        ketqua="Phuong trinh khong hop le"
    else:
        delta= b*b - 4*a*c
        if delta < 0:
            ketqua='Phuong trinh vo nghiem'
        elif delta ==0:
            ketqua='Phuong trinh co nghiem kep x1 = x2' + str(-b/(2*a))
        else:
            ketqua= 'Phuong trinh co 2 nghiem phan biet'
            ketqua += 'x1= '+str((-b+math.sqrt(delta))/(2*a))
            ketqua += ' ; x2= '+str((-b-math.sqrt(delta))/(2*a))
    return ketqua
