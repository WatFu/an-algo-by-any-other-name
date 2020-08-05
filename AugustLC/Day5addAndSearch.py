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
                if not word[i] in d:
                    d[word[i]] = {}
                d = d[word[i]]
        d['isWord'] = True
                    

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        flag = [False]
        
        def dfs(curr_word, curr_d):
            if flag[0] == True:
                return
            if not curr_word:
                flag[0] = 'isWord' in curr_d
                return
            if curr_word[0] == '.':
                all_keys = list(curr_d.keys())
                if len(all_keys) == 1 and all_keys[0] == 'isWord':
                    return
                for key in all_keys:
                    if key != 'isWord':
                        dfs(curr_word[1:], curr_d[key])
            elif curr_word[0] in curr_d:
                dfs(curr_word[1:], curr_d[curr_word[0]])
            else:
                return
        
        dfs(word, self.root)
        
        return flag[0]
