import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

"""
for (int i = 0; i < n; i++) {
    // Track number of elements swapped during a single array traversal
    int numberOfSwaps = 0;

    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
            numberOfSwaps++;
        }
    }

    // If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0) {
        break;
    }
}
"""
numberOfSwaps = 0
for i in range(n):

    for j in range((n - 1)):
        if a[j] > a[j + 1]:
            index1 = a.index(a[j])
            index2 = a.index(a[j + 1])
            a[index1], a[index2] = a[index2], a[index1]
            numberOfSwaps += 1

    if numberOfSwaps == 0:
        break

print("Array is sorted in {} swaps.".format(numberOfSwaps))
print("First Element:", a[0])
print("Last Element:", a[n - 1])