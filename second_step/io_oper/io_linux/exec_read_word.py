"""
    从终端输入单词，
    打印出该单词及解释，
    若没有则打印找不到
"""


def search_word(word):
    f = open('dict.txt')
    f.seek(0,0)
    for line in f:
        # 如果遍历到的单词大于word结束查找
        # print(line.split())
        if line.split()[0] > word:
            f.close()
            return "No this word"
        elif word == line.split()[0]:
            f.close()
            return line
    else:
        f.close()
        return "No this word"

# print(search_word("abash"))





