#给定一个单词列表，每个单词可以写成每个字母对应摩尔斯密码的组合。
#例如，"cab" 可以写成 "-.-..--..."，(即 "-.-." + ".-" + "-..." 字符串的结合)。我们将这样一个连接过程称作单词翻译。
#返回我们可以获得所有词不同单词翻译的数量。

#ord(): asc码
class Solution:
    def uniqueMorseRepresentations(words) -> int:
        from collections import Counter
        res = []
        mos = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for _ in words:
            tmp = ""
            for i in _:
                tmp = tmp + mos[ord(i)-97]
            res.append(tmp)
        res = Counter(res)
        return len(res)
words = ["gin","zen","gig","msg"]
print(Solution.uniqueMorseRepresentations(words))