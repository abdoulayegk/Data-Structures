"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any
positions ) so that the resulting parentheses string is valid and return any
valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid
strings, or It can be written as (A), where A is a valid string.
"""


class Solution:
    def minRemoveToMakeValid(self, S: str) -> str:
        S, stack = list(S), []
        for i, c in enumerate(S):
            if c == ")":
                if stack:
                    stack.pop()
                else:
                    S[i] = ""
            elif c == "(":
                stack.append(i)
        for i in stack:
            S[i] = ""
        return "".join(S)