class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if not word:
            return
        else:
            d = self.root
            for i in range(len(word)):
                if word[i] in d:
                    continue
                else:
                    d[word[i]] = {}
                d = d[word[i]]
        d['isWord'] = True
                    

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        flag = [False]
        
        def bfs(curr_word, curr_d):
            if flag[0] == True:
                return
            if not curr_word:
                flag[0] = 'isWord' in curr_d
            for i in range(len(curr_word)):
                if curr_word[i] == '.':
                    all_keys = curr_d.keys()
                    for key in all_keys:
                        if key == 'isWord':
                            if i == len(curr_word) - 1:
                                flag[0] == True
                            continue
                        else:
                            return bfs(curr_word[i+1:], curr_d[key])
                elif curr_word[i] in curr_d:
                    curr_d = curr_d[curr_word[i]]
                else:
                    return

            flag[0] = 'isWord' in curr_d
        
        bfs(word, self.root)
        
        return flag[0]
