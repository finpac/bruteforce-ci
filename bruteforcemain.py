import threading
import queue
from pwdproducer import PwdProducer
from pwdconsumer import PwdConsumer

your_list = 'abc'

complete_list2 = []
for current in range(3):
    a = [i for i in your_list]
    #print(a)
    b = []
    for y in range(current):
        for x in a:
            for i in your_list:
                b.append(x+i)
    print(b)
    a = [i for i in b]
   # a = b

    complete_list2 = complete_list2 + b

    print(complete_list2)

queue = queue.Queue(maxsize=10)1
condition = threading.Condition()

producer = PwdProducer(queue,condition)
consumer = PwdConsumer(queue, condition)

producer.start()
consumer.start()

producer.join()
consumer.join()
