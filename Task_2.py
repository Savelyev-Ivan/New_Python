#Пользователь вводит время в секундах.
#Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
#Используйте форматирование строк.
t = int(input("Введите время в секундах : "))
h = t // 3600
m = t // 60 - h * 60
s = t % 60
print(f"{h:02}:{m:02}:{s:02}")