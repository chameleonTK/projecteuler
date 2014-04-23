fibo = [1,1]

for i in range(2,100):
    fibo.append(fibo[i-1]+fibo[i-2])

print fibo

for i in range(1,20):
    print i," : ",fibo[2*i-1]*fibo[2*i]

