x = int(input("Type a natural number: 1"))
y = int(input("Type a natural number: 1"))
z = int(input("Type a natural number: 1"))
n = int(input("Type a natural number: 2"))
answer1 = [[i, j, k] for i in range(0, x + 1) for j in range(0, y + 1) for k in range(0, z + 1)]
answer2 = [[i, j, k] for [i, j, k] in answer1 if i + j + k != n]
print(answer2)

# 순서쌍은 제대로 출력되는데 순서쌍만 출력되는 게 아니라, 그 순서쌍 앞에 input에 넣은 내용도 같이 출력됩니당..