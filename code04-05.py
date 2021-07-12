## 함수 class 선언부
class Node():
    def __init__(self):
        self.data = None
        self.link = None
def printNode(start) :
    current = start
    print(current.data, end='  ')
    while current.link != None:
        current = current.link
        print(current.data, end='  ')
    print()
def insert_node(finddata,insertdata):
    global memory,head,current,pre

    if head.data == finddata:
        node = Node()
        node.data = insertdata
        node.link = head
        head = node
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == finddata:
            node = Node()
            node.data = insertdata
            node.link = current
            pre.link = node
            return
    node = Node()
    node.data = insertdata
    current.link = node
def delete_node(deleteData):
    global memory, head, current, pre

    if head.data == deleteData:
        current = head
        head = head.link
        del(current)
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return

def find_node(findData):
    global memory, head, current, pre
    current = head
    if current.data == findData:
        return current
    while current.link != None:
        current = current.link
        if current.data == findData:
            return current
    return Node()








## 전역변수부
memory = []
head , current , pre = None,None,None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']


##메인코드부
#첫 데이터 입력
node = Node()
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNode(head)
insert_node('다현','화사')
printNode(head)
insert_node('사나','솔라')
printNode(head)
insert_node('재남','문별')
printNode(head)

delete_node('재남')
printNode(head)

fNode = find_node('재남')
print(fNode.data)
fNode = find_node('사나')
print(fNode.data)

