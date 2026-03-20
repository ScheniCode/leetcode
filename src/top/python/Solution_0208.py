"""
208. 实现 Trie (前缀树)
https://leetcode.cn/problems/implement-trie-prefix-tree/description/?envType=study-plan-v2&envId=top-100-liked

每个节点有26个子节点用来存对应的字母  为None时表示当前位置没有对应的字符串
"""
class Trie:

    def __init__(self):
        self.children = []
        self.end = False
        for i in range(26):
            self.children.append(None)

    def insert(self, word: str) -> None:
        children = self.children
        node = None
        for char in word:
            index = ord(char) - 97
            node = children[index]
            if node is None:
                node = Trie()
                children[index] = node
            children = node.children
        node.end = True

    def search(self, word: str) -> bool:
        children = self.children
        node = None
        for char in word:
            index = ord(char) - 97
            node = children[index]
            if node is None:
                return False
            children = node.children
        return node.end

    def startsWith(self, prefix: str) -> bool:
        children = self.children
        for char in prefix:
            index = ord(char) - 97
            node = children[index]
            if node is None:
                return False
            children = node.children
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':
    trie = Trie()
    trie.insert('apple')
    trie.search('apple')
