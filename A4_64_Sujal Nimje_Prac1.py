import pandas, time, matplotlib.pyplot as plt


# Q1 =>
#  insertion sort
def insertion_sort(arr):
    for x in range(1, len(arr)):
        key = arr[x]
        j = x - 1
        while key < arr[j] and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# # merge sort
def divide(arr, first, last):
    if first < last:
        mid = (first + last) // 2
        divide(arr, first, mid)
        divide(arr, mid + 1, last)
        merge(arr, first, last, mid)


def merge(arr, first, last, mid):
    newarr = []
    x1 = first
    x2 = mid + 1
    while x1 <= mid and x2 <= last:
        if arr[x1] < arr[x2]:
            newarr.append(arr[x1])
            x1 += 1
        else:
            newarr.append(arr[x2])
            x2 += 1

    newarr.extend(arr[x1 : mid + 1])
    newarr.extend(arr[x2 : last + 1])
    arr[first : last + 1] = newarr


def mergesort(arr):
    divide(arr, 0, len(arr) - 1)


data = pandas.read_csv("data.csv")
data1 = list(data["numbers"])
data2 = list(data["numbers"])

start = time.perf_counter()
insertion_sort(data1)
end = time.perf_counter()
print("Array is sorted using insertion sort -> ")
print(data1)
insertion_time = end - start

start = time.perf_counter()
mergesort(data2)
end = time.perf_counter()
merge_time = end - start
print("\nArray is sorted using merge sort -> ")
print(data2)
print("\nThe time taken by insertion sort to sort 500 numbers is : ", insertion_time)
print("The time taken by merge sort to sort 500 numbers is : ", merge_time)
print(
    "the minimum number in data = ",
    min(data1),
    "the maximum number in data =",
    max(data1),
)


time_data = pandas.DataFrame({
   "insertion sort": insertion_time,
    "merge sort" : merge_time
    },
      index=[""]
)
time_data.plot(kind="bar", color = ["red","green"])
plt.xlabel("Execution Time")
plt.ylabel("Time (seconds)")
plt.title("Comparison of Insertion Sort and Merge Sort")
plt.legend(title="Sorting Algorithm")
plt.show()



# Q2 =>
def put_john_age_mid(arr, john_age):
    arr.append(john_age)
    mergesort(arr)
    john_post = arr.index(john_age)
    left_arr = arr[0:john_post]
    right_arr = arr[(john_post + 1) : len(arr)]

    left_length = len(left_arr)
    right_length = len(right_arr)
    if left_length == right_length:
        return arr
    elif left_length > right_length:
        make_left_equal(left_arr, right_arr, left_length, right_length, john_age)
    else:
        make_right_equal(left_arr, right_arr, left_length, right_length, john_age)

    arr = left_arr
    arr.append(john_age)
    arr.extend(right_arr)
    return arr


def make_left_equal(left_arr, right_arr, left_length, right_length, john_age):
    choice = int(
        input(
            "would you like to add a student or delete write 1 for add and 0 for delete : "
        )
    )

    if choice == 0:
        print(
            "we discarded",
            left_length - right_length,
            "students to place john at middle",
        )
        while left_length > right_length:
            left_arr.pop(0)
            left_length = len(left_arr)

    else:
        print(
            "we invited", left_length - right_length, "students to place john at middle"
        )
        while left_length > right_length:
            if len(right_arr) == 0:
                right_arr.append(john_age + 1)
                right_length += 1
                continue
            right_arr.append(right_arr[right_length - 1] + 1)
            right_length += 1


def make_right_equal(left_arr, right_arr, left_length, right_length, john_age):
    choice = int(
        input(
            "would you like to add a student or delete write 1 for add and 0 for delete : "
        )
    )
    if choice == 0:
        print(
            "we discarded",
            right_length - left_length,
            "students to place john at middle",
        )
        while right_length > left_length:
            right_arr.pop()
            right_length -= 1

    else:
        print(
            "we invited", right_length - left_length, "students to place john at middle"
        )

        while right_length > left_length:
            if len(left_arr) == 0:
                if john_age <= 1:
                    left_arr.append(john_age)
                else:
                    left_arr.append(john_age - 1)

                left_length += 1
                continue

            if left_arr[0] <= 1:
                append_value = 0
            else:
                append_value = 1
            left_arr.append(left_arr[0] - append_value)
            left_length += 1


print("\nQ2 -> \n")
john_age = int(input("enter the age of john : "))

age_list = list(input("enter the ages of other students : ").split(" "))
age_list = [int(x) for x in age_list]
age_list = put_john_age_mid(age_list, john_age)
print("the sorted list after putting John's age at middle position is : ", age_list)
