class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        n = len(characters)
        self.arr = []
        
        for i in range(1<<n):
            curr_word = ''
            for j in range(n):
                mask = 1 << j
                if mask & i != 0:
                    curr_word += characters[j]
            if len(curr_word) == combinationLength:
                self.arr.append(curr_word)
        
        self.arr.sort()
        self.maxcounter = len(self.arr)
        self.counter = 0
        
    def next(self) -> str:
        self.counter += 1
        return self.arr[self.counter - 1]

    def hasNext(self) -> bool:
        return self.counter < self.maxcounter
        
