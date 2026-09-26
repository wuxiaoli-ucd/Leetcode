# groups = [
#     ["a", "b"],
#     ["1", "2"],
#     ["x", "y"]
# ]
#
# ans = []
#
#
# def dfs(index, path):
#     print(f"进入 dfs: index={index}, path={path}")
#
#     if index == len(groups):
#         word = "".join(path)
#         ans.append(word)
#
#         print(f"  到底了！加入答案: {word}")
#         print(f"  准备 return, path={path}")
#         return
#
#     print(f"  当前处理 groups[{index}] = {groups[index]}")
#
#     for char in groups[index]:
#         print(f"\n  准备选择 char='{char}'")
#         print(f"  append 前: path={path}")
#
#         path.append(char)
#
#         print(f"  append 后: path={path}")
#         print(f"  调用 dfs({index + 1}, path)")
#
#         dfs(index + 1, path)
#
#         print(f"  从 dfs({index + 1}, path) 回来了")
#         print(f"  pop 前: path={path}")
#
#         removed = path.pop()
#
#         print(f"  pop 掉 '{removed}'")
#         print(f"  pop 后: path={path}")
#
#     print(f"\n结束 dfs: index={index}, path={path}")
#
#
# dfs(0, [])
#
# print("\n最终答案:")
# print(ans)

class Solution:
    def expand(self, s: str) -> list[str]:
        groups = []
        ans = []

        i = 0
        while i < len(s):
            if s[i] == "{":
                group = []
                i += 1

                while s[i] != "}":
                    if s[i] != ",":
                        group.append(s[i])
                    i += 1
                groups.append(group)

            else:
                groups.append([s[i]])
            i += 1

        def dfs(index, path):
            if index == len(groups):
                letter = "".join(path)
                ans.append(letter)
                return

            for ch in groups[index]:
                path.append(ch)
                dfs(index + 1, path)
                path.pop()

        dfs(0, [])
        ans.sort()
        return ans

# 需要注意的点是，1， 首先是对这项字符串做分层处理 2，然后是注意定义dfs的时候是要return的，3，如何去定义dfs，dfs是从当前状态出发，把所有组合走一遍。
# 1）当前状态是什么 index path，2)什么时候结束-base case  3)当前有哪些选择 4)选完以后去哪里