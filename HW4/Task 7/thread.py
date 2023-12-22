import threading
import time
import random

num_list = [random.randint(1, 100) for _ in range(1_000_000)]
results = 0


def sum_list(start, end):
    global results
    for i in num_list[start:end]:
        results += i


if __name__ == '__main__':
    start_time = time.time()
    threads = []

    for i in range(4):
        start = i * len(num_list) // 4
        end = (i + 1) * len(num_list) // 4
        print(f"Поток {i+1} работает с {start} по {end} элемент")
        t = threading.Thread(target=sum_list, args=(start, end))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Все потоки завершили работу за {time.time()- start_time} секунд")

    print(f"Сумма элементов массива: {results}")
