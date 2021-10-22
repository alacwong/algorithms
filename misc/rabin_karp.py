def search(s: str, t: str) -> bool:
    """
    check if t is a substring of t in O(s + t) time O(st) on bad hash
    """

    t_hash = sum(list(map(ord, t)))
    s_hash = 0

    for idx, char in enumerate(s):
        s_hash += ord(char)

        # abcde
        if idx >= len(t):
            s_hash -= ord(s[idx - len(t)])

        # abc => 2
        if s_hash == t_hash and s[idx + 1 - len(t): idx + 1] == t:
            return True

    return False


if __name__ == '__main__':
    print(search('hello world', 'whor'))
    print(search('hello world', 'world'))
