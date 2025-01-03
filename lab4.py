import asyncio
import aiofiles

async def process_line(line):
    word_count = len(line.split())
    await asyncio.sleep(0.52)
    print(f"Processed line with {word_count} words.")

async def process_large_file(file_path):
    async with aiofiles.open(file_path, mode='r') as file:
        async for line in file:
            await process_line(line)