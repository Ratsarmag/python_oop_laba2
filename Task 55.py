class Text():
    
    def __init__(self, text):
        self.text = text

    def getLength(self):
        return len(self.text)

    def getLettersCount(self):
        counter = 0
        for s in self.text:
            if s.isalpha():
                counter += 1
        return counter
    
    def getSpacesCount(self): 
        counter = 0
        for s in self.text:
            if s == " ":
                counter += 1
        return counter

    def getLengthWithoutSpaces(self): 
        return self.getLength() - self.getSpacesCount()

    def getWords(self):
        return self.text.split()

    def getSentences(self):
        return self.text.split('.' or '!' or '?')


text = Text("Данная строка является техническим экспериментом. Торт - это ложь! 420")

print(text.getLength())
print(text.getLettersCount())
print(text.getSpacesCount())
print(text.getLengthWithoutSpaces())
print(text.getWords())
print(text.getSentences())