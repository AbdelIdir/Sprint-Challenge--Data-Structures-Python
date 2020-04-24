from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.size = 0

    def append(self, item):

        if self.storage.length == self.capacity:
            self.current.value = item
            self.current = self.current.next
        else:
            self.storage.add_to_tail(item)
            if self.storage.length == 1:
                self.current = self.storage.head
            if self.storage.length == self.capacity:
                self.storage.tail.next = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        latest = self.storage.head
        list_buffer_contents.append(latest.value)

        while latest.next != self.storage.head:
            if not latest.next:
                break
            list_buffer_contents.append(latest.next.value)
            latest = latest.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass
