Product=input('Nhập sản phẩm: ')
Qty=int(input('Nhập số lượng: '))
Price=int(input('Nhập đơn giá: '))
Sale=Qty*Price
print('Thành tiền: {:,}'.format(Sale))
Promo=0
if Sale>130000:
    Promo=Sale*0.1
print('Khuyến mãi: {:,}'.format(Promo))
print('Thanh toán: {:,}'.format(Sale-Promo))
