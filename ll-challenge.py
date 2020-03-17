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
        current_node = self
        next_node = None
        prev_node = None

        while current_node:
            # SAVE NEXT NODE BEFORE ITS GONE
            next_node = current_node.next
            # CURRENT NEXT TO PREV
            current_node.next = prev_node
            # PREV TO CURR
            prev_node = current_node
            # CURR TO NEXt
            current_node = next_node

        main = self
        while main:
            print(main.value)
            main = self.next
        

            
   




node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
print(node1.reverse())