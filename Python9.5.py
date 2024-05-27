def calc_stat(listened):  # От англ. calculate statistics, посчитать статистику 
# Напишите код функции calc_stat() 
    N = len(listened) 
    amount = 0 
    for item in listened: 
        amount += item
        M = amount//60 # Деление нацело
    return (f'Вы прослушали {N} песен общей продолжительностью {M} минут.') 

print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))