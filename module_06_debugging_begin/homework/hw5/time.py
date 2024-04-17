import datetime


with open('logger.txt', 'r') as file:
    log_data = file. readlines()
odd_data = []
even_data = []
for key in range(30):
    if key % 2 != 0:
        odd_data.append(log_data[key].rstrip())
    else:
        even_data.append((log_data[key]).rstrip())

zipped_data = list(zip(odd_data, even_data))

data_list = []
for value in zipped_data:
    obj_time = datetime.datetime.strptime(value[0][:9], "%M:%S.%f")
    obj_time2 = datetime.datetime.strptime(value[1][:9], "%M:%S.%f")
    result = obj_time - obj_time2
    data_list.append(result.microseconds / 1000)
average_time = sum(data_list) / 15

print(f"Среднее время выполнения функции measure_me: {round(average_time, 2)} миллисекунд")