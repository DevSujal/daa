def merge_sort(arr, temp, left, right):
    inv_count = 0

    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort(arr, temp, left, mid)
        inv_count += merge_sort(arr, temp, mid + 1, right)
        inv_count += merge(arr, temp, left, mid, right)

    return inv_count

def merge(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
            inv_count += mid - i + 1
            k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for p in range(left, right + 1):
        arr[p] = temp[p]

    return inv_count

def count_overtakes(N, velocities, positions):

    horse_velocity = [0]*N

    for i in range(N):
        horse_velocity[positions[i] - 1] = velocities[i]
    temp = [0] * N
    return merge_sort(horse_velocity, temp, 0, N - 1)

# Sample Input
N = int(input())
velocities = list(map(int, input().split()))
positions = list(map(int, input().split()))

# Sample Output
overtakes = count_overtakes(N, velocities, positions)
print(overtakes)