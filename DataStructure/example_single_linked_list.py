class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None
class SLL:
   def __init__(self):
      self.head = None

# Print the linked list
   def list_print(self):
      print_val = self.head
      print("Linked List: ")
      while print_val is not None:
         print (print_val.data)
         print_val = print_val.next
   def AddAtBeginning(self,new_data):
      NewNode = Node(new_data)

      # Update the new nodes next val to existing node
      NewNode.next = self.head
      self.head = NewNode

l1 = SLL()
l1.head = Node("731")
e2 = Node("672")
e3 = Node("63")

l1.head.next = e2
e2.next = e3

l1.AddAtBeginning("122")
l1.list_print()