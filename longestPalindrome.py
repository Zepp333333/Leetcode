class Solution:
    def longestPalindrome(self, s: str) -> str:


        def find_substrings(s: str, n: int) -> list:
            result = []
            for i in range(len(s) - (n - 1)):
                if is_palindrome(s[i:i+n]):
                    result.append(s[i:i+n])
            return result

        def find_all_substrings(s: str) -> list:
            result = []
            for i in range(len(s), 1, -1):
                t = find_substrings(s, i)
                if t:
                    return t
            return result

        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        strings = find_all_substrings(s)
        if strings:
            return strings[0]
        return s[0]


sol = Solution()
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome('cbbd'))
print(sol.longestPalindrome('a'))
print(sol.longestPalindrome("jcwwnkwiajicysmdueefqjnrokunucidhgkswbgjkkrujkxkxeanrpjvpliomxztalhmvcldnqmkslkprhgtwlnsnygbzdvtdbsdzsdjggzgmhogknpfhtgjmclrkgfqdbiagwrqqcnagosnqrnpapxfrtrhzlyhszdtgkqggmewqmwugrbufiwfvtjhczqgcwpcyjioeacggiwyinpkyxrpxhglrtojgjmmswxnvirfsrbhmpqgjyyagjqfwkqkjkumywvgfutmiwihwnnhbfxcijaoiyxbdnrckexqfhsmmxflaneccyaoqoxfbaylcvvpfafsikebzcdufvhluldguwsmrtjaljpcjestranfrvgvytozxpcvnwquhnsxlmzkehwopgxvifajmrlwqiqylgxibnypxwpkggxevyfoxywfsfpjbzfxxysgxgwxrzkwdqlkrpajlltzqfqshdokibakkhydizsgwbygqulljqmtxkwepitsukwjlrrmsjptwabtlqytprkkuxtqdmptctkfabxsohrfrqvrbjfbppfkpthosveoppiywkkuoasefviegormlqkqlbhnhblkmglxcbszblfipsyumcrjrkrnzplkveznbtdbtlcptgswhiqsjugqrvujkzuwvoxbjremyxqqzxkgerhgtidsefyemtmstsznvgohexdgetqbhrxaomzsamapxhjibfvtbquhowyrwyxthpwvmfyyqsyibemnfbwkddtyoijzwfxhossylygxmnznpegtgvlrsreepkrcdgbujkghrgtsxwlvxrgrqxnvgqkppbkrxjupjfjcsfzepdemaulfetn"))
