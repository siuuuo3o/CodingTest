def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        arrSum = []
        for j in range(len(arr1[0])):
            arrSum.append(arr1[i][j]+arr2[i][j])
        answer.append(arrSum)
    return answer