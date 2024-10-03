day = int(input("Введите день: ")) # ввод числа "дня" с клавиатуры 
month = int(input("Введите месяц: ")) # ввод числа "месяца" с клавиатуры 
if (day < 1 or month <1):
    print("Неверная дата")
else:
  if (month == 3 and day >= 1) or (month == 4) or (month == 5) or (month == 6 and day <= 31): # оператор ветвления if-elif-else
    season = "Весна" # сезон в соответстивии с условием 
  elif (month == 6 and day >= 1) or (month == 7) or (month == 8) or (month == 8 and day <= 31): # оператор ветвления if-elif-else
    season = "Лето" # сезон в соответстивии с условием 
  elif (month == 9 and day >= 1) or (month == 10) or (month == 11 and day <= 30): # оператор ветвления if-elif-else
    season = "Осень" # сезон в соответстивии с условием 
  else: # оператор ветвления if-elif-else
    season = "Зима" # сезон в соответстивии с условием 

  print(f"Дата {day}.{month} относится к сезону: {season}") # вывод даты с обозначением сезона
