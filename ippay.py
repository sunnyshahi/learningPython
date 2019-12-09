def piglang(word):
    vowel = ['a','e','i','o', 'u']
    if not word.isalpha():
        return None
    if word[0] not in vowel:
        temp =  word[1:] + word[0] + 'ay'
        return temp
    else:
        return word + 'way'

if __name__ == "__main__":
    print(piglang('pig'))
    print(piglang('apple'))