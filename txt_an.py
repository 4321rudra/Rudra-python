import string

class TextAnalyzer:

    def __init__(self, text):

        for p in string.punctuation:
            text = text.replace(p, " ")

        self.text = text.lower()

    def freqAll(self):

        words = self.text.split()
        frequency = {}

        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1

        return frequency

    def freqof(self, word):
        frequency = self.freqAll()
        print(f"Frequency of '{word}' : {frequency.get(word.lower(), 0)}")


strr = "Hello, My Name is Rudra! My name is Rudra."

obj = TextAnalyzer(strr)

a = obj.freqAll()

for key, value in a.items():
    print(f"{key} : {value}")

obj.freqof("my")
obj.freqof("rudra")