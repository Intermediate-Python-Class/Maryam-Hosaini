



class Queue:
    
    def __init__(self):
        self.queue = []

   
    def enqueue(self, item):
        self.queue.append(item)


        # bellow code does not work
        
        # def dequeue(self):
        #     if self.is_empty():

        #         return "Q is empty"

        #         return Self.queue.dequeue()

       
               

                
    



q = Queue()


q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
q.enqueue('d')


print("Current Queue:", q.queue)
# print( queue.dequeue())


