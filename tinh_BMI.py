import math
def tinhBMI(can_nang,chieu_cao):
    bmi=""
    can_nang=float(input('nhap so can nang: '))
    chieu_cao=float(input('nhap so chieu cao: '))
    if can_nang==0 or chieu_cao == 0:
       bmi=0
    else:
        chiso_bmi= can_nang/math.pow(chieu_cao,2)
        if chiso_bmi <18.5:
            print ( 'chi so bmi la:', bmi,'gay')
        elif 18.5<=chiso_bmi and chiso_bmi<25:
            print ( 'chi so bmi la:', bmi,'binh thuong')
        else:
            print ( 'chi so bmi la:', bmi,'thua can')