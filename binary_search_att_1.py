
arr = [1,2,3,4,5,6,7,8,9,10]

num = int(input("Enter a num between 1 and 10: "))

guess = round(len(arr) / 2)
count = 0
while guess != num and count != 12:
    if guess == num:
        print("you entered: {} num of hops to find: {}".format(num, count))
    if num > guess:
        prev = guess
        guess = guess + round(((arr[len(arr)-1] - guess ) / 2)) + 1
        
    elif num < guess:
        holding = guess
        guess = guess - round(((arr[len(arr)-1] - guess ) / 2)) + 1
        
    print(guess)

    if count >= 11:
        print("err number not found")
        
    count+=1