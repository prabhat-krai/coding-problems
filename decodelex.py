"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def decode(lex, dic):
    for i in range(1,3):
        char = lex[i -1]
        print(dic[char])
        decode(lex[i:], dic)












dic = {str(i - 96): str(chr(i)) for i in range(97, 123)}

decode('1123', dic)