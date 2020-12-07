def evalPoly(a, xData, x):
    n = len(xData) - 1
    p = a[n]
    for k in range(1, n + 1):
        p = a[n - k] + (x - xData[n - k]) * p
    return p


def coeffts(xData, yData):
    m = len(xData)
    a = yData.copy()
    for k in range(1, m):
        for i in range(k, m):
            a[i] = (a[i] - a[k - 1]) / (xData[i] - xData[k - 1])

    return a


xData = [-2, 0, 1, 3]
yData = [8, 4, 2, -2]

a = coeffts(xData, yData)
p = evalPoly(a, xData, x)

print(a)