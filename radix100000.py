import time
startTime = time.time()

def radixSort(list):
    maxLength = len(str(max(list)))
    for i in range(maxLength):
        buckets = [[] for _ in range(10)]
        for j in list:
            buckets[int(j/(10**i))%10].append(j)
        list = [num for bucket in buckets for num in bucket]
    return list

def main():
    file = open("100000likliste 4.txt", "r")
    list = file.readlines()
    maxLength = 3

    for i in range(len(list)):
        list[i]=int(float(list[i])*(10**maxLength))
    print(list)
    sorted = radixSort(list)
    
    for i in range(len(sorted)):
        sorted[i] = float(sorted[i]/(10**maxLength))
        if sorted[i] == int(sorted[i]):
            sorted[i] = int(sorted[i])
    print(sorted)

    print("--- %s saniye ---" % (time.time() - startTime))

main()