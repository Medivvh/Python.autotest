json = {
    "state": 0,
    "data": [
        {
            "_id": "3d8c861f-e2c0-442a-9d82-810ae5eb5f52",
            "count": 1,   # попробовать поменять на 1, 0, -1
            "brand_id": 84375,
            "delay": 1,
            "startedAt": "2024-03-21T16:48:03.513Z",
            "completedAt": "2024-03-21T16:48:03.513Z",
            "completed": 0,
            "wait_refund": 0,
            "refunded": 0
        },
        {
            "_id": "4816385b-a5a5-4341-aedf-6f80bedbdce4",
            "count": 2,     # попробовать поменять на 2, 0, -6
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
            "count": 16,   # попробовать поменять на 16, 0, -6
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

# count - кол-во услуг всего в заказе
# completed/wait_refund/refunded - статусы обработанных услуг в конкретном заказе.
# Если значение 0 - значит нет услуг в этом заказе подходящее под этот статус-то есть
# услуга может быть выполненной, возвращенной или ожидающей возврата`
# delay - кол-во часов между выполнениями услуг


'''#1 Надо убедиться, что заказы вообще есть в ответе от сервера'''


order_1 = json['data'][0]
order_2 = json['data'][1]
order_3 = json['data'][2]

count_of_order1 = order_1['count']
count_of_order2 = order_2['count']
count_of_order3 = order_3['count']

inc_req = [count_of_order1 + count_of_order2 + count_of_order3]

def sum_count(counts):
    for count in counts:
        if count > 0:
            print(f'Количество услуг в заказах: {count}')
        elif count == 0:
            print(f'Количество услуг в заказе = {count} , ожидаем заказы')
        else:
            print(f'Количество услуг в заказе не может быть отрицательным = {count} ')
sum_count(inc_req)



'''#2 Надо убедиться, что время выполнение первого и второго заказов не превышает 6 часов'''
