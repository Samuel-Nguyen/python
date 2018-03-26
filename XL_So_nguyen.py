def NhapDanhSachSoNguyen(danhSach):
    tt=1
    print('Nhap vao danh sach cac so nguyen, ket thuc -1')
    while tt!=-1:
        tt=int(input(' '))
        if tt!=-1:
            danhSach.append(tt)
def InDanhSachSoNguyen(danhSach):
    chuoi=''
    for so in danhSach:
        chuoi += str(so)+' '
    print(chuoi)
def TongDanhSach(danhSach):
    tong=0
    for so in danhSach:
        tong+=so
def InDanhSole(danhSach):
    chuoi=''
    for so in danhSach:
        if so%2!=0:
            chuoi += str(so)+' '
    print(chuoi)
def InDanhSoChan(danhSach):
    chuoi=''
    for so in danhSach:
        if so%2==0:
            chuoi += str(so)+' '
    print(chuoi)
def kiemTraSoNguyenTo(so):
    if so<2:
        return False
    flag=True
    for i in range(2,so):
        if so %i==0:
            flag=False
            break
    return flag

def inDanhSachSoNguyenTo(danhSach):
    chuoi=''
    for so in danhSach:
        if kiemTraSoNguyenTo(so):
            chuoi += str(so) + ' '
    print(chuoi)
    
    
