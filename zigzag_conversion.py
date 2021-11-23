class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        def zigzag():
            word_size = numRows
            result = []
            index = 0

            def read(s :str, index: int, word_size:int):
                return s[index:index+word_size]

            def write(chunk: str, word_size:int):
                if word_size == numRows:
                    result.append(chunk + (numRows - len(chunk)) * '_')
                else:
                    chunk_size = len(chunk)
                    prepend_size = numRows - chunk_size - 1
                    new_chunk = (prepend_size * '_') + chunk[::-1] + '_'
                    result.append(new_chunk)

            while True:
                chunk = read(s, index, word_size)
                write(chunk, word_size)
                index += word_size
                if index >= len(s):
                    break
                word_size = numRows - 2 if word_size == numRows else numRows
            print(result)

            return result

        def combine(lst):
            print(lst)
            result = []
            for i in range(numRows):
                for chunk in lst:
                    result.append(chunk[i])
            result_str = ''.join(result)
            return result_str.replace("_", "")

        if numRows == 1:
            return s

        return combine(zigzag())




s = "PAYPALISHIRING"


sol = Solution()

numRows = 3
r = sol.convert(s, numRows)
print(r)
assert r == "PAHNAPLSIIGYIR"
numRows = 4
r = sol.convert(s, numRows)
print(r)
assert r == "PINALSIGYAHRPI"
numRows = 1
r = sol.convert('ABc', numRows)
print(r)
