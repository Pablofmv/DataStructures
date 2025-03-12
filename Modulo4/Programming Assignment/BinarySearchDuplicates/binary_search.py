def binary_search(keys, query):
    A = keys
    key = query
    def binary_serch_duplicates(A,low,high,key):

        mid = low + (high - low) // 2

        if high < low:
            return -1
        
        if A[mid] == key:
            
            if mid == 0 or A[mid-1] < key:
                return mid
            else:
                return binary_serch_duplicates(A,low,mid-1,key)
        elif key < A[mid]:
            return binary_serch_duplicates(A,low,mid-1,key)
        else:
            return binary_serch_duplicates(A,mid+1,high,key)
    
    if not A:
        return -1

    return binary_serch_duplicates(A,0,len(A)-1,key)


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
