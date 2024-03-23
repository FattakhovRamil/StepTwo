import requests
import sqlite3
import time

def getRequest(jsonObj):
    url = 'http://localhost:3001/api/getstate'
    response = requests.get(url, json=jsonObj)
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print("Error:", response.status_code)
    

def postRequest(jsonObj):
    url = 'http://localhost:3001/api/savestate'
    response = requests.post(url, json=jsonObj)
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print("Error:", response.status_code)
    

def dataBasePrint():
    print("База данных:")
    conn = sqlite3.connect('../gopher.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    for row in rows:    
        print(row)
    cursor.close()
    conn.close()

get_data_1 = {
    "application": "first-client",
}

get_data_2 = {
    "application": "second-client",
}

post_data_1 = { 
    "application": "first-client",
    "param1": 10,
    "param2": "abc"
}

post_data_2 = { 
    "application": "second-client",
    "param1": 20,
    "param2": "def"
}

post_data_2_2 = { 
    "application": "second-client",
    "param1": 30,
    "param2": "ghi"
}

post_data_2_3 = { 
    "application": "second-client",
    "param1": 31,
    "param2": "ghi"
}

time_sleep = 2

print("Для начала проверим POST запрос по адресу http://localhost:3001/api/savestate как в примере")
time.sleep(time_sleep)
print("Сохраним в базу данные 1-го клиента first-client")
time.sleep(time_sleep)
print({ 
    "application": "first-client",
    "param1": 10,
    "param2": "abc"
})
time.sleep(time_sleep)
postRequest(post_data_1)
time.sleep(time_sleep)
dataBasePrint()
time.sleep(time_sleep)

print("Запись появилась в БД")
time.sleep(time_sleep)
print("Вставим данные 2-го клиента")
time.sleep(time_sleep)
print({ 
    "application": "second-client",
    "param1": 20,
    "param2": "def"
})
time.sleep(time_sleep)
postRequest(post_data_2)
time.sleep(time_sleep)
dataBasePrint()
time.sleep(time_sleep)

print("Клиент 1 идёт получать свой статус first-client:")
time.sleep(time_sleep)
print("Проводим GET запрос по адресу http://localhost:3001/api/getstate и получаем текущую версию 1")
time.sleep(time_sleep)
getRequest(get_data_1)
time.sleep(time_sleep)
print("Клиент 2 делает запрос для своего статуса second-client:")
time.sleep(time_sleep)
getRequest(get_data_2)
time.sleep(time_sleep)


print("Теперь, если мы сохраняем изменяем значение у клиента через api/savestate, у нас \n номер версии должен измениться (увеличиться на 1 после каждого \n изменения или неизменяться, если мы сохраняем точно такие же параметры). Т.е. после")
time.sleep(time_sleep)
postRequest(post_data_2_2)
time.sleep(time_sleep)
dataBasePrint()
time.sleep(time_sleep)
print("Версия увеличилась на 1")
time.sleep(time_sleep)
print("При запросе 2-го клиента, версия не изменится")
time.sleep(time_sleep)
getRequest(get_data_2)
time.sleep(time_sleep)
dataBasePrint()
time.sleep(time_sleep)

print("А при изменении любого другого параметра, увеличиться:")
time.sleep(time_sleep)
postRequest(post_data_2_3)
time.sleep(time_sleep)
getRequest(get_data_2)
time.sleep(time_sleep)
dataBasePrint()
time.sleep(time_sleep)
print("Программа отрабатывает корректно, согласно ТЗ. Спасибо за внимание :)")