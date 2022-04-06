character = input("请输入明文：")
password = chr(ord("a") + (ord(character) - ord("a") + 3) % 26)
print("密码为：")
print(password)
