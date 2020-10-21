class place:
    def __init__(self, name, country, priority, visited):
        # //Method to define variables for class's object
        self.important = False
        self.country = country
        self.name = name
        self.visited = visited
        self.priority = priority
        if self.priority <= 2:
            self.important = True

    def __getitem__(self, item):
        return getattr(self, item)

    def __str__(self):
        # //Method to return correct string annotation
        if self.visited:
            return "{} in {}, priority {} (visited)".format(self.name, self.country, self.priority)
        elif not self.visited:
            return "{} in {}, priority {}".format(self.name, self.country, self.priority)
