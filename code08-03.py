##함수 클래스
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

##전역변수
memory = []
root = None
nameArray = ['블랭핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스스']


##메인코드
node = TreeNode()
node.data = nameArray[0]
root = node
memory.append(node)
for name in nameArray[1:] :
    node = TreeNode()
    node.data = name

    current = root
    while True:
        if name < current.data :
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right

    memory.append(node)

print('이진 탐색트리 구성 완료')

findData = '레드벨벳'
current = root
while True:
    if current.data == findData:
        print(findData,'찾았음')
        break
    elif current.data > findData:
        if current.left == None:
            print(findData,'가 트리에 없음')
            break
        else:
            current = current.left
    else:
        if current.right == None:
            print(findData,'가 트리어 없음')
            break
        else:
            current = current.right