n = int(input())

half = n/2

if n <= 0 or n > 1000:
  return -1

nums = [int(n) for num in input().split(' ')]

nums.sort()
if nums[:half] == nums[half:]:
  nums[-1],  nums[0] = nums[0], nums[-1]
  if nums[:half] == nums[half:]:
    return -1
  else:
    return nums
  
return nums