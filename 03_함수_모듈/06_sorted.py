숫자들 = [3,1,1,3,4,5]
이름들 = ["철수","영희","민준"]

print(sorted(숫자들))
print(sorted(이름들))
print(sorted(숫자들,reverse=True))


이름들 = ["박철수", "안영희야","박민준이야"]

print(sorted(이름들, key=lambda x: len(x)))

def 길이순서기능(x):
    return len(x)

순서변경 = sorted(이름들, key=길이순서기능)
print(순서변경)