data = [
    [2.36, 0.85866],
    [2.37, 0.86289],
    [2.38, 0.86710],
    [2.39, 0.87129]
]
def prime_pov_1(dataList, h):
    return (-3 * dataList[0][1] + 4 * dataList[1][1] - dataList[2][1]) / (2 * h)
def prime_pov_2(dataList, h):
    return (2 * dataList[0][1] -5 * dataList[1][1] + 4 * dataList[2][1] - dataList[3][1]) / h**2
h = data[1][0] - data[0][0]
print("f'(2,36) is ")
print(prime_pov_1(data, h))
print("\nf''(2.36) is")
print(prime_pov_2(data, h))