arr = [5, 10, 17, 39, 48, 0, 84]
for i in range(len(arr)):
    if arr[i] % 2 and arr[i] >= 10:
        arr[i] = int(arr[i] / 10)
    elif arr[i] % 2:
        arr[i] = -1
    else:
        str1 = str(arr[i])
        str2 = ''
        for j in str1:
            str2 += j * 2
        arr[i] = int(str2)
print("Ваш список", arr)
