#存在在键盘每一行的单词
#for循环可以直接扫面字符串的每一个字母
class Solution:
    def findWords(words):
        row_1 = ["q","w","e","r","t","y","u","i","o","p","Q","W","E","R","T","Y", "U","I","O","P"]
        row_2 = ["A","S","D","F","G","H","J","K","L","a","s","d","f","g","h","j","k","l"]
        row_3 = ["z","x","c","v","b","n","m","Z","X","C","V","B","N","M"]
        res = []
        for word in words:
            cnt1 = cnt2 = cnt3 = 0
            for letter in word:
                if letter in row_1:
                    cnt1 += 1 
                elif letter in row_2:
                    cnt2 += 1
                elif letter in row_3:
                    cnt3 += 1
            if cnt1 == len(word) or cnt2 == len(word) or cnt3 == len(word):
                res.append(word)
        return res
words = ["Hello","Alaska","Dad","Peace"]
print(Solution.findWords(words))