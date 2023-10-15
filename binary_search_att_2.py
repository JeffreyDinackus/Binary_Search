def search(arr, low, high, guess):

  

  while low <= high:
    mid = low + (high - low) // 2
    print(guess, low, mid,  high)

    if mid == guess:
      return mid

    elif arr[mid] < guess:
      print("x")
      low = mid + 1
    else:
      high = mid - 1
  return -1
if __name__ == '__main__':
  arr = [2, 3, 4, 10, 40,50,60]
  guess = 4



  print(search(arr, 0, len(arr)-1, guess))

