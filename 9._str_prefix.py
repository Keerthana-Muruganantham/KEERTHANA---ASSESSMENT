arr = ["abcdef" , "abcd", "abcdgs" ]
if not arr:
  print("There is no common prefix for the given array")

elif len(arr) == 1:
  print("The longest common prefix:", arr[0])
else:
  arr.sort()
  result = ""
  for i in range(len(arr[0])):
    if arr[0][i] == arr[-1][i]:
          result += arr[0][i]

    else:
          break
  print("The longest common prefix is:", result)



