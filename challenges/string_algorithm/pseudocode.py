def find_index(text, pattern):
    starter = 0
    index = 0
    subindex = 0
    while index <= len(text) - 1:
        if text[i] == pattern[subindex]:
            index += 1
            subindex += 1
            return index if subindex == len(pattern) - 1
        
        else:
            subindex = 0
            i = 