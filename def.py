# def invite(title="축 결 혼", message="축하드립니다"):
#     header(title)
#     body(message)

# def header(title):
#     print(title)

# def body(message):
#     print(message)

# invite(title="축 결혼", message="찾아와주셔서 감사합니다")

    # for i in range(0, len(문장), 5):
    #     print(문장[i:i+5])
def my_split(string):  

    charNum = 5
    length = len(string)
    dist = int(length / charNum)

    for start in range(dist):
        stop = start + 1
        print(string[start * charNum : stop * charNum])

my_split("안녕하세요반갑습니다기대되네요")

