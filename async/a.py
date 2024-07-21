import asyncio
# import time
# for i in range(100000):
#     print(i)

# # sync:
# def main():
#     print('a')
#     otherfunction()
#     print('b')
     

# def otherfunction():
#     print('1')
#     # await asyncio.sleep(2)
#     time.sleep(1)
#     print('2')

# main()

# # async with sync manner:
# async def main():
#     print('a')
#     await otherfunction()
#     print('b')
     

# async def otherfunction():
#     print('1')
#     await asyncio.sleep(2)
#     print('2')
# asyncio.run(main())

# async def main():
#     task=asyncio.create_task(otherfunction())
#     print('a')
#     await asyncio.sleep(1)
#     print('b')
#     await task

# async def otherfunction():
#     print('1')
#     await asyncio.sleep(2)
#     print('2')
 
# return value:

# async def main():
#     task=asyncio.create_task(otherfunction())
#     print('a')
#     await asyncio.sleep(1)
#     print('b')
#     value= await task
#     print(value)

# async def otherfunction():
#     print('1')
#     await asyncio.sleep(2)
#     print('2')
#     return 1065
 
# asyncio.run(main())
# _____________________________________________
import threading
# def worker():
#     start=time.time()
#     print('start')
#     # time.sleep(3)
#     for i in range(10000):
#         print(i)
#     end=time.time()
#     duration=end-start
#     print(duration)
#     print('done')

# t1=threading.Thread(target=worker)
# t1.start()
# t2=threading.Thread(target=worker)
# t2.start()
# t3=threading.Thread(target=worker)
# t3.start()
# t4=threading.Thread(target=worker)
# t4.start()

# tread pool:
# from concurrent.futures import ThreadPoolExecutor
# def worker(number):
#     print(number)
#     print('start')
#     time.sleep(2)
#     return number**2
    # start=time.time()
    # # time.sleep(3)
    # for i in range(10000):
    #     print(number)
    # end=time.time()
    # duration=end-start
    # print(duration)

# pool=ThreadPoolExecutor(6)
# # it is async
# work1=pool.submit(worker,1)
# work2=pool.submit(worker,6)
# work3=pool.submit(worker,7)
# work4=pool.submit(worker,7)
# work5=pool.submit(worker,8)
# work6=pool.submit(worker,9)
# print('aaaaaaaaaaaaaaaa')
# print(work1.result())

# ---------------------------------------
# import asyncio
# async def printsecond():
#     print('a')
#     while True:
#         print('a')
#         await asyncio.sleep(1)
#         print('.')

# async def dosth(taskname,seconds):
#     print(f'start {taskname}')
#     await asyncio.sleep(seconds)
#     print(f'finish {taskname}')

# async def main():
#     asyncio.create_task(printsecond())

#     tasks=[]
#     for i ,name in enumerate('abcde'):
#         task=asyncio.create_task(dosth(name,i+1))
#         tasks.append(task)
#     await asyncio.gather(*tasks)

# asyncio.run(main())
import time
# -------------------------------------------------
# 2 cup intensive as async:
async def yehdci(x):
    startime=time.time()
    print(f'start{x}')
    async for i in range(10):
        print(x)
    # await asyncio.sleep(x)
    print(f'end{x}')
    endtime=time.time()
    print(endtime-startime)
async def main():
    results=await asyncio.gather(yehdci(2),yehdci(3),yehdci(3))
    # corutinlis=[]
    # for i in range(1,11):
    #     corutinlis.append(yehdci(i))
    # results=await asyncio.gather(*corutinlis)
    # print(results)

asyncio.run(main())