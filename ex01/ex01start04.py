# bool -> True / False
# and / or / not operators

p = False
q = True

print('true', p)
print('false', q)
print()

result_a = p and q
result_b = p or q
not_p = not p
not_q = not q

print('p and q ', result_a)
print('p or q ', result_b)
print('not p ',not_p)
print('not q ', not_q)

my_implication = (not p) or q
print('implication ', my_implication)