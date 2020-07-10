n = int(input(3))
if float(n / 2) == int(n / 2) and 2 <= n <= 5:
    print("Not Weird")
elif float(n / 2) == int(n / 2) and 6 <= n <= 20:
    print("Weird")
elif float(n / 2) == int(n / 2) and n > 20:
    print("Not Weird")
else:
    print("Weird")

#3을 넣어서 출력해 보면 계속 3 아니면 오류로 뜨는데 뭐가 잘못됐는지 모르겠어요..