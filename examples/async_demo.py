import asyncio


async def dreaming(n, m):
    await asyncio.sleep(n)
    return m**n


async def main():
    print("Hello")
    await asyncio.sleep(5)
    print("World")


# 运行协程
asyncio.run(main())
