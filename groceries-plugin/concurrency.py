import asyncio
from io import StringIO
from asyncio import Lock


# Asynchronous function to append to StringIO buffer
async def append_to_buffer(buffer, text, lock):
    async with lock:
        buffer.write(text)


# Main asynchronous function
async def bufferThreads():
    buffer = StringIO()
    lock = Lock()

    # Create a list of tasks
    tasks = []
    for i in range(5):
        tasks.append(append_to_buffer(buffer, f"Line {i}\n", lock))

    tasks2 = []
    for i in range(5):
        tasks2.append(append_to_buffer(buffer, f"Line {i}\n", lock))

    # Combine both lists of tasks and run them concurrently
    await asyncio.gather(*tasks, *tasks2)

    # Get the final string
    result = buffer.getvalue()
    print(result)


# Run the main function
asyncio.run(bufferThreads())
