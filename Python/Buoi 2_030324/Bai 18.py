import math
a,b,c=eval(input('Nhập a,b,c: '))
if a==0:
    if b==0 and c==0:
      print('PT Vô số nghiệm')
    elif b==0 and c!=0:
      print('PT Vô nghiệm')
    else: print('x=%.1f'%(-c/b))
else:
    delta=b**2-4*a*c
    if delta<0:
      print('PT vô nghiệm')
    elif delta==0:
      print('PT có nghiệm kép x=%.1f'%(-b/(2*a)))
    else:
       print('PT có 2 nghiệm phân biệt: ')
       print('x1=%.1f'%((-b+math.sqrt(delta))/(2*a)))
       print('x2=%.1f'%((-b-math.sqrt(delta))/(2*a)))