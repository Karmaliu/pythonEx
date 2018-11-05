class Song(object):
    def __init__(self, song_text):
        self.song_text = song_text
        self.name = 'zzzz'

    def sing_me_a_song(self):
        for line in self.song_text:
            print(line)


happy_boday = Song(["Happy birthday to you "])

bulls_on_parade = Song(["They rally around the family"])


happy_boday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

print(happy_boday.song_text)