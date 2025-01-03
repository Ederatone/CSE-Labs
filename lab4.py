import asyncio

async def process_line(line):
    word_count = len(line.split())
    await asyncio.sleep(0.52)
    print(f"Processed line with {word_count} words.")