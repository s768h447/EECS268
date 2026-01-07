# Sam Harrison 2/15/2022

from node import Node

class Stack:

    def __init__(self):

        self.top = None

    def is_empty(self):

        #   it can only be empty if the top is None

        if self.top is None:

            return True

        else:

            return False

    def push(self, data):

        if self.is_empty():

            self.top = Node(data)

        else:

            #   creates a node with said data

            temporary_node = Node(data)

            #   puts the current top into the position after

            temporary_node.next = self.top

            #   sets the top to the new data

            self.top = temporary_node

    def pop(self):

        if self.is_empty():

            return None

        else:

            #   sets popped_data to the current top

            popped_data = self.top

            #   sets next to the top and now next is None

            self.top = self.top.next

            popped_data.next = None

            #   returns the entry of the popped_data

            return popped_data.entry

    def peek(self):

        if self.is_empty():

            return None

        else:

            return self.top.entry

class Queue:

    def __init__(self):

        self.front = None

        self.back = None

    def is_empty(self):

        #   it can only be empty if the front is None

        return self.front is None

    def enqueue(self, data):

        temporary_node = Node(data)

        if self.is_empty():

            #   if the front is empty, turn the front into temporary_node and back into front

            self.front = temporary_node

            self.back = self.front

        else:

            #   otherwise, put temporary_node in back and back.next

            self.back.next = temporary_node

            self.back = temporary_node

    def dequeue(self):

        if self.is_empty():

            return None

        #   puts self.front into the temporary_nde

        temporary_node = self.front

        self.front = temporary_node.next

        #   removes the front of the queue and then resets all to None

        if self.front is None:

            self.back = None

    def peek(self):

        if self.is_empty():

            return None

        #   returns None unless it exists, then returns the front

        else:

            return self.front.entry


def list_to_string(input_list):

    #   takes inputted list from user's command and removes command then returns

    input_list.pop(0)

    return ' '.join(input_list)


def main(program_run=True):

    #   only runs while the variable, program_run, is true

    temporary_queue = Queue()

    temporary_stack = Stack()

    #   after starting the nodes, puts main on the bottom of the stack

    temporary_stack.push('main')

    while program_run is True:

        #   takes user_command and splits into a string

        user_command = input().split(' ')

        if 'START' == user_command[0]:

            #   example: START <process name>

            #   if something goes wrong, it tells the user, and this can be applied to all exception handles

            try:

                user_command = list_to_string(user_command)

                #   uses the temporary_node and adds user_command to the queue

                temporary_queue.enqueue(user_command)

                print(user_command + ' added to queue')

            except:

                print('invalid command')


        elif 'CALL' == user_command[0]:

            #   example: CALL <function name>

            try:

                user_command = list_to_string(user_command)

                #   prints the call and then stores the front

                print(temporary_queue.peek() + ' calls ' + user_command)

                temporary_node = temporary_queue.peek()

                #   puts process at the back of the queue

                temporary_queue.dequeue()

                temporary_queue.enqueue(temporary_node)

            except:

                print('invalid command')

        elif 'RETURN' == user_command[0]:

            try:

                print(temporary_queue.peek() + ' returns from main')

                print('program ended')

                program_run = False

            except:

                print('invalid command')

if __name__ == '__main__':

    main()
