class Solution:

    def encode(self, strs: List[str]) -> str:
        mystring=""
        for i in range(len(strs)):
            length=str(len(strs[i]))
            mystring+=length+'#' +strs[i]
        return mystring

        


    def decode(self, s: str) -> List[str]:
        mylist=[]
        i=0
        j=0
        while i<len(s):
            if s[i]=="#":
                length=int(s[j:i])
                mylist.append(s[i+1:i+length+1])
                i=length+i+1
                j=i
            
            else:
                i+=1
        return mylist


