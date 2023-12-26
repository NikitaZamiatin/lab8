import itertools

N = int(input("Введите натуральное число N от 1 до 1000, равное количеству сотрудников компании: "))
if N < 1:
    print("Число не может быть меньше одного!")
    exit()

distances = list(map(int, input("Введите N положительных целых чисел, задающих расстояния в километрах от работы до домов каждого сотрудника компании: ").split()))

tariffs = list(map(int, input("Далее еще N положительных целых чисел чисел — тарифы в рублях за проезд одного километра каждого из вызванных такси: ").split()))

n = len(distances) 
m = len(tariffs)  


permutations = list(itertools.permutations(range(1, n + 1))) # все возможные перестановки

total_cost = float('inf')  # минимальная стоимость
result_fin = None

for route in permutations:
    cost = 0

    for i in range(n): # стоимость для текущего маршрута
        driver = route[i] % m
        distance = distances[i]
        tariff = tariffs[driver]
        cost += distance * tariff

    if cost < total_cost:
        total_cost = cost
        result_fin = route

print(*result_fin)

print(total_cost)

def spell_out_number(number):
    words = ['рубль', 'рубля', 'рублей']
    remainder = number % 100
    if 11 <= remainder <= 19:
        return f"{number} {words[2]}"
    else:
        remainder = remainder % 10
        if remainder == 1:
            return f"{number} {words[0]}"
        elif remainder in [2, 3, 4]:
            return f"{number} {words[1]}"
        else:
            return f"{number} {words[2]}"

print(spell_out_number(total_cost))