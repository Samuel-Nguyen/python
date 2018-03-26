def nam_am_lich(namduonglich):
    list_can=('Canh','Tan','Nham','Quy','Giap','At','Binh','Dinh','Mau','Ky')
    list_chi=('Than','Dau','Tuat','Hoi','Ti','Suu','Dan','Meo','Thin','Ti','Ngo','Mui')
    return list_can[namduonglich%10] + ' ' +list_chi[namduonglich%12]

if __name__=='__main__':
    namDuong= int(input('Nhap nam duong lich:  '))
    namAm=nam_am_lich(namDuong)
    print ('nam %d la nam %s'%(namDuong,namAm))