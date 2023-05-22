class Node:
    def __init__(self,item):
        self.item=item
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
    
    def insertionmiddle(self,middleNode,newItem):
        if middleNode is None:
            print("middle node is absent")
        else:
            newNode = Node(newItem)
            newNode.next = middleNode.next
            middleNode.next = newNode


linked_list=Linkedlist()
linked_list.head=a=Node("Thor")
a.next=b=Node("Thanos")
b.next=c=Node("spiderMan")

linked_list.insertionmiddle(b,"ironMan")

while linked_list.head:
    print(linked_list.head.item)
    linked_list.head=linked_list.head.next