strings_positions = {}
str_num = 0


def custom_write(file_name, strings):
    global str_num
    for i in strings:
        file = open(file_name, 'a', encoding='utf-8')
        str_num += 1
        strings_positions.update({(str_num, file.tell()): i})
        file.write(f'{i}\n')
        file.close()
    return strings_positions


spisok = ['Text for tell.', '1234', 'Камчатка', 'bye']
result = custom_write('example2.txt', spisok)

for elem in result.items():
    print(elem)
