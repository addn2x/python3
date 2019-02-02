# 6 / 5 = 1.2 -> float vs 6 // 5 = 1 -> int 

a = 6 / 5
b = 6 // 5

print(a, type(a))
print(b, type(b))
print()                                 

# Given price transform into banknotes 
# (500, 200, 100, 50, 20, 10, 5, 2, 1)

fifty_bill = 50
twenty_bill = 20
ten_bill = 10
five_bill = 5
two_bill = 2
one_bill = 1

price = 150

print(' Given price is: ', price)

fifty = price // fifty_bill
price = price % fifty_bill

twenty = price // twenty_bill
price = price % twenty_bill

ten = price // ten_bill
price = price % ten_bill

five = price // five_bill
price = price % five_bill

two = price // two_bill
price = price % two_bill

one = price // one_bill
price = price % one_bill

print('50: ', fifty, type(fifty))
print('20: ', twenty, type(twenty))
print('10: ', ten, type(ten))
print('5: ', five, type(five))
print('2: ', two, type(two))
print('1: ', one, type(one))

