##함수
def isQueueFull():
    global SIZE, front, rear
    if ((rear+1) % SIZE == front):
        return True
    else:
        return False
def enQueue(data):
    global SIZE, front, rear
    if isQueueFull():
        print('큐가 가득 찼습니다.')
        return
    rear  = (rear+1) % SIZE
    queue[rear] = data

def isQueueEmpty():
    global SIZE, front, rear
    if front == rear:
        return True
    else:
        return False

def deQueue():
    global SIZE, front, rear
    if isQueueEmpty():
        print('큐가비었습니다.')
        return None
    front += (front+1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek():
    global SIZE, front, rear
    if isQueueEmpty():
        print('큐가비었습니다.')
        return None
    front += 1
    return queue[(front+1) % SIZE]




##변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front, rear = 0,0
select = -1
##
if __name__ =="__main__":

    while(select != 4):

        select = int(input("선택하세요(1:삽입,2:추출,3:확인,4.종료)-->"))

        if(select == 1):
            data = input('입력할 데이터----->')
            enQueue(data)
            print('현 큐 상태',queue)
        elif (select == 2):
            data = deQueue()
            print('추출 데이터 = ',data)
            print('현 스택 상태', queue)
        elif (select == 3):
            data = peek()
            print('확인된 데이터 =',data)
        elif (select == 4):
            print('현 스택 상태', queue)
            exit
        else:
            print("1~4의 숫자만 이용가능합니다")
            continue
