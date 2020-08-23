#first try is just simple trie, gets TLE bc you need to traverse the whole path every time. big dumb

class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = {}
        self.curr_query = {}
        
        for word in words:
            curr_dict = self.root
            for letter in word:
                if not letter in curr_dict:
                    curr_dict[letter] = {}
                curr_dict = curr_dict[letter]
            curr_dict['isWord'] = True
        
    def query(self, letter: str) -> bool:
        next_query = {}
        flag = False
        for key in self.curr_query:
            searchres = self.wordcheck(key + letter)
            if searchres == 2:
                flag = True
                next_query[key + letter] = 1
            elif searchres == 1:
                next_query[key + letter] = 1
        if letter in self.root:
            if 'isWord' in self.root[letter]:
                flag = True
            next_query[letter] = 1
        self.curr_query = next_query
        return flag
    
    def wordcheck(self, word):
        curr_dict = self.root
        for letter in word:
            if not letter in curr_dict:
                return 0
            curr_dict = curr_dict[letter]
        if 'isWord' in curr_dict:
            return 2
        return 1
