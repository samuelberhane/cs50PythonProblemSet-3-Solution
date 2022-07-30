while True:
    fuel = input('Fraction: ')
    try:
        x,y = fuel.split('/')
        x_num = int(x)
        y_num = int(y)
        fuel_num = x_num / y_num
        if fuel_num <= 1:
            break
    except:
        pass
percentage = round(fuel_num * 100)
if percentage <= 1:
    print('E')
elif percentage >= 99:
    print('F')
else:
    print(f"{percentage}%")