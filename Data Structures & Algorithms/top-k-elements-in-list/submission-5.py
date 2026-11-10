class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        # for i in nums: //same approach is given below
        #     if i in d:
        #         d[i]+=1
        #     else:
        #         d[i]=1
        f=[[]for i in range(len(nums)+1)]
        for i in nums:
            d[i] =d.get(i,0)+1
        for key,v in d.items():
            f[v].append(key)
        res=[]
        for i in range(len(f)-1,0,-1):
            for j in f[i]:
                res.append(j)
                if len(res)==k:
                    return res


        
        

            