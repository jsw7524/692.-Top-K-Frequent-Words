import heapq
class Solution(object):
    
    def MyCmp(self,x):
        return -x[1],x[0]
    
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        wordsDict={}
        for w in words:
            if w not in wordsDict:
                wordsDict[w]=1
            else:
                wordsDict[w]+=1
        result = heapq.nsmallest(k, [(n[0],n[1]) for n in wordsDict.items()],key=self.MyCmp) 
        return [ r[0] for r in result ]
                
