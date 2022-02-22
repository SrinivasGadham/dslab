def contains(text, pattern):
    for i in range(len(text)):
        for j in range(len(pattern)):
            if i + j >= len(text):
                break
            if text[i + j] != pattern[j]:
                break
        else:
            return True
    return False