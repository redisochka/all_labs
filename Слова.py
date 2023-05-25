a = 1
c = ''
while a == 1:
    b = input('Вводите слова сколько хотите, когда надоест напиши "stop"')
    c = c + " " + b
    if b == "stop":
        a += 1
        d = c[0:-5]
print(d)
