class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class LinkedList:
  def __init__(self):
    self.head=None
    
  # Function to insert a new node at the beginning
  def push(self,new_data):
    new_node=Node(new_data)
    new_node.next=self.head
    self.head=new_node
    
  # insert a new node after the given node
  def insertAfter(self,prev_node,new_data):
    if prev_node is None:
      print("The given previous node cannot be null")
      return
    new_node=Node(new_data)
    new_node.next=prev_node.next
    prev_node=new_node
    
  #Append a new node at the end
  def append(self,new_data):
    new_node=Node(new_data)
    new_node.next=null
    if self.head is None:
      self.head=new_node
      return
    last=self.head
    while(last.next):
      last=last.next
    last.next=new_node
    
  # Utility function to print the linked list
  def printList(self):
    temp=self.head
    while(temp):
      print(temp.data)
      temp=temp.next
      
if __name__=="__main__":
  llist=LinkedList()
  llist.append(8)
  llist.push(7)
  llist.push(1)
  llist.append(4)
  llist.insertAfter(llist.head.next, 8)
  llist.printList()
    

    
