def insertion_sort(A: int):
    """Insertion sort algorithm implementation"""
    for i in range(1, len(A)):
        """At iterationi, the algorithm may be required to moveielements, so the
        total runtime is roughly ∑ni=1i=n(n+1)2=O(n2)."""
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A


A = [6, 4, 1, 3, 7, 5]
print(insertion_sort(A))
