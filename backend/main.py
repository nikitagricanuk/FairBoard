import asyncio
import datetime
from database.db import add_user, get_user, add_problem, get_problems

async def main():
    user = await add_user("John", "Doe", 44433)
    print(user)
    user_data = await get_user(user, 44433)
    print(user_data)

    for i in range(1, 25):
        await add_problem(f"19.{str(i)}", datetime.datetime.now())

    problems = await get_problems()
    print(problems)
    exit(0)
    
asyncio.run(main())