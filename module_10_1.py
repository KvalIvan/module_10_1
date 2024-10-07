from datetime import datetime
from threading import Thread
from time import sleep


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for number in range(1, word_count + 1):
            file.write(f'Какое-то слово № {number}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


first_time = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

second_time = datetime.now()
res_time = second_time - first_time
print(res_time)

third_time = datetime.now()

first_flow = Thread(target=write_words, args=(10, 'example5.txt'))
second_flow = Thread(target=write_words, args=(30, 'example6.txt'))
third_flow = Thread(target=write_words, args=(200, 'example7.txt'))
fourth_flow = Thread(target=write_words, args=(100, 'example8.txt'))

first_flow.start()
second_flow.start()
third_flow.start()
fourth_flow.start()


first_flow.join()
second_flow.join()
third_flow.join()
fourth_flow.join()

fourth_time = datetime.now()
res_time2 = fourth_time - third_time
print(res_time2)
