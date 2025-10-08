class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root


from collections import deque


def print_tree(root):
    if not root:
        return "[]"

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")

    while result and result[-1] == "null":
        result.pop()

    return str(result)


solution = Solution()
nums1 = [-10, -3, 0, 5, 9]
nums2 = [1, 3]

tree1 = solution.sortedArrayToBST(nums1)
tree2 = solution.sortedArrayToBST(nums2)

print(print_tree(tree1))  # Output: [0, -3, 9, -10, null, 5]
print(print_tree(tree2))  # Output: [3, 1]
