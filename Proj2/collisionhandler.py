class Node:
    def __init__(self,value,next = None):
        '''
        :param value: contains the key value being stored that will be accessed later
        :param next: contains the next node to travel to in case of a collision
        '''
        self.value = value
        self.next = next

primary = 0
collisions = 0
class CollisionHandler:
    def __init__(self, bucket_size, modulo):
        '''
        This class handles each kind of collision. The getter functions help track the number of collisions
        :param bucket_size: The number of keys that can be entered in a bucket before it is considered full
        :param modulo: The modulo value used to find the next index
        '''
        self.bucket_size = bucket_size
        self.modulo = modulo

    def get_primary(self):
        return primary

    def get_collisions(self):
        return collisions

    def linear(self,array,index,value):
        '''
        Linear probing collision handling scheme
        :param array: Entire hash table
        :param index: hash value that is used as index for the hash table
        :param value: key value that is being entered at that index
        :return: Returns the hash table after collision is handled
        '''
        global primary, collisions
        start = index
        counter = 1
        # Runs until the value within hash table at index is less than bucket size
        while len(array[index]) >= self.bucket_size:
            index = (int((index + 1)) % self.modulo) % (120 // self.bucket_size)
            counter += 1
        # While loop ends which means an enpty space is found. Key is entered there
        array[index].append(value)
        primary = 1
        collisions = counter - 1
        return array

    def quadratic(self,array,index,value):
        '''
        Quadratic Probing Collision Handling Scheme
        :param array: Entire hash table
        :param index: hash value that is used as index for the hash table
        :param value: key value that is being entered at that index
        :return: Returns the hash table after collision is handled
        '''
        global primary, collisions
        start = index
        jump = 1

        # Runs until the value within hash table at index is less than bucket size
        while len(array[index]) >= self.bucket_size:
            index = (int((index + (jump * jump))) % self.modulo) % (120 // self.bucket_size)
            # increments jump by 1 each time so after each loop, the jump gets bigger and bigger
            jump += 1
        array[index].append(value)
        primary = 1
        collisions = jump - 1
        return array

    def chaining(self,array,index,value):
        '''
        Chaining Collision Handling Scheme
        :param array: Entire hash table
        :param index: hash value that is used as index for the hash table
        :param value: key value that is being entered at that index
        :return: Returns the hash table after collision is handled
        '''
        global primary, collisions

        # if current value is not a Node, a Node is made there to start a linked list there
        if type(array[index]) != Node:
            array[index] = Node(array[index])
        counter = 1

        current = index

        # loops until it reaches the end of the linked list while traversing using .next entries
        while array[current].next != None:
            current = array[current].next
            counter += 1

        # Calculates a new next index and sets it as the current Node's .next
        next_index = ((int(array[current].value[0][:2])) % self.modulo)
        array[next_index] = Node([value])
        array[current].next = next_index

        primary = 1
        collisions = primary + counter - 1
        return array