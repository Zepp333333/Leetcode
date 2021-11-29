import random
import string

class Codec:

    def __init__(self):
        self.urls = {}

    def encode(self, longUrl: str) -> str:
        code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        tiniurl = f"http://tiniyrl.com/{code}"
        self.urls[tiniurl] = longUrl
        return tiniurl

    def decode(self, shortUrl: str) -> str:
        return self.urls[shortUrl] if shortUrl in self.urls else None

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

c = Codec()
r = c.decode(c.encode("https://leetcode.com/problems/design-tinyurl"))
assert r == "https://leetcode.com/problems/design-tinyurl"
