import json
import math
def NhapDanhSachPhuongTrinhBachHai(path):
    try:
        flag=1
        dsPT=[]
        n=0
        while n<=0:
            n=int(input('Ban muon nhap bao nhieu phuong trinh'))
        for i in range(n):
            a,b,c=eval(input('Nhap a,b,c:\t'))
            pt={'a':a,'b':b,'c':c}
            dsPT.append(pt)
        #Luu vao file
        f=open(path,'w')     
        json.dump(dsPT, f,indent=4)        
        f.close()
    except Exception as ex:
        flag=-1
    finally:
        return flag
def DocDanhSachPTBachHai(path):
    f=open(path,encoding='utf-8')
    noi_dung=json.load(f)
    for pt in noi_dung:
        print(pt)
def GiaiPhuongTrinhBachHai(a,b,c):
    try:
        nghiem=''
        if a==0:
            nghiem='Phuong trinh khong hop le'
        else:
            delta=b*b-4*a*c
            if delta<0:
                nghiem='Phuong trinh vo nghiem'
            elif delta==0:
                nghiem='Phuong trinh co nghiem ket x1=x2='+str(-b/(2*a))
            else:
                x1=((-b+math.sqrt(delta))/(2*a))
                x2=((-b-math.sqrt(delta))/(2*a))
                nghiem='Phuong trinh co hai nghiem\n';
                nghiem+='x1 = ' + str(x1)
                nghiem+='x2 = ' + str(x2)
    except Exception as e:
        raise e
    finally:
        return nghiem
def GiaiDanhSachPhuongTrinhBacHai(path, path_luu):
    f=open(path,encoding='utf-8')
    noi_dung=json.load(f)
    dsPTGiai=[]
    for pt in noi_dung:
        a=0
        b=0
        c=0
        for key,value in pt.items():
            if key=='a':
                a=value
            elif key=='b':
                b=value
            else:
                c=value
        nghiem=GiaiPhuongTrinhBachHai(a,b,c)
        pt['n']=nghiem
        dsPTGiai.append(pt)
    #ghi file
    f=open(path_luu,'w')
    json.dump(dsPTGiai,f,indent=4)
    f.close()
def InPhuongTrinhVoNghiem(path):
    f=open(path,encoding='utf-8')
    dsPT=json.load(f)
    for pt in dsPT:
        if pt.get('n')=='Phuong trinh vo nghiem':
            print(pt)
def InPhuongTrinhKhongHopLe(path):
    f=open(path,encoding='utf-8')
    dsPT=json.load(f)
    for pt in dsPT:
        if pt.get('n')=='Phuong trinh khong hop le':
            print(pt)
def InPhuongTrinhCoNghiem(path):
    f=open(path,encoding='utf-8')
    dsPT=json.load(f)
    for pt in dsPT:
        if pt.get('n').find('Phuong trinh co nghiem')!=-1 or pt.get('n').find('Phuong trinh co 2 nghiem')!=-1:
            print(pt)