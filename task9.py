# 9. Напишите функцию где вводится нормализованный
# текст, который кроме слов может содержать определенные
# знаки препинания. Распечатать текст без знаков
# припинания, то есть удалить все знаки препинания.
# Примечание. Под нормализованнымтекстом будем понимать текст, в котором
# пробел ставится после знаков препинания, за исключением открывающей
# скобки (пробел перед ней).
def text(list_):
    new_list = list_#.split()
    for i in new_list:
        for j in i:
            if j == "!" or j == "," or j == "." or j == "-" or j =="(" or j ==")":
                new_list = new_list.replace(j, "")
    return new_list

print(text("sdv !b! , ."))
