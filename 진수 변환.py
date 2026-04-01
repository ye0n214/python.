a= int(input("입력 진수 결정(16/10/8/2):" ))

if a==16: 
    num= int(input("값 입력:"), 16)
if a==10: 
    num= int(input("값 입력:"), 10)
if a==8: 
    num= int(input("값 입력:"), 8)
if a==2: 
    num= int(input("값 입력:"), 2)

print("16진수===>", hex(num))
print("10진수===>", int(num))
print("8진수===>", oct(num))
print("2진수===>", bin(num))