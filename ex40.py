class Song(object):

   def __init__(self, lyrics):
      self.lyrics = lyrics

   def sing_me_a_song(self):
      for line in self.lyrics:
         print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pocket full of shells"])

one_more_time = Song(["Second verse same as the first"])

lets_see = Song(["how does this work", "lets see", "a comma means next line"])


happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

one_more_time.sing_me_a_song()

lets_see.sing_me_a_song()
