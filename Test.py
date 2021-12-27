ticket = int(input("Сколько нужно билетов? "))
total_price = 0
for i in range(ticket):
    age = int(input("Возраст посетителя - "))
    if 18 <= age < 25:
        total_price += 990
    elif age >= 25:
        total_price += 1390
if ticket > 3:
        total_price *= 0.9
print("Итоговая сумма - ", total_price)