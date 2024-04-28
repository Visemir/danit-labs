import requests
import json

# Базовий URL вашого Flask-сервера
base_url = "http://127.0.0.1:5000/"

# Файл для запису результатів
results_file = "results.txt"

# Функція для запису результатів до файлу
def log_result(data):
    with open(results_file, "a") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
        
        



# Крок 1: Отримати всіх існуючих студентів (GET)
response = requests.get(f"{base_url}/students")
log_result("Отримання всіх існуючих студентів:")
log_result(response.json())
print("Отримання всіх існуючих студентів: \n", json.dumps(response.json(), ensure_ascii=False, indent=2))

# Крок 2: Створити трьох студентів (POST)
students_data = [
    {"first_name": "Ivan", "last_name": "Ivanov", "age": 21},
    {"first_name": "Petro", "last_name": "Petrov", "age": 22},
    {"first_name": "Svitlana", "last_name": "Shevchenko", "age": 20},
]

for student in students_data:
    response = requests.post(f"{base_url}/students/new", json=student)
    log_result("Створення студента:")
    log_result(response.json())
    print("Створення студента: \n", json.dumps(response.json(), ensure_ascii=False, indent=2))

# Крок 3: Отримати всіх студентів після додавання (GET)
response = requests.get(f"{base_url}/students")
log_result("Отримання всіх студентів після додавання:")
log_result(response.json())
print("Отримання всіх студентів після додавання: \n", json.dumps(response.json(), ensure_ascii=False, indent=2))

# Крок 4: Оновити вік другого студента (PATCH)
update_age_data = {"age": 23}
response = requests.patch(f"{base_url}/students/ageupdate/2", json=update_age_data)
log_result("Оновлення віку другого студента: ")
log_result(response.json())
print("Оновлення віку другого студента: \n", json.dumps(response.json(), ensure_ascii=False, indent=2))

# Крок 5: Отримати інформацію про другого студента (GET)
response = requests.get(f"{base_url}/students/2")
log_result("Інформація про другого студента: ")
log_result(response.json())
print("Інформація про другого студента: \n", json.dumps(response.json(), ensure_ascii=False, indent=2))

# Крок 6: Оновити ім'я та прізвище третього студента (PUT)
update_name_data = {"first_name": "Tretiy", "last_name": "Student", "age": 20}
response = requests.put(f"{base_url}/students/update/3", json=update_name_data)
log_result("Оновлення третього студента:")
log_result(response.json())
print("Оновлення третього студента: \n", json.dumps(response.json(), ensure_ascii=False, indent=2))

# Крок 7: Отримати інформацію про третього студента (GET)
response = requests.get(f"{base_url}/students/3")
log_result("Інформація про третього студента :")
log_result(response.json())
print("Інформація про третьго студента : \n", json.dumps(response.json(), ensure_ascii=False, indent=2))

# Крок 8: Отримати всіх студентів (GET)
response = requests.get(f"{base_url}/students")
log_result("Отримання всіх студентів після оновлень:")
log_result(response.json())
print("Отримання всіх студентів після оновлень: \n", json.dumps(response.json(), ensure_ascii=False, indent=2))

# Крок 9: Видалити першого студента (DELETE)
response = requests.delete(f"{base_url}/delete/1")
log_result("Видалення першого студента:")
log_result(response.json())
print("Видалення першого студента: \n", json.dumps(response.json(), ensure_ascii=False, indent=2))

# Крок 10: Отримати всіх студентів після видалення (GET)
response = requests.get(f"{base_url}/students")
log_result("Отримання всіх студентів після видалення: ")
log_result(response.json())
print("Отримання всіх студентів після видалення: \n", json.dumps(response.json(), ensure_ascii=False, indent=2))


