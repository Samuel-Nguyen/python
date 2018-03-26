def TongHaiSo(so1,so2):
    assert(so1>0 and so2>0),"Gia tri khong hop le"
    return so1+so2
x,y=10,2
try:
    print(x/y)
    tong=TongHaiSo(10,10)
    print(tong)
except AssertionError as er:
    print(er)
except Exception as e:
    print("Da xay ra loi " , e)