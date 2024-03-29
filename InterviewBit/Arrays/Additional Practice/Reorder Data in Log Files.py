# You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

# There are two types of logs:
# Letter-logs: All words (except the identifier) consist of lowercase English letters.
# Digit-logs: All words (except the identifier) consist of digits.

# Reorder these logs so that:
# The letter-logs come before all digit-logs.
# The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
# The digit-logs maintain their relative ordering.

# Return the final order of the logs.

# Problem Constraints
# 1 <= logs.length <= 1000
# 3 <= logs[i].length <= 1000

# All the tokens of logs[i] are separated by a single space.
# logs[i] is guaranteed to have an identifier and at least one word after the identifier.

# Input Format
# The first argument is a string array A where each element is a log.

# Output Format
# Return the string array A after making the changes.

# Example Input
# Input 1:
# A = ["dig1-8-1-5-1", "let1-art-can", "dig2-3-6", "let2-own-kit-dig", "let3-art-zero"]
# Input 2:
# A = ["a1-9-2-3-1","g1-act-car","zo4-4-7","ab1-off-key-dog","a8-act-zoo"]

# Example Output
# Output 1:
# ["let1-art-can","let3-art-zero","let2-own-kit-dig","dig1-8-1-5-1","dig2-3-6"]
# Output 2:
# ["g1-act-car", "a8-act-zoo", "ab1-off-key-dog", "a1-9-2-3-1", "zo4-4-7"]

# Example Explanation
# Explanation 1:
# The letter-log contents are all different, so their ordering is "art-can", "art-zero", "own-kit-dig".
# The digit-logs have a relative order of "dig1-8-1-5-1", "dig2-3-6".
# Explanation 2:
# The array has been sorted restricted to the conditions given.

class Solution:
    # @param A : list of strings
    # @return a list of strings
    def reorderLogs(self, A):
        let_log = []
        dig_log = []
        
        for log in A:
            if (log.split('-')[1]).isdigit():
                dig_log.append(log)
            
            else:
                let_log.append(log.split('-'))
        
        let_log.sort(key = lambda x:x[0])
        let_log.sort(key = lambda x:x[1:])
        
        for i in range(len(let_log)):
            let_log[i] = '-'.join(let_log[i])
        
        return let_log + dig_log