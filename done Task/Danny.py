from datetime import datetime

json = {
    "state": 0,
    "data": [
        {
            "_id": "3d8c861f-e2c0-442a-9d82-810ae5eb5f52",
            "count": 1,  # попробовать поменять на 1, 0, -1
            "brand_id": 84375,
            "delay": 1,
            "startedAt": "2024-03-21T16:48:03.513Z",
            "completedAt": "2024-03-21T16:48:03.513Z", #поменять на "2024-03-21T22:48:03.513Z"
            "completed": 0,
            "wait_refund": 0,
            "refunded": 0
        },
        {
            "_id": "4816385b-a5a5-4341-aedf-6f80bedbdce4",
            "count": 2,  # попробовать поменять на 2, 0, -6
            "brand_id": 88339,
            "delay": 2,
            "startedAt": "2024-03-21T16:27:32.062Z",
            "completedAt": "2024-03-21T16:28:32.062Z",
            "completed": 0,
            "wait_refund": 2,
            "refunded": 0
        },
        {
            "_id": "7e0882b5-38b8-4dcb-9825-625158a92314",
            "count": 16,  # попробовать поменять на 16, 0, -6
            "brand_id": 88339,
            "delay": 3,
            "startedAt": "2024-03-21T16:17:04.723Z",
            "completedAt": "2024-03-21T16:17:04.723Z",
            "completed": 7,
            "wait_refund": 3,
            "refunded": 6
        }
    ]
}


class Account:
    def __init__(self, name, mail):
        self._name = name
        self._mail = mail

    def show_account(self):
        print(f'name: {self._name}, mail: {self._mail}')

operator = Account('Danil', 'DVW@mail.ru')

'''#1 Надо убедиться, что заказы вообще есть в ответе от сервера'''

assert json['data'] is not None and len(json['data']) > 0, f'Заказов нет'

'''#2 Надо убедиться, что время выполнение первого и второго заказов не превышает 6 часов'''

result_time = []
def count_by(json):
    for I in range(len(json['data'][0:2])):
        start = datetime.strptime(json["data"][I]["startedAt"], "%Y-%m-%dT%H:%M:%S.%fZ")
        end = datetime.strptime(json["data"][I]["completedAt"], "%Y-%m-%dT%H:%M:%S.%fZ")
        dif_time = (end - start).seconds
        result_time.append(dif_time)
count_by(json)

assert sum(result_time) <= 21600, f'Время выполнения заказов превышает 6 часов'

'''#3 Надо убедиться, что для третьего заказа все услуги обработаны 
И выполнено не меньше половины. 
Ну или по крайней мере на текущий момент возвращено не больше, чем выполнено, 
а ожидают возврат не больше, чем уже возвращено'''

completed_count = json['data'][2]['completed']
wait_refund_count = json['data'][2]['wait_refund']
refunded_count = json['data'][2]['refunded']
count = json['data'][2]['count']

assert ((completed_count + wait_refund_count + refunded_count == count and completed_count >= count / 2)
        or (refunded_count <= completed_count and not wait_refund_count > refunded_count))

'''Подготовь словарь, который будет содержать:
1. массив айдишников заказов
2. объект, который будет содержать в себе инфу о том, сколько всего услуг выполненных, возвращенных и ожидающих возврат 
3. Так же в самом начале программы сделай переменную под названием operator и положи в нее свою почту и имя. Эта информация должна быть в отчете. (мало ли кто другой воспользуется программой, чтобы ему было просто в самом начале задать свои почту и имя и они были в отчете)
 *. Имей в виду, надо сделать так, чтобы во время выполнения этой программы после объявления переменной не было возможности поменять данные этой переменной
4. Ну и последнее - я хочу немного приукрасить наш отчет. Сделай так, чтобы в массив с id добавился еще один id - вот такой  `326b23a1-e6ab-4b4a-84a1-a3ecb33afc97`'''

id_of_orders = []

for i in range(len(json['data'])):
    Id = json["data"][i]["_id"]
    id_of_orders.append(Id)

#сделать цикл для заказов

list_of_orders = {
    'completed': 0,
    'wait_refund': 0,
    'refunded': 0
}

for key in list_of_orders.keys():
    for obj in json['data']:
        list_of_orders[key] += obj[key]

orders = {'orders_id': id_of_orders,
          'orders_list': list_of_orders,
          }

operator.show_account()
id_of_orders += ['326b23a1-e6ab-4b4a-84a1-a3ecb33afc97']

print(orders)
