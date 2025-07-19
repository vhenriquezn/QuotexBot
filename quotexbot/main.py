import asyncio
from quotexbot.bot import BotModular

async def main():
    bot = BotModular()
    await bot.conectar()
    await bot.set_account()
    await bot.trading_loop()

if __name__ == "__main__":
    asyncio.run(main())
