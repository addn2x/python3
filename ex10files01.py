
my_file_name = 'my_text.txt'
my_file = open(my_file_name, 'r')
# lorem_ipsum = my_file.read()
lorem_ipsum = my_file.readlines()
print(lorem_ipsum)
my_file.close()

wfile = 'writitng_file.txt'
wf = open(wfile, 'w')
while True:
    text = input('Enter text (end with blank): ')
    if len(text) == 0:
        break
    else:
        wf.write(text + ' \n')
wf.close()