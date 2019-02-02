#   convert dollars to franks provided that
#   1 dollar is 80 eur and
#   1 frank is 100 eur

dollar = 80
frank = 100

inputDollar = 3
inputFrank = 5

outputFrank = (float(inputDollar) * float(dollar)) / float(frank)
outputDollar = (float(inputFrank) * float(frank)) / float(dollar)

print ('Given dollar ', inputDollar, ' is ', outputFrank, ' franks')
print ('Given franks ', inputFrank, ' is ', outputDollar,' dollars')
print ('Given franks ', inputFrank, ' is ', round(outputDollar),' dollars')
print ('Given franks ', inputFrank, ' is ', round(outputDollar, 1),' dollars')