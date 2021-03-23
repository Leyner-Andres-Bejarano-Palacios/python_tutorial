#!/usr/bin/python3
# -*- coding: utf-8 -*-
class Solution:
    def defangIPaddr(self, address: str) -> str:
        DefangingIp = ""
        for char in address:
            if char != ".":
                DefangingIp = DefangingIp + char
            else:
                DefangingIp = DefangingIp + "[.]"
        return DefangingIp


solution = Solution()
print(solution.defangIPaddr("1.1.1.1"))