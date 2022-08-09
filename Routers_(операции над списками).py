### Программа Routers демонстрироует операции над списками: ###
                        # Добавление и удаление элементов;
                        # Вывод списка;
                        # Сортировка списка;
                        # Поиск элемента в списке.
###############################################################

routers = []

print("*" * 10, " Routers v.0.0.1 ", "*" * 10)

response = 1
while response:
    print("""Выберите действие:
            1 - Добавить маршрутизатор
            2 - Удалить маршрутизатор
            3 - Вывести список маршрутизаторов
            4 - Поиск
            5 - Сортировка
            0 - выход""")
    response = int(input(">> "))
    if response == 1:
        router = input("Новый маршрутизатор: ")
        routers.append(router)
    elif response == 2:
        router = input("Удалить маршрутизатор: ")
        routers.remove(router)
    elif response == 3:
        print(routers)
    elif response == 4:
        router = input("Поиск: ")
        if router in routers:
            print("Такой маршрутизатор уже есть! ")
        else:
            print("Такого маршрутизатора нет в списке! ")
    elif response == 5:
        routers.sort()
        print("Отсортировано! ")
    else:
        print("Досвидания! ")

####################################### English Version #############################################################

routers = []

print("*" * 10, " Routers v.0.0.1 ", "*" * 10)

response = 1
while response:
    print("""Select an action:
            1 - Add a router
            2 - Remove the router
            3 - Display a list of routers
            4 - Search
            5 - Sorting
            0 - exit""")
    response = int(input(">> "))
    if response == 1:
        router = input("New Router: ")
        routers.append(router)
    elif response == 2:
        router = input("Remove the router: ")
        routers.remove(router)
    elif response == 3:
        print(routers)
    elif response == 4:
        router = input("Search: ")
        if router in routers:
            print("There is already such a router! ")
        else:
            print("There is no such router in the list! ")
    elif response == 5:
        routers.sort()
        print("Sorted! ")
    else:
        print("Goodbye! ")
