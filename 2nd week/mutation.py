line = "short!"
condition = "6 ?"
if len(line) <= int(condition[0]):
    print("The number you gave is too large!")
else:
    print(line.replace(int(condition[0]), condition[3]))

#The number you gave is too large! 출력에는 성공했는데(3번째 예시), else에서 다른 문자로 대체하여 출력하는 것은 실패했습니당ㅠ