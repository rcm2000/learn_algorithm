import random
##함수
def findMinIdx(ary):
    minIdx = 0
    for i in range(1,len(ary)):
        if (ary[minIdx] > ary[i]):
            minIdx = i
    return minIdx

##변수
before = [random.randint(100,999) for _ in range(8)]
after = []
##메인
print('정렬전 -- >', before)
for i in range(len(before)):
    minPos = findMinIdx(before)
    after.append(before[minPos])
    del(before[minPos])
print('최솟값 -- >', after)
