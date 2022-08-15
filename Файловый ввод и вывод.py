# Запись строки в файл
f = open("somefile.txt", "w", encoding="utf-8")
f.write("String")
f.close()

# Запись нескольких строк
a = open("test.txt", "w", encoding="utf-8")
a.writelines(["String1 \n", "String2 \n", "String3"])
a.flush()
a.close()

# Чтение из файла
print("** Построчное чтение всего файла:")
txt = open("test.txt", "r", encoding='utf-8')
for line in txt:
    print(line)
txt.close()