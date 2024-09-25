while True:
    try:
        u_nums = input("Введите числа через пробел: ")
        nums = [int(num) for num in u_nums.split()]
        break
    except ValueError:
        print("Нужно ввести числа через пробел.")
e_nums = []

for n in nums:
    if n % 2 == 0:
        e_nums.append(n)

print("Чётные числа:", e_nums)


slovo = input('Введите слово: ')

slovo = slovo.replace(" ", "").lower()

if slovo == slovo[::-1]:
    print('"'+slovo.upper()+'" является палиндромом.')
else:
    print('"'+slovo.upper()+'" не является палиндромом.')

def f_summa(n):
    r = []
    for i in range(0, len(n) - 1, 2):
        summa = n[i] + n[i + 1]
        r.append(summa)
    return r

while True:
    try:
        u_inp = input("Введите числа через пробел: ")
        spisok = [int(num) for num in u_inp.split()]
        resultat = f_summa(spisok)
        print('Сумма пар чисел: ' + str(resultat))
        break
    except ValueError:
        print("Нужно ввести числа через пробел.")