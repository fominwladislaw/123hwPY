
def copy_line(source_file, target_file, line_number):

    # Открытие исходного файла для чтения

    with open(source_file, 'r') as file:

        lines = file.readlines()

    

    # Проверка корректности номера строки

    if line_number < 1 or line_number > len(lines):

        print('Некорректный номер строки')

        return

    

    # Открытие целевого файла для записи

    with open(target_file, 'w') as file:

        # Копирование выбранной строки в целевой файл

        file.write(lines[line_number - 1])

        

        # Запись оставшихся строк

        for i in range(len(lines)):

            if i != line_number - 1:

                file.write(lines[i])



    print('Копирование строки успешно выполнено')



# Пример 

source_file = 'source.txt'

target_file = 'target.txt'

line_number = int(input('Введите номер строки: '))



copy_line(source_file, target_file, line_number)