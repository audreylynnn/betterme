alice,bob,carol=eval(input('Nhập số kẹo của Alice, Bob, Carol: '))
tongkeo=alice+bob+carol
print('Cần hủy {} cái kẹo để chia đều cho 3 bạn'.format(tongkeo%3))
