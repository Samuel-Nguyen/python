def ThemDanhBa(danhSach):
    tt=0
    while tt<=0:
        tt=int(input('Ban muon them bao nhieu'))
    for i in range(tt):
        print(i+1,"\t")
        name=input("Ten danh ba: \t")
        sdt=input("So dien thoai: \t")
        danhSach[name]=sdt
def InDanhSachDanhBa(danhSach):
    for key,value in danhSach.items():
        print(key,"===\t",str(value))
def TimKiemDanhBa(danhSach, ten):
    SDT=danhSach.get(ten)
    if SDT!=None:
        print(ten,"===\t",str(SDT))
    else:
        print("Khong tim thay")
def CapNhatDanhBa(danhSach):
    name=input("Ten danh ba: \t")
    sdt=input("So dien thoai: \t")
    danhSach[name]=sdt