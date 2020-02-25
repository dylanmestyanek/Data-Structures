class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)

    def middle_node(self):
        current_node = self

        if not current_node.next:
            return current_node.value
        else:
            double_node = current_node.next
            while double_node:
                current_value = current_node.value

                if double_node.next == None:
                    return current_value
                if double_node.next.next == None:
                    current_node = current_node.next
                    return current_node.value
                
                current_node = current_node.next
                double_node = double_node.next.next
        
    def reverse(self):
        initial_node = self
        current_node = self
        
        while current_node:
            next_node = current_node.next
            next_node.next = current_node
            print(current_node.value, next_node.value)

            current_node = current_node.next

            
   




node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10
print(node1.middle_node())