# 分支
temp = input("你的考试成绩是多少分？")

score = int(temp)
if 100 > score > 90:
    print("成绩为A")
elif 90 >= score > 80:
    print("成绩为B")
elif 60 >= score > 80:
    print("成绩为C")
elif 60 > score:
    print("成绩为D")
else:
    print("输入错误")

# 循环
name = 'Danke'
for i in name:
    print(i,end=' ')
print("--------------")

for i in range(5):
    print(i)
print("--------------")

for i in range(10):
    if i%2 != 0:
        print(i)
        continue
    i += 2
    print(i)