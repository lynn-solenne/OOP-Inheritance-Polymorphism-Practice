#file Processing system +Inheritance+Runtime polymorphism
class FileProcessor:
    def __init__(self,filename):
        self.filename=filename
    def process(self):
        print("Processing File ...")
class TextFile(FileProcessor):
    def process(self):
        print("Processing text file:",self.filename)
class ImageFile(FileProcessor):
    def process(self):
        print("Processing image file:",self.filename)
class AudioFile(FileProcessor):
    def process(self):
        print("Processing audio file:",self.filename)
Text=TextFile("notes.txt")
Image=ImageFile("photo.jpg")
Audio=AudioFile("song.mp3")
files=[Text,Image,Audio]
for file in files:
    file.process()

