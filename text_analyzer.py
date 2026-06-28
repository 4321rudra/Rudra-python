import string
class text_analyzer(object):
    def __init__(self,text):
        
        for p in string.punctuation:
            text=text.replace(p," ")
        # text.split()
        self.text=text.lower()

    def freqAll(self):
        words=self.text.split()
        frequency={}
        for word in words:
            if word in frequency:
                frequency[word]+=1
            else:
                frequency[word]=1
        return frequency
    def freqof(self,word):
        frequency=self.freqAll()
        print(f"Frequency of {word} : {frequency.get(word.lower())}")
strr = "Hello, My Name is Rudra! My name is Rudra."
a=text_analyzer(strr)
obk=a.freqAll()
for key, value in obk.items():
    print(f"{key} : {value}")
