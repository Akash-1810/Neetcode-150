class Solution(object):
    def groupAnagrams(self, strs):
        d={}
        for i in strs:
            S="".join(sorted(i))
            if S in d:
                d[S].append(i) #if the string is found to be in the sorted list, then we push or add it in the list.
               # d[S]=[i]
            else:
                d[S]=[i] # if the string is not matched then we are check with other strings on the list.
               # d[S].append(i)

        return list(d.values()) 
            

        return d.values()
       
       
        


       