class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # left_bias = True: find the first occurrence of target
        # left_bias = False: find the last occurrence of target
        def binarySearch(nums, target, left_bias):
            left, right = 0, len(nums) - 1
            result = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    result = mid

                    if left_bias:
                        right = mid - 1
                    else:
                        left = mid + 1

            return result

        return [
            binarySearch(nums, target, True),
            binarySearch(nums, target, False)
        ]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
        ([1], 1, [0, 0]),
        ([2, 2, 2, 2], 2, [0, 3])
    ]

    for nums, target, expected in test_cases:
        result = solution.searchRange(nums, target)

        assert result == expected, (
            f"Failed: nums={nums}, target={target}, "
            f"expected={expected}, got={result}"
        )

    print("All tests passed!")