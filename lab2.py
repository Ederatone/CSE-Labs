import asyncio
import time
from typing import Callable, List, Any
from concurrent.futures import ThreadPoolExecutor


# async map
async def async_map(func: Callable, iterable: List[Any]) -> List[Any]:
    tasks = [func(item) for item in iterable]
    return await asyncio.gather(*tasks)


# async function
async def async_square(number: int) -> int:
    await asyncio.sleep(1)
    return number ** 2


# debounce for delay
async def debounce(func: Callable, delay: float, *args, **kwargs) -> Any:
    start_time = time.monotonic()
    result = await func(*args, **kwargs)
    elapsed_time = time.monotonic() - start_time

    if elapsed_time < delay:
        await asyncio.sleep(delay - elapsed_time)
    return result

def promise_map(func: Callable, iterable: List[Any]) -> List[Any]:
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(func, item) for item in iterable]
        return [future.result() for future in futures]

def sync_square(number: int) -> int:
    time.sleep(1)
    return number ** 2

async def async_parallel_map(func: Callable, iterable: List[Any], concurrency: int = 2) -> List[Any]:
    semaphore = asyncio.Semaphore(concurrency)

    async def limited_task(item):
        async with semaphore:
            return await func(item)

    tasks = [limited_task(item) for item in iterable]
    return await asyncio.gather(*tasks)

# demo function
async def demo() -> None:
    nums = [1, 2, 3, 4, 5, 6]

    print("async_map:")
    result = await async_map(async_square, nums)
    print(f"result: {result}")

    print("\nasync_map with debounce:")
    debounce_result = await debounce(async_map, 2, async_square, nums)
    print(f"result: {debounce_result}")

    print("\nasync_parallel_map:")
    parallel_result = await async_parallel_map(async_square, nums, 2)
    print(f"result: {parallel_result}")

def demo_promise():
    nums = [1, 2, 3, 4, 5, 6]

    print("promise_map:")
    result = promise_map(sync_square, nums)
    print(f"result: {result}")

if __name__ == "__main__":
    print("===== Async Demo =====")
    asyncio.run(demo())
    print("\n===== Promise Demo =====")
    demo_promise()
