#   Samuel Harrison 4/7/2022

#   I had to remove some of the code to run the other ones efficiently

#   I also have never used excel before, so my graphs are bad

import time
from queue import Queue
from stack import Stack
from linkedlist import LinkedList

def ns_to_s(ns):

    return ns/1000000000

def main():

    #   all calculations for the single-pop stack
    stack_length = 0

    timed_stack = Stack()

    while stack_length != 100000:

        #   puts 1000 elements on a stack
        [timed_stack.push(0) for _ in range(1000)]

        stack_length += 1000

        start = time.perf_counter_ns()

        timed_stack.pop()

        end = str(time.perf_counter_ns() - start)

        #   takes calculations and puts into a file
        with open('StackSinglePop.csv', 'a') as file:

            file.write(end + '\n')

        timed_stack.push(0)

 #   all calculations for the multi-pop stack
    stack_length = 1000

    timed_stack = Stack()

    while stack_length != 100000:

        #   puts stack_length amount of  elements on a stack
        [timed_stack.push(0) for _ in range(stack_length)]

        stack_length += 1000

        start = time.perf_counter_ns()

        [timed_stack.pop() for _ in range(stack_length) if timed_stack.is_empty() == False]

        end = str(time.perf_counter_ns() - start)

        #   takes calculations and puts into a file
        with open('StackMultiPop.csv', 'a') as file:

            file.write(end + '\n')

    #   all calculations for the enqueue
    queue_length = 0

    timed_queue = Queue()


    while queue_length != 100000:

        start = time.perf_counter_ns()

        [timed_queue.enqueue(0) for _ in range(1000)]

        end = str(time.perf_counter_ns() - start)

        queue_length += 1000

        #   takes calculations and puts into a file
        with open('QueueEnqueue.csv', 'a') as file:

            file.write(end + '\n')



if __name__ == '__main__':

    main()
