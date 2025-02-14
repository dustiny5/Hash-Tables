# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # Instantiate LP
        lp = LinkedPair(key, value)
        
        # Get index using hash method
        index = self._hash_mod(key)
        
        # If None then insert LP
        if self.storage[index] == None:
            self.storage[index] = lp
          
        # If not None then link LP
        else:
            current = self.storage[index]
            # Loop to the end of the LP
            while current:
                # If .next is none then set current.next to LP
                if current.next == None:
                    current.next = lp
                    break
                else:
                    current = current.next




    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # Get index using hash method
        index = self._hash_mod(key)
        
        current = self.storage[index]
        prev = None
        
        if not current:
          print('Invalid Key')
        
        while current:
            if current.key == key and prev == None:
                self.storage[index] = current.next
                print(f'Removed Key: {key}')
                break
            elif current.key == key and prev != None:
                prev.next = current.next
                print(f'Removed Key: {key}')
                break
            else:
                prev = current
                current = current.next
        


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # Get index using hash method
        index = self._hash_mod(key)
        
        current = self.storage[index]
        
        while current:
            if current.key == key:
                return current.value
            else:
                current = current.next
        else:
            print('Invalid Key')


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # Resize to double
        self.capacity *= 2
        
        # Save old storage
        old_storage = self.storage
        
        # Save new storage
        self.storage = [None] * self.capacity
        
        # Loop over old_strage and insert back into resized storage
        for current in old_storage:
            if current is not None:
                # Loops thorugh all LinkedList for each index, if it exists.
                while current:
                
                    # Get key value pair of current LP
                    key, value = current.key, current.value
                    self.insert(key, value)
                    
                    # Save next variable then override current.next to None ro reset pointer
                    next_var = current.next
                    current.next = None
                    
                    # Continue to next LP
                    current = next_var
          
          



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
