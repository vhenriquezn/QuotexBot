import asyncio
from .bot import BotModular

def main():
    asyncio.run(run_bot())

async def run_bot():
    bot = BotModular()
    await bot.conectar()
    await bot.set_account()
    await bot.trading_loop()

if __name__ == "__main__":
    main()