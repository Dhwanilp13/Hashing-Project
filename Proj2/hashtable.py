from Proj2.collisionhandler import CollisionHandler, Node

counter = [0,0,0]
class HashTable:
    def __init__(self, size, scheme, modulo, bucket_size, collision):
        '''
        Creates a hash table with two different hash functions and an insert function
        :param size: size of hash table
        :param scheme: which of two hash functions to use
        :param modulo: modulo divisor for division function; m for multiplication function
        :param bucket_size: number of possible values allowed in a bucket
        :param collision: type of collision method to use if there is one
        '''
        self.size = size
        self.scheme = scheme
        self.modulo = modulo
        self.bucket_size = bucket_size
        self.num_buckets = size // bucket_size
        self.array = [[] for _ in range(self.num_buckets)]
        self.collision = collision
        self.handler = CollisionHandler(self.bucket_size, self.modulo)

    def division(self, value):
        return (int(value) % self.modulo) % self.num_buckets

    def multiplication(self, value):
        a = 0.127
        m = self.modulo
        return int(m * ((int(value) * a) % 1))

    def insert(self, value):
        global counter
        # hash function used is determined based on the parameter that's passed to the hash table class
        if self.scheme == 'division':
            hash_index = self.division(value)
        if self.scheme == 'multiplication':
            hash_index = self.multiplication(value)
        collision = False

        # For both list and Node types, it checks if an available space exists to enter number
        # If not, collision is made true
        if type(self.array[hash_index]) == list:
            if len(self.array[hash_index]) < self.bucket_size:
                self.array[hash_index].append(value)
                counter[0] += 1
            else:
                collision = True
        elif type(self.array[hash_index]) == Node:
            if len(self.array[hash_index].value) < self.bucket_size:
                self.array[hash_index].append(value)
                counter[0] += 1
            else:
                collision = True

        # if collision is made true, this runs and calls on the CollisionHandler class from collisionhandler.py
        if collision:
            if self.collision == 'linear':
                self.array = self.handler.linear(self.array, hash_index, value)
                counter[1] += self.handler.get_primary()
                counter[2] += self.handler.get_collisions()

            elif self.collision == 'quadratic':
                self.array = self.handler.quadratic(self.array, hash_index, value)
                counter[1] += self.handler.get_primary()
                counter[2] += self.handler.get_collisions()

            elif self.collision == 'chaining':
                self.array = self.handler.chaining(self.array, hash_index, value)
                counter[1] += self.handler.get_primary()
                counter[2] += self.handler.get_collisions()

            else:
                raise Exception("Invalid collision method called")

    def get_array(self):
        return self.array