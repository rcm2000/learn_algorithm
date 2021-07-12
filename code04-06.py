##함수 선언 부분##
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
select = -1

##메인 코드 부분##
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

if __name__ =="__main__":

    while(select != 4):

        select = int(input("선택하세요(1:삽입,2:삭제,3:검색,4.종료)-->"))

        if(select == 1):
            finddata = input("검색할 데이터 --> ")
            insertdata = input("검색한 데이터 앞에 추가할 데이터 --> ")
            insert_node(finddata,insertdata)
            printNode(head)
        elif (select == 2):
            deleteData = input("삭제할 데이터 --> ")
            delete_node(deleteData)
            printNode(head)
        elif (select == 3):
            findData = input("검색할 데이터 --> ")
            find_node(findData)
            fNode = find_node(findData)
            print(fNode.data)
        elif (select == 4):
            printNode(head)
            exit
        else:
            print("1~4의 숫자만 이용가능합니다")
            continue