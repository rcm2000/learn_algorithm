##함수
def isStckFull() :
    global SIZE, stack,top
    if top == SIZE -1:
        return True
    else:
        return False
def push(data):
    global SIZE, stack, top
    if isStckFull():
        print('스텍이 꽉찼습니다.')
        return
    top +=1
    stack[top] = data

def isStackEmpty():
    global SIZE, stack, top
    if top <= - 1:
        return True
    else:
        return False
def pop():
    global SIZE, stack, top
    if isStackEmpty():
        print('스택이 없습니다.')
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data
def peek():
    global SIZE, stack, top
    if isStackEmpty():
        print('스택이 없습니다.')
        return None
    return stack[top]
##전역변수
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1
select = -1
##메인
if __name__ =="__main__":

    while(select != 4):

        select = int(input("선택하세요(1:삽입,2:추출,3:확인,4.종료)-->"))

        if(select == 1):
            data = input('입력할 데이터----->')
            push(data)
            print('현 스택 상태',stack)
        elif (select == 2):
            data = pop()
            print('추출 데이터 = ',data)
            print('현 스택 상태', stack)
        elif (select == 3):
            data = peek()
            print('확인된 데이터 =',data)
        elif (select == 4):
            print('현 스택 상태', stack)
            exit
        else:
            print("1~4의 숫자만 이용가능합니다")
            continue