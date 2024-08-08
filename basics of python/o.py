class Node:
    def init(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None

class LinkedList:
    def init(self):
        self.head = None
    
    def insert(self, coefficient, exponent):
        new_node = Node(coefficient, exponent)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def display(self):
        current = self.head
        while current:
            print(f"{current.coefficient}x^{current.exponent}", end=" ")
            current = current.next
        print()
    
    def add_polynomials(self, other_list):
        result = LinkedList()
        current1 = self.head
        current2 = other_list.head

        while current1 and current2:
            if current1.exponent > current2.exponent:
                result.insert(current1.coefficient, current1.exponent)
                current1 = current1.next
            elif current1.exponent < current2.exponent:
                result.insert(current2.coefficient, current2.exponent)
                current2 = current2.next
            else:
                sum_coeff = current1.coefficient + current2.coefficient
                if sum_coeff != 0:
                    result.insert(sum_coeff, current1.exponent)
                current1 = current1.next
                current2 = current2.next
        
        while current1:
            result.insert(current1.coefficient, current1.exponent)
            current1 = current1.next
        
        while current2:
            result.insert(current2.coefficient, current2.exponent)
            current2 = current2.next
        
        return result
    
    def multiply_polynomials(self, other_list):
        result = LinkedList()
        current1 = self.head
        while current1:
            current2 = other_list.head
            while current2:
                new_coeff = current1.coefficient * current2.coefficient
                new_exp = current1.exponent + current2.exponent
                result.insert(new_coeff, new_exp)
                current2 = current2.next
            current1 = current1.next
        return result
#Example usage    
linked_list1 = LinkedList()
linked_list1.insert(5, 4)
linked_list1.insert(3, 2)
linked_list1.insert(5, 0)

linked_list2 = LinkedList()
linked_list2.insert(3, 3)
linked_list2.insert(5, 1)
linked_list2.insert(3, 0)

print("result of addition:: ")
result_addition = linked_list1.add_polynomials(linked_list2)
result_addition.display() 

print("result of multiplication:: ")
result_multiplication = linked_list1.multiply_polynomials(linked_list2)
result_multiplication.display()
result.insert(current2.coefficient, current2.exponent)
current2 = current2.next
else:
sum_coeff = current1.coefficient + current2.coefficient
if sum_coeff != 0:
                    result.insert(sum_coeff, current1.exponent)
current1 = current1.next
current2 = current2.next
        
while current1:
            result.insert(current1.coefficient, current1.exponent)
            current1 = current1.next
        
while current2:
            result.insert(current2.coefficient, current2.exponent)
            current2 = current2.next
return result