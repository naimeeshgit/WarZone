import time
target = []
target.append(10)
target.append(20)
target.append(30)

t = time.time()
for i in target:
    print(i)

a = 'a'
b = "a"

if(a == b):
    print("a == b")

time.sleep(1)

t = time.time() - t
print(t)



