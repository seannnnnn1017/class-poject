class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class Linklist:
    def __init__(self,head=None):
        self.head=head
    def append_data(self,data):
        if self.head==None:
            self.head=Node(data)
            return
        node=self.head
        while node.next:
            node=node.next
        node.next=Node(data)

    def print_list(self):
        if not self.head:
            print(self.head)
        node = self.head
        print('[',end='')
        while node:
            print(node.data, end='->') if node.next else print(node.data, end='')
            node = node.next
        print(']',end='')

if __name__=='__main__':
    A=Linklist()
    while True:
        user=int(input("""
                    1=輸入data
                    2=查看
                    0=離開
                    """))
        if user==0:break
        elif user==1:
            while True:
                data=input("""
                         輸入leave離開
                         """)
                if data =='leave':break
                A.append_data(int(data))
        elif user==2:
            A.print_list()