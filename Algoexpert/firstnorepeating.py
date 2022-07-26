def firstNonRepeatingCharacter(string):
    characterFriequencies = {}
    for character in string:
        if character not in characterFriequencies:
            characterFriequencies[character] = 0
        
        characterFriequencies[character] += 1
    
    for idx in range(len(string)):
        character = string[idx]
        if characterFriequencies[character] == 1:
            return idx
    return -1

input = "abcdcaf"
print(firstNonRepeatingCharacter(input))