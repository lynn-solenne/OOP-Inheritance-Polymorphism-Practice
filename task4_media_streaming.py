#Media Streaming System-Multilevel inheritance+Method overriding+polymorphism
class Media:
    def __init__(self,title):
        self.title=title
    def play(self):
        print("Playing media: ",self.title)
class Audio(Media):
    def __init__(self,title,duration):
        super().__init__(title)
        self.duration=duration
    def play(self):
        print(f"Playing audio: {self.title} - {self.duration} minutes")
class Podcast(Audio):
    def __init__(self,title,duration,host):
        super().__init__(title,duration)
        self.host=host
    def play(self):
        print(f"Playing podcast: {self.title} hosted by {self.host}")
media=Media("Python Basics")
audio=Audio("Relaxing Music",4)
podcast=Podcast("AI Today",30,"John")
media.play()
audio.play()
podcast.play()


