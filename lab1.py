import asyncio
from typing import Callable, List, Any

async def async_map(func: Callable, iterable: List[Any]) -> List[Any]:
    tasks = [func(item) for item in iterable]
    return await asyncio.gather(*tasks)

async def async_square(number: int) -> int:
    await asyncio.sleep(1)
    return number ** 2

async def demo() -> None:
    nums = [1, 2, 3, 4, 5, 6]

    print("async_map:")
    result = await async_map(async_square, nums)
    print(f"result: {result}")

asyncio.run(demo())