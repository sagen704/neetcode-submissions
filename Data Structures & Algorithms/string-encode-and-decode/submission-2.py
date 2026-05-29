class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = ""

        for word in strs:
            encoded_str = encoded_str + str(len(word)) +"#"  + word
            
        return encoded_str

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0
        while i < len(s):
            j = i
            
            while s[j] != "#":
                j += 1
            
            length_word = int(s[i:j])
            # move window 
            j += 1
            res.append(s[j: j+length_word])
            
            i = j+length_word
        
        return res

        

 

                
                


