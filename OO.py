user_vibor = ""
chet1 = 100
chet2 = 200

while user_vibor != "7":


    print("Добро пожаловать в примитивный банкомат".upper())

    print("МЕНЮ\nВыберите действие:\n1. Баланс всего\n2. Баланс на первом счете\n3. Баланс на втором "
                     "счете\n4. Вывод средств\n5. Внесение средств\n6. Перенос средств между счетами\n7. Выход")
    print()

    user_vibor = input("Введите выбранный номер пункта - ")
    if user_vibor == "1":
        print("Всего средств на счетах - ", chet1 + chet2, "$")
    elif user_vibor == "2":
        print(f"Баланс на первом счете - {chet1}$")
    elif user_vibor == "3":
        print(f"Баланс на втором счете - {chet2}$")
    elif user_vibor == "4":
        user_vibor = input("С какого счета выводим средства, с первого или второго?")
        if user_vibor == "1":
            user_vibor = int(input("Сколько средств снимаем?"))
            if user_vibor <= chet1:
                print("Вы сняли", chet1 - user_vibor, "$, на балансе счета осталось - ", chet1- user_vibor,"$")
        elif user_vibor == "2":
            user_vibor = int(input("Сколько средств снимаем?"))
            if user_vibor <= chet2:
                print("Вы сняли", chet2 - user_vibor, "$, на балансе счета осталось - ", chet2 - user_vibor,"$")
    elif user_vibor == "5":
        user_vibor = input("На какой счет вносим деньги?")
        if user_vibor == "1":
            user_vibor = int(input("Сколько средств вводим? - "))
            print("Вы ввели на первый счет - ", user_vibor, "$, Баланс первого счета - ", user_vibor + chet1)
        elif user_vibor == "2":
            user_vibor = int(input("Сколько средств вводим? - "))
            print("Вы ввели на второй счет - ", user_vibor, "$, Баланс второго счета - ", user_vibor + chet2)
    elif user_vibor == "7":
        print("Выход из программы")
        exit()
