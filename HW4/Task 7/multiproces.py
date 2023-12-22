import multiprocessing
import time
import random

num_list = [random.randint(1, 100) for _ in range(1_000_000)]
results = multiprocessing.Value('i', 0)


def sum_list(start, end, results):
    for i in num_list[start:end]:
        with results.get_lock():
            results.value += i


if __name__ == "__main__":
    start_time = time.time()
    processes = []

    for i in range(4):
        start = i * len(num_list) // 4
        end = (i + 1) * len(num_list) // 4
        print(f"Процесс {i+1} работает с {start} по {end} элемент")
        p = multiprocessing.Process(target=sum_list, args=(start, end, results))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Все процессы завершили работу за {time.time()- start_time} секунд")

    print(f"Сумма элементов массива: {results.value}")
