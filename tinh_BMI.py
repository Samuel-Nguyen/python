import math
# a<x and x<b A<x<b


def tinhBMI(can_nang, chieu_cao):
    bmi = 0
    # can_nang=float(input('nhap so can nang: '))
    # chieu_cao=float(input('nhap so chieu cao: '))
    if can_nang == 0 or chieu_cao == 0:
        return 0
    else:
        chiso_bmi = can_nang/math.pow(chieu_cao, 2)
        if chiso_bmi < 18.5:
            return ('chi so bmi la:', bmi, 'gay')
        elif 18.5 <= chiso_bmi and chiso_bmi < 25:
            return ('chi so bmi la:', bmi, 'binh thuong')
        else:
            return ('chi so bmi la:', bmi, 'thua can')
