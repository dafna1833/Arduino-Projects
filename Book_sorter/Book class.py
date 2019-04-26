class Book:
    def __init__(self, title, location):
        self.title = title
        self.location = location

    def description(self):
        return "{}, {}".format(self.title, self.location)


        
