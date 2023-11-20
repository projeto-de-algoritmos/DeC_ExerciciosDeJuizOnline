def merge_and_count_inversions(arr, left, mid, right):
    inv_count = 0
    n1 = mid - left + 1
    n2 = right - mid

    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            inv_count += n1 - i
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    return inv_count

def merge_sort_and_count_inversions(arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count_inversions(arr, left, mid)
        inv_count += merge_sort_and_count_inversions(arr, mid + 1, right)
        inv_count += merge_and_count_inversions(arr, left, mid, right)

    return inv_count

def train_swaps(L, carriages):
    swaps = merge_sort_and_count_inversions(carriages, 0, L - 1)
    return swaps


N = int(input())

for _ in range(N):
    L = int(input())
    carriages = list(map(int, input().split()))

    swaps = train_swaps(L, carriages)

    print(f'Optimal train swapping takes {swaps} swaps.')

