import asyncio
#create_tasks

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from coroutine {id}"}


async def main():
    # Create tasks for running coroutines concurrently ทำให้งานหลายรูทีนทำงานได้พร้อมกัน
    task1 = asyncio.create_task(fetch_data(1, 2))
    task2 = asyncio.create_task(fetch_data(2, 3))

    result1 = await task1
    result2 = await task2

    task3 = asyncio.create_task(fetch_data(3, 1))

    result3 = await task3

    print(result1, result2, result3)



asyncio.run(main())