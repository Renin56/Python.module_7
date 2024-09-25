def custom_write(file_name, strings):
    strings_position = {}
    index = 0

    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        strings_position[index + 1, file.tell()] = string
        file.write(string + '\n')
        index += 1
    file.close()
    return strings_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
