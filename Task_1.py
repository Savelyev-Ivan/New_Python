
#number = input("Напишите число: ")
#rezult = int(number) + 2
#print(rezult)

#number = int(input("Напишите число:"))
#if int(number) <= 10:
#    new_number = number ** 2
#    print(new_number)
#else:
#    print("Введите другое число")


while True:
    number = int(input("Напишите число:"))
    if number > 0 and number < 10:
         print(number**2)
         break
    else:
        print("Введите другое число")
