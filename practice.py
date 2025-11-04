from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
          new_nums = nums[:i]+nums[i+1:]
          if all(new_nums[j] < new_nums[j+1] for j in range(len(new_nums)-1)):
            return True
        return False
          
        
          
          
          
my_sol = Solution()

my_sol.canBeIncreasing([1,2,10,5,7])


for i in range(len([1,2,10,5,7])+1):
  print([1,2,10,5,7][i-1])

if all([2, 10, 9, True]):
  print("Ok")
else:
  print("Not Ok!")
  
  
nums = [1, 2 ,4 ,5,6] + [2,4,5, 0]
print(nums)
nums.sort()

nums[:3] + nums[4:]

class Solutions:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        
       out1 = nums1[:m] + nums2[:n]
       out1.sort()
       
       for i in range(len(out1)):
         nums1[i] = out1[i]
       print(nums1)
       
  
            
        
nums1=[2,4,2]
nums2=[6,9,0]         
          
        
my_sol1 = Solutions()

my_sol1.merge(nums1, m=3, nums2=nums2 , n = 3)



class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_list = []
        for i in range(len(nums)):
            if nums[i] != val:
                new_list.append(nums[i])

        for i in range(len(new_list)):
            nums[i] = new_list[i]    
        
        return len(nums), nums
      
      
 
nums = [3, 2,3, 4 ,5 ,3 ,2 ,4 ,3 ,2,1]
repeat = {}

for num in nums:
  repeat[num] = repeat.get(num, 0) + 1

list1= []
list2=[] 
for key, vaue in repeat.items():
  list1.append(key)
  list2.append(vaue)
  
if max(list2) > len(nums)/2:
  return list1[list2.index(max(list2))]
  
  
repeat

 
x = [2, 3, 4 ,5 ,4 ,6 ,7 ,6 ,4 ,5,  8, 54] 
x.sort()
len(x)   

len(x) /2

x[5]
     
  

  

