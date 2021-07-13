##함수 클래스
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


## 전역변수

##메인함수
node1 = TreeNode()
node1.data = '화사'

node2 = TreeNode()
node2.data = '솔라'
node1.left = node2

node3 = TreeNode()
node3.data = '문별'
node1.right = node3

node4 = TreeNode()
node4.data = '휘인'
node2.left = node4

node5 = TreeNode()
node5.data = '쯔위'
node2.right = node5

node6 = TreeNode()
node6.data = '선미'
node3.left = node6

print(node1.data,end='   ')
print()
print(node1.left.data,node1.right.data,end='   ')
print()
print(node2.left.data,node2.right.data,node3.left.data,end='   ')
print()
