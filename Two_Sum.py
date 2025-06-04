#This Code returns the index number of the two values of the list that sums up to the target variable.

nums = [2,7,11,15]
target = 18
lst = []
found = "not_found"

for i in range(len(nums)):
    for j in range(len(nums)):
        if i!=j and target == nums[i]+nums[j]:
            lst.append(i)
            lst.append(j)
            found = "found"
            break
    if found == "found":
        break

print(lst)
