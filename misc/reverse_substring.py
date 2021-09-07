"""
Given a string str that consists of lower case English letters and brackets.
The task is to reverse the substrings in each pair of matching parentheses,
starting from the innermost one. The result should not contain any brackets.

Examples:

Input: str = “(skeeg(for)skeeg)”
Output: geeksforgeeks

Input: str = “((ng)ipm(ca))”
Output: camping
"""


def reverse(s: str):
    """
    ((ng)ipm(ca))

    ( -> reverse( '(ng)ipm(ca)' )

     s =  [ '', 'ng'] -> ['gn']

     [ 'gnipm', 'ca'] -> ca

     'gnimpca
    """

    stack = []
    current = ''
    for char in s:

        if char == '(':
            stack.append(current)
            current = ''
        elif char == ')':
            current = stack.pop() + current[::-1]
        else:
            current += char

    return current


if __name__ == '__main__':

    print(reverse('hi'))
    print(reverse('((ng)ipm(ca))'))
    print(reverse('yo(skeeg(for)skeeg)'))
