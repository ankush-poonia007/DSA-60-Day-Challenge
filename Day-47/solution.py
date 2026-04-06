import heapq
 
class Node:
    def __init__(self, freq, char=None, left=None, right=None, min_idx=float('inf')):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
        self.min_idx = min_idx
 
class Solution:
    def huffmanCodes(self, s, f):
        n = len(s)
        heap = []
        for i in range(n):
            node = Node(f[i], s[i], min_idx=i)
            heapq.heappush(heap, (f[i], i, node))
 
        while len(heap) > 1:
            freq1, idx1, left  = heapq.heappop(heap)
            freq2, idx2, right = heapq.heappop(heap)
            merged_min_idx = min(idx1, idx2)
            merged = Node(freq1 + freq2, left=left, right=right, min_idx=merged_min_idx)
            heapq.heappush(heap, (freq1 + freq2, merged_min_idx, merged))
 
        _, _, root = heap[0]
        result = []
 
        def dfs(node, code):
            if node.left is None and node.right is None:
                result.append(code)
                return
            dfs(node.left,  code + "0")
            dfs(node.right, code + "1")
 
        # Single-node tree: root is already a leaf, assign code "0"
        start_code = "0" if root.left is None and root.right is None else ""
        dfs(root, start_code)
        return result
 
# Example usage:
s = "abc"
f = [5, 9, 12]
solution = Solution()
print(solution.huffmanCodes(s, f))

#output will be ['00', '01', '1'] or any other valid Huffman code representation depending on the structure of the tree.

s = "hello"
f = [10, 20, 30, 40, 50]
print(solution.huffmanCodes(s, f))
#output will be a list of Huffman codes for the characters in "hello" based on their frequencies.