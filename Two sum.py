nums=[1,5,4,3,6] # here were takin this example
target=9 # target
for i in range(len(nums)):
    for j in range(i+1,len(nums):
        if nums[i]+nums[j]==target:
            print([i,j])
