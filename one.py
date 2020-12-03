s=0
for i in range(1,101):
    s=s+i  #缩进表示循环部分
print('s={}\n'.format(s))

t=0
for i in range(1,101):
    if i%2==1:   #i%2表示除以2取余数
        t=t+1/i
    else:
        t=t-1/i
print('t={}\n'.format(t))