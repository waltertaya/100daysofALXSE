import asyncio
import time

async def drinkCoffee():
    print('Pour coffee into the cup and start drinking')
    await asyncio.sleep(3)
    print('Finish drinking coffee')
    return 'Finished drinking coffee, start next task'

async def study():
    print('Start studying for the exams')
    await asyncio.sleep(8)
    print('Take a break')
    return 'Finished reading'

async def main():
    start_time = time.time()
    # batch = asyncio.gather(drinkCoffee(), study())
    # result_drink, result_study = await batch
    coffee_task = asyncio.create_task(drinkCoffee())
    study_task = asyncio.create_task(study())

    result_drink = await coffee_task
    result_study = await study_task
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Result for drinking coffee: {result_drink}')
    print(f'Result for studying for exams: {result_study}')
    print(elapsed_time)
    return

if __name__ == '__main__':
    asyncio.run(main())