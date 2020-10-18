class place:
    def __init__(self, name, country, priority, visited):
        self.name = name
        self.country = country
        self.priority = priority
        self.visited = visited
        if self.priority <= 2:
            self.important = True
        else:
            self.important = False

    def __str__(self):
        if self.visited:
            return "{} in {}, priority {} (visited)".format(self.name, self.country, self.priority)
        elif not self.visited:
            return "{} in {}, priority {}".format(self.name, self.country, self.priority)
