def data():
    import nltk
    import pyphen
    nltk.download('words')
    nltk.download('punkt')
    nltk.download('wordnet')
    from nltk.corpus import words
    from nltk.corpus import wordnet

    def count_syllables(word):
        dic = pyphen.Pyphen(lang='en_US')
        return len(dic.inserted(word).split('-'))

    def word_bank():
        word_list = words.words()

        # Filtering words of about 4 to 8 characters and with no more than 4 syllables
        filtered_words = [word for word in word_list
                          if 4 <= len(word) <= 8 and count_syllables(word) <= 4]

        vocabulary = []

        for word in filtered_words:
            synsets = wordnet.synsets(word)
            if any(s.pos() == 'a' for s in synsets):
                vocabulary.append(word)
            if any(s.pos() == 'n' for s in synsets):
                vocabulary.append(word)

        with open("vocabulary.txt", "w") as file:
            file.write("\n".join(vocabulary))
            print("Word bank created")
    word_bank()
