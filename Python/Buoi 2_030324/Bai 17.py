a,b=eval(input('Nhập a,b: '))
if a==0 and b==0:
    print('PT Vô số nghiệm')
elif a==0 and b!=0:
    print('PT Vô nghiệm')
else: print('x=%.1f'%(-b/a))