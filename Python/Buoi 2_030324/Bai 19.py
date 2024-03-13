xe=input('Nhập loại xe: ')
if xe!='4' and xe!='7':
    print('Xe không hợp lệ')
else:
    x=int(input('Nhập số km: '))
    tg_cho=int(input('Nhập thời gian chờ: '))
    phi_cho=0
    if tg_cho>5:
        phi_cho=(tg_cho-5)*750
    if xe=='4':
        if x<=0.5:
            tien_cuoc=11000
        elif 0.5<x<=30:
            tien_cuoc=11000+(x-0.5)*17600
        else: tien_cuoc=11000+29.5*17600+(x-30)*14500
    else:
        if x<=0.5:
            tien_cuoc=12000
        elif 0.5<x<=30:
            tien_cuoc=12000+(x-0.5)*19600
        else: tien_cuoc=12000+29.5*19600+(x-30)*17100
    print('Tiến cước xe: ',tien_cuoc)
    print('Tiền chờ: ',phi_cho)
    print('Thanh toán: {:,}+{:,}={:,} VNĐ'.format(tien_cuoc,phi_cho,tien_cuoc+phi_cho))