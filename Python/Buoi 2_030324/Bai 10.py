x=int(input('Nhập số tiền: '))
x500=x//500000
x%=500000
x200=x//200000
x%=200000
x100=x//100000
x%=100000
x50=x//50000
x%=50000
x_du=x%50000
print('Số tờ 500K: ',x500)
print('Số tờ 200K: ',x200)
print('Số tờ 100K: ',x100)
print('Số tờ 50K: ',x50)
print('Số tiền dư: ',x_du)
