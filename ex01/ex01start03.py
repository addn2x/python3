#   convert degrees in celsius to dregrees feirenheit
#   Tf = Tc x 9/5 + 32
#   and other way around
#   Tc = (Tf - 32) x 5/9

nine_fifts = 9.0 / 5.0
five_ninths = 1 / nine_fifts
tt = 32

given_feirenheit = 11.0
given_celsius = 32.0

feirenheit = given_celsius * nine_fifts + float(tt)
celsius = (given_feirenheit - float(tt)) * five_ninths

print ('Given C(', given_celsius, ') is F(', feirenheit, ')')
print ('Given F(', given_feirenheit, ') is C(', celsius, ')')

print ('Given F(', given_feirenheit, ') is C(', int(celsius), ')')
print ('Given F(', given_feirenheit, ') is C(', round(celsius), ')')
print ('Given F(', given_feirenheit, ') is C(', round(celsius, 3), ')')

# int(), math.trunc(), round() 