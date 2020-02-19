class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punc = ["!", "?", "'", ",", ";", "."]
        ms = collections.Counter()
        
        paragraph = paragraph.lower()
        for i in punc: 
            paragraph = paragraph.replace(i, ' ')

        paragraph = paragraph.split()
        
        for i in range(len(paragraph)):
            if paragraph[i] not in banned:
                ms.update([paragraph[i]])
        
        return ms.most_common(1)[0][0]