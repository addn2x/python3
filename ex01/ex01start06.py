#         on a chessboard (8x8)
#             - row: up -> down
#             - column: left -> right
#         determin if:
#             a) two fields are same color
#             b) the queen attacks given field
#             c) the knight attacks given field


y1 = 3
x1 = 3

y2 = 5
x2 = 5

y = abs(y1 - y2)
x = abs(x1 - x2)

field = (y % 2 == 0) and (x % 2 == 0)
queen = (y1 == y2) or (x1 == x2) or (y == x)
knight = (y % 2 == 1 and x % 2 == 0) or (y % 2 == 0 and x % 2 == 1)

print ('two fields are the same color: ', field)
print ('the queen attacks given field: ', queen)
print ('the knight attacks given field: ', knight)
