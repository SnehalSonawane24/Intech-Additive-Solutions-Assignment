# get middle element of a singly linked list in one pass
class Node:
    def __init__(self,k):
        self.data = k
        self.next = None
        
def getLength(h):
    length = 0
    
    while h:
        length += 1
        h = h.next
        
    return length
    
def getMiddle(h):
    length = getLength(h)
    
    mid_index = length // 2
    while mid_index:
        h = h.next
        mid_index -= 1
        
    return h.data
    
def main():
    # Input
    head = Node(70)
    head.next = Node(20)
    head.next.next = Node(80)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    
    print(getMiddle(head))
    
if __name__ == "__main__":
    main()

# Output - 80
