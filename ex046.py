from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('\033[1;33m-*' * 15)
print('\033[1;36mPOW!   POW!   POOOOW!   BUUMM!')
print('\033[1;31m-*' * 15)