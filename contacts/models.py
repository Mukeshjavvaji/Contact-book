from django.db import models

# Create your models here.
class Node:
    def __init__(self, name=None, number=None):
        self.name=name
        self.number=number
        self.next=None
        self.prev=None
    
class DLinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def bisecting_insert(self, name, number):
        n=self.head
        newnode=Node(name, int(number))
        if n:
            if name<n.name:
                self.head=Node(name, int(number))
                self.head.next=n
                n.prev=self.head
            else:
                while n:
                    if name<n.name:
                        n.prev.next=newnode
                        newnode.prev=n.prev
                        newnode.next=n
                        n.prev=newnode
                        break
                    n=n.next
                else:
                    num=lst.tail
                    num.next=newnode
                    newnode.prev=num
                    lst.tail=newnode
        else:
            self.head=newnode
        
    def delete(self, num):
        n=self.head
        l=self.tail
        if int(n.number)==int(num):
            self.head=n.next
            if self.head:
                self.head.prev=None
        elif int(l.number)==int(num):
            l.prev.next=None
            self.tail=l.prev
        else:
            while n:
                if int(n.number)==int(num):
                    n.prev.next=n.next
                    if n.next:
                        n.next.prev=n.prev
                    break
                n=n.next

    def deletelog(self, num):
        n=self.head
        if n:
            if int(n.number)==int(num):
                self.head=n.next
                if self.head:
                    self.head.prev=None
        l=self.tail
        if l:
            if int(l.number)==int(num):
                self.tail=l.prev
                if self.tail:
                    self.tail.next=None
        while n:
            if int(n.number)==int(num):
                if n.prev:
                    n.prev.next=n.next
                if n.next:
                    n.next.prev=n.prev
            n=n.next

lst=DLinkedlist()
lst.head=Node('Ajay', 5464168653)
n2=Node('Matt', 1368464861)
n3=Node('Olivia', 9585966565)
lst.head.next=n2
n2.next=n3
n2.prev=lst.head
n3.prev=n2
lst.tail=n3

log=DLinkedlist()
log.tail=Node('Ajay', 5464168653)
n2=Node('Olivia', 9585966565)
log.head=n2
log.tail.prev=n2
n2.next=log.tail
