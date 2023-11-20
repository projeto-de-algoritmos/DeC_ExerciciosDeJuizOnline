from math import hypot

def comp(A, B):
    return A[1] < B[1]

def closest_pair(P):
    n = len(P)
    P.sort(key=lambda point: point[1])
    best = 100000.0
    box = set()
    box.add(P[0])
    left = 0
    for i in range(1, n):
        while left < i and P[i][1] - P[left][1] > best:
            box.discard(P[left])
            left += 1
        for point in box:
            if P[i][0] + best >= point[0]:
                best = min(best, hypot(P[i][1] - point[1], P[i][0] - point[0]))
        box.add(P[i])
    return best

if __name__ == "__main__":
    while True:
        quantidade = int(input())
        if quantidade == 0:
            break
        entrada = []
        for _ in range(quantidade):
            x1, y1 = map(float, input().split())
            entrada.append((y1, x1))
        resultado = closest_pair(entrada)
        if resultado > 10000.0 and abs(resultado - 10000.0) > 1e-5:
            print("INFINITY")
        else:
            print("{:.4f}".format(resultado))