import asyncio
import time
import random

num_list = [random.randint(1, 100) for _ in range(1_000_000)]


async def sum_list(start, end):
    return sum(num_list[start:end])


async def main():
    start_time = time.time()
    tasks = []

    for i in range(4):
        start = i * len(num_list) // 4
        end = (i + 1) * len(num_list) // 4
        print(f"Корутина {i+1} работает с {start} по {end} элемент")
        tasks.append(asyncio.ensure_future(sum_list(start, end)))
    results = await asyncio.gather(*tasks)

    print(f"Все корутины завершили работу за {time.time()- start_time} секунд")

    print(f"Сумма элементов массива: {sum(results)}")

if __name__ == '__main__':
    asyncio.run(main())
