def openBox():
    global count
    print('박스열기~~~~')
    count -= 1
    if count == 0 :
        print('반지넣기')
        return
    openBox()
    print('박스닫기')

count = 10
openBox()