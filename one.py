s=0
for i in range(1,101):
    s=s+i
print('s={}\n'.format(s))

t=0
for i in range(1,101):
    if i%2==1:
        t=t+1/i
    else:
        t=t-1/i
print('t={}\n'.format(t))