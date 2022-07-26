'''
def isPalindrome(string):
    # Write your code here.
    reversedChars = []
    #reversed で逆からイテレート可能
    for i in reversed(range(len(string))):
        reversedChars.append(string[i])
    return string == "".join(reversedChars)
'''

def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True

if isPalindrome("abcdccba"):
    print("Yes")
else:
    print("No")