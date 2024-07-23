import asyncio
import time


# single event loop
async def task(name: str):
    print(f'Hello, {name}')
    await asyncio.sleep(1)  # return the control back to "event loop"
    print(f'Goodbye, {name}')


async def main():
    tasks: list[asyncio.Task] = [asyncio.create_task(task(name)) for name in ['John', 'Alice', 'Bob']]
    await asyncio.gather(*tasks)


# Python 3.11+ 버전부터는 다음과 같은 방식으로도 사용할 수 있습니다.
async def main1():
    async with asyncio.TaskGroup() as tg:
        for name in ['John', 'Alice', 'Bob']:
            tg.create_task(task(name))


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    asyncio.run(main1())  # 인자로 넘긴 Coroutine (코루틴) 을 실행
    time_took = time.perf_counter() - start
    print(f"it took {time_took} seconds")
