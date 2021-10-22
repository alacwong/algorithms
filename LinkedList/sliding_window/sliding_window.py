def smallest_subarray_with_given_sum(s, arr):
    left = right = 0
    t = s
    n = len(arr)
    ans = 0
    while right < n:
        t += arr[right]
        right += 1
        while t > s and left < right:
            t -= arr[left]
            left += 1
        ans = max(right - left, ans)
    return ans

if __name__ == '__main__':
    print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]))
