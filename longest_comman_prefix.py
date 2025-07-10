class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        strs.sort()

        first_str = strs[0]
        last_str = strs[-1]

        comman_prefix = []

        for i in range (len(first_str)):
            if i < len(last_str) and first_str[i] == last_str[i]:
                comman_prefix.append(first_str[i])
            else:
                break
        return "".join(comman_prefix)


        