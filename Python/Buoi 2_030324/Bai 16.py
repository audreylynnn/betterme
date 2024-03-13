x=float(input("Nhập điểm trug bình: "))
if x<3.5:
    print('Kém')
elif x<5:
    print('Yếu')
elif x<6.5:
    print('Trung bình')
elif x<8:
    print('Khá')
elif x>=8:
    print('Giỏi')
else: print('Điểm ko hợp lệ')