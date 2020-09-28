groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика","ЭЭиС","Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "ИКГ"],
        "marks": [3, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "История", "ИКГ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Виктор",
        "surname": "Миронов",
        "exams": ["Философия", "ИНО", "ИКГ"],
        "marks": [5, 3, 4]
    },
    {
        "name": "Андрей",
        "surname": "Соколов",
        "exams": ["АиГ", "История", "ИНО"],
        "marks": [5, 4, 5]
    }
]

def filter_students(students, middle):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(35), u"Оценки".ljust(20), u"Средний балл".ljust(15))
    for student in students:
        sum = 0
        for mark in student["marks"]:
            sum += mark
        average = sum / len(student["marks"])
        if (round(average, 2) > middle):
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(35), str(student["marks"]).ljust(20), str(round(average, 2)).ljust(15))

mid = float(input("Введите средний балл: "))

filter_students(groupmates, mid)
