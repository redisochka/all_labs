password = input('Введите пароль:')

numeric = False
upper = False
lower = False
spec = False

for char in password:
    if char.isnumeric():
        numeric = True
    elif char.islower():
        lower = True
    elif char.isupper():
        upper = True
    elif char in "@#%&":
        spec = True

if len(password) > 4 and numeric and upper and lower and spec:
    print('Good job man')
else:
    print('Too bad...')

