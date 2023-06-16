class Solution:
    def twoSum(self,List,target):
        for i in range(len(List)):
            for j in range(i+1,len(List)):
                if List[i]+List[j]==target:
                    return i,j

if __name__ == "__main__":
    list=input()
    target=int(input())
    arr=[int(i) for i in list.split()]
    sol=Solution()
    i,j=sol.twoSum(arr,target)
    indices=[i,j]
    print(indices)
