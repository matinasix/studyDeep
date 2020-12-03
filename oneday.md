# 第一天
\n是换行，{}是放t的数值，format是t的属性
## 计算1+...+101
s=0
for i in range(1,101):
    s=s+i              缩进表示循环部分
print('s={}\n'.format(s)) 
## 计算1-1/2+1/3-...-1/101
t=0
for i in range(1,101):
    if i%2==1:
        t=t+1/i
    else:
        t=t-1/i
print('t={}\n'.format(t))
i%2表示除以2取余数


