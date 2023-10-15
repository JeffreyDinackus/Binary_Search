def Search(arr, l, r, x):
 
    while l <= r:
 
        mid = l + (r - l) // 2
 
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
 
        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1
 
        # If x is smaller, ignore right half
        else:
            r = mid - 1
 
    # If we reach here, then the element
    # was not present
    return -1
 

  

 
if __name__ == '__main__':
  arr = [2, 3, 4, 10, 40,50,60]
  guess = 4



  print(Search(arr, 0, len(arr)-1, guess))

