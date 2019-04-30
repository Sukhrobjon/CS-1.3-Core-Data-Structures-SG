from set import Set

class Redact(object):
    def redact_words(self, words, banned_words):
        "Returns words excluding banned words"
        # words_set = set(words)
        banned_words_set = Set(banned_words)
        cleaned_words = [word for word in words if not banned_words_set.contains(word)]
        
        return cleaned_words
    

if __name__ == "__main__":
    print("hello")