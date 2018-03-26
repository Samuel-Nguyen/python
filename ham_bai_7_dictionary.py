def themdanhba(danhsach):
    tt = 0
    while tt <= 0:
        tt = int(input('ban muon them bao nhieu'))
    for i in range(tt):
        print(i+1, '\t')
        name = input('nhap ten danh ba: \t')
        sdt = input('nhap sdt: \t')
        danhsach[name] = sdt


def indanhsachdanhba(danhsach):
    for key, value in danhsach.items():
        print(key, '====\t', str(value))


def timkiemdanhba(danhsach, ten):
    sodienthoai = danhsach.get(ten)
    if sodienthoai not None:
        print(ten, '====\t', str(sodienthoai))
    else:
        print('khong tim thay')


def capnhatdanhba(danhsach):
    name = input('nhap ten danh ba: \t')
    sdt = input('nhap sdt: \t')
    danhsach[name] = sdt
