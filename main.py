import keep_alive
import asyncio
import headless_chrome

async def main():
  print('Running...')

# database(frame)
keep_alive.keep_alive()
headless_chrome()
asyncio.run(main())