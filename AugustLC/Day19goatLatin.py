class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        return ' '.join([(x if x[0] in vowels else x[1:] + x[0]) + 'ma'+ 'a' * (i + 1) for (i, x) in enumerate(S.split())])
