def pattern1():
    print("***************************\n\
* ** ** ** ** ** ** ** ** *\n\
***************************")

def pattern2():
    print("***   ******   ******   ***\n\
* *   * ** *   * ** *   * *\n\
***   ******   ******   ***")

def pattern3():
    print("*********         *********\n\
* ** ** *         * ** ** *\n\
*********         *********")


N = int(input())

index = N // 3

for i in range(1, index + 1):
    pattern1()