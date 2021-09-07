from functools import cache


class Solution:

    def __init__(self):
        self.blocks = []

    def pack_blocks(self, blocks, height):
        self.blocks = blocks
        return self.helper(0, 0, height)

    @cache
    def helper(self, i, curr_width, height):

        widths = []
        while i < len(self.blocks):



