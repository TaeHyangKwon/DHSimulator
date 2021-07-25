g = 7
p = 23
x = 3
r1 = g**x % p
print("r1 : ", r1)
y = 6
r2 = g**y % p
print("r2 : ", r2)

ka = r2**x % p
kb = r1**y % p

print("앨리스 대칭키 계산 : ", ka)
print("밥 대칭키 계산 : ", kb)

if ka == kb:
    print("공유키가 같습니다.")
else:
    print("공유키가 다릅니다.")

