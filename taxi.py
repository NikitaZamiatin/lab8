N = int(input("Введите натуральное число N от 1 до 1000, равное количеству сотрудников компании: "))

distances = list(map(int, input("Введите N положительных целых чисел, задающих расстояния в километрах от работы до домов сотрудников компании: ").split()))

tariffs = list(map(int, input("Далее еще N положительных целых чисел чисел — тарифы в рублях за проезд одного километра в такси").split()))

employees = [(i+1, distances[i]) for i in range(N)]
employees.sort(key=lambda x: x[1])

taxis = [(i+1, tariffs[i]) for i in range(N)]
taxis.sort(key=lambda x: x[1])

result = [(employee[0], 1) for employee in employees]

for i in range(N):
    min_taxi = result[i][1]
    for j in range(i+1, N):
        if result[j][1] < min_taxi:
            result[j] = (result[j][0], min_taxi)
    
total_cost = 0
for i in range(N):
    total_cost += employees[i][1] * taxis[result[i][1]-1][1]