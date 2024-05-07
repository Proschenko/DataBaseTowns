# Мужские фио
# n1=[]
# n2=[]
# n3=[]
#
# file = open('Мужские ФИО.txt','r', encoding="utf-8")
#
# lines = [[x.rstrip('\n')] for x in file]
#
# for i in range(len(lines)):
#     tmp=lines[i][0].split(" ")
#     n1.append(tmp[0])
#     n2.append(tmp[1])
#     n3.append(tmp[2])
#
# n1=list(set(n1))
# n2=list(set(n2))
# n3=list(set(n3))
# n1.sort()
# n2.sort()
# n3.sort()
# file1=open('Мужские Фамилии.txt','w',encoding="utf-8")
# file2=open('Мужские Имена.txt','w',encoding="utf-8")
# file3=open('Мужские Отчества.txt','w',encoding="utf-8")
#
# for i in range(len(n1)):
#     tmp1=n1[i]+"\n"
#     tmp2=n2[i]+"\n"
#     tmp3=n3[i]+"\n"
#     file1.writelines(tmp1)
#     file2.writelines(tmp2)
#     file3.writelines(tmp3)
#
# file.close()
# file1.close()
# file2.close()
# file3.close()

# Женские фио
# n1 = []
# n2 = []
# n3 = []
#
# file = open('Женские ФИО.txt', 'r', encoding="utf-8")
# lines = [x.rstrip('\n') for x in file]
# for i in range(len(lines)):
#     tmp = lines[i].split(" ")
#     n1.append(str(tmp[0]))
#     n2.append(str(tmp[1]))
#     n3.append(str(tmp[2]))
#
#
# n1.sort()
# n2.sort()
# n3.sort()
#
#
#
# file1 = open('Женские Фамилии.txt', 'w', encoding="utf-8")
# file2 = open('Женские Имена.txt', 'w', encoding="utf-8")
# file3 = open('Женские Отчества.txt', 'w', encoding="utf-8")
#
# for i in range(len(n1)):
#     tmp1 = n1[i] + "\n"
#     file1.writelines(tmp1)
# for i in range(len(n2)):
#     tmp2 = n2[i] + "\n"
#     file2.writelines(tmp2)
# for i in range(len(n3)):
#     tmp3 = n3[i] + "\n"
#     file3.writelines(tmp3)
#
# file.close()
# file1.close()
# file2.close()
# file3.close()
import csv
import random

#encoding_value ='utf-8'

encoding_value='utf-8-sig'

def region_generator():
    regions = ["Тюменская область"]
    region_index = ["72"]
    result_region = []
    for i in range(len(regions)):
        result_region.append([str(region_index[i]), str(regions[i])])
    with open("Area.csv", mode="w" ) as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        # file_writer.writerow(["Ключ", "Область"])
        file_writer.writerow(["subject_code", "name_area"])

        for j in range(len(result_region)):
            file_writer.writerow(result_region[j])

    print("Данные о регионах в Area.csv")


def town_generator():
    towns = ["Тюмень"]
    postal_code = ["625000"]
    result_town = []
    for i in range(len(towns)):
        result_town.append([str(i + 1), str(towns[i]), str(postal_code[i]), str(72)])

    with open("City.csv", mode="w" ) as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        # file_writer.writerow(["Ключ", "Область", "Почтовый индекс", "Ссылка"])
        file_writer.writerow(["id_city", "name_city", "postal_code", "area_id"])

        for j in range(len(result_town)):
            file_writer.writerow(result_town[j])

    print("Данные о городах в City.csv")


def area_streets_generator():
    file = open('Районы +улицы Тюмени.txt', 'r', encoding="utf-8")
    lines = [x.rstrip('\n') for x in file]
    result_area = []
    result_street = []
    for i in range(len(lines)):
        tmp = lines[i].split(",")
        result_area.append([str(i + 1), tmp[0], str(1)])

        for j in range(1, len(tmp)):
            result_street.append([str(i + 1), tmp[j]])  # костыль

    with open("District.csv", mode="w" ) as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        # file_writer.writerow(["Ключ", "Район", "Ссылка"])
        file_writer.writerow(["id_district", "name_district", "city_id"])

        for j in range(len(result_area)):
            file_writer.writerow(result_area[j])

    print("Данные о районах в District.csv")

    for i in range(len(result_street)):
        result_street[i].append(str(i + 1))
        result_street[i].reverse()

    with open("Street.csv", mode="w" ) as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        # file_writer.writerow(["Ключ", "улица", "Ссылка"])
        file_writer.writerow(["id_street", "name_street", "district_id"])

        for j in range(len(result_street)):
            file_writer.writerow(result_street[j])

    print("Данные об улицах в Street.csv")


def house_generator(count):
    n = count
    result_house = []
    floor_count = [5, 9, 15, 21]
    for i in range(n):
        result_house.append([str(i + 1),
                             str(random.randint(1, 40)),
                             str(random.randint(1970, 2015)),
                             str(random.choice(floor_count)),
                             str(random.randint(1, max_index_street))])
    # Проверка на одинаковые дома относящиеся к одной и той же улице(исключение повторений)
    skip_index = []
    for i in range(len(result_house)):
        for j in range(i + 1, len(result_house)):
            if result_house[j][2] == result_house[i][2] and result_house[i][4] == result_house[j][4]:
                skip_index.append(i)

    with open("Residential_Building.csv", mode="w" ) as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        # file_writer.writerow(["Ключ", "Номер дома", "Год постройки", "Количество этажей", "Ссылка"])
        file_writer.writerow(["id_residential_building", "house_number", "year_of_construction", "numbers_of_floors", "street_id"])

        for j in range(len(result_house)):
            # if j in skip_index:
            #     continue
            file_writer.writerow(result_house[j])

    print("Данные о домах в Residential_Building.csv")
    return len(skip_index)


def flat_generator(count):
    n = count
    result_flat = []
    room_count = [1, 2, 3, 4]
    for i in range(n):
        result_flat.append([str(i + 1),
                            str(random.randint(1, 100)),
                            str(random.choice(room_count)),
                            str(float(random.randint(250, 1000) / 10)),
                            str(random.randint(1, max_index_house))])
    # Проверка на одинаковые квартиры относящиеся к одному и тому же дома(исключение повторений)
    skip_index = []
    for i in range(len(result_flat)):
        for j in range(i + 1, len(result_flat)):
            if result_flat[j][3] == result_flat[i][3] and result_flat[i][4] == result_flat[j][4]:
                skip_index.append(i)

    with open("Apartment.csv", mode="w" ) as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        # file_writer.writerow(["Ключ", "Номер квартиры", "Количество комнат", "Площадь", "Ссылка"])
        file_writer.writerow(["id_apartment", "apartment_number", "num_of_rooms", "area", "residential_building_id"])

        for j in range(len(result_flat)):
            # if j in skip_index:
            #     continue
            file_writer.writerow(result_flat[j])

    print("Данные об квартирах в Apartment.csv")
    return len(skip_index)


def people_generator(count):
    def phone_number_generator(count_numbers):
        result = []

        while len(result) < count_numbers:
            phone_number = "+7"
            for j in range(10):
                phone_number += str(random.randrange(0, 10))
            result.append(phone_number)
            result = list(set(result))
        return result

    def name_generator(choice_inner):
        if choice_inner:
            return str(random.choice(m_name1) + " " + random.choice(m_name2) + " " + random.choice(m_name3))
        else:
            return str(random.choice(f_name1) + " " + random.choice(f_name2) + " " + random.choice(f_name3))

    n = count

    # Заполнение массивов фио
    file1 = open('Мужские Фамилии.txt', 'r', encoding="utf-8")
    file2 = open('Мужские Имена.txt', 'r', encoding="utf-8")
    file3 = open('Мужские Отчества.txt', 'r', encoding="utf-8")
    m_name1 = [x.rstrip('\n') for x in file1]
    m_name2 = [x.rstrip('\n') for x in file2]
    m_name3 = [x.rstrip('\n') for x in file3]
    file1.close()
    file2.close()
    file3.close()

    file1 = open('Женские Фамилии.txt', 'r', encoding="utf-8")
    file2 = open('Женские Имена.txt', 'r', encoding="utf-8")
    file3 = open('Женские Отчества.txt', 'r', encoding="utf-8")
    f_name1 = [x.rstrip('\n') for x in file1]
    f_name2 = [x.rstrip('\n') for x in file2]
    f_name3 = [x.rstrip('\n') for x in file3]
    file1.close()
    file2.close()
    file3.close()

    month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    start_passport = 3020100000  # Серия (4) + номер(6)

    phone_numbers = phone_number_generator(n)

    result_people = []
    for i in range(0, n):
        month = str(random.randrange(1, 12 + 1))
        if len(month) == 1:
            month = "0" + month

        day = str(random.randrange(1, month_day[int(month) - 1]))
        if len(day) == 1:
            day = "0" + day
        year = str(random.randrange(1950, 2005))

        start_passport += 1
        choice = random.choice([True, False])
        name = name_generator(choice)

        result_people.append([str(i + 1),
                              str(name),
                              str(start_passport),
                              str(phone_numbers[i]),
                              str(str(year) + '-' + str(month) + '-' + str(day)),
                              str(int(choice)),
                              str(random.randint(1, max_index_flat))])

    # Данные из двумерного списка в csv
    with open("Citizen.csv", mode="w" ) as w_file:
        file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
        #file_writer.writerow(["Ключ", "Имя", "Паспорт", "Телефон", "Дата рождения", "Пол", "Ссылка"])
        file_writer.writerow(["id_citizen", "full_name", "passport_data", "phone_number", "date_of_birth", "gender", "apartment_id"])
        for j in range(len(result_people)):
            file_writer.writerow(result_people[j])

    print("Данные о людях в Citizen.csv")


max_index_region = 1
max_index_tow = 1
max_index_street = 46
max_index_house = 100
max_index_flat = 100
max_index_people = 300

region_generator()
town_generator()
area_streets_generator()

house_generator(max_index_house)  # Можно менять значение
flat_generator(max_index_flat)  # Можно менять значение

people_generator(max_index_people)  # Можно менять значение

print("Домов:", max_index_house)
print("Квартир:", max_index_flat)
print("Людей:", max_index_people)
