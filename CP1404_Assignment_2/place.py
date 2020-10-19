class place:
    def __init__(self, name, country, priority, visited):
        self.important = False
        self.country = country
        self.name = name
        self.visited = visited
        self.priority = priority
        if self.priority <= 2:
            self.important = True

    def __str__(self):
        if self.visited:
            return "{} in {}, priority {} (visited)".format(self.name, self.country, self.priority)
        elif not self.visited:
            return "{} in {}, priority {}".format(self.name, self.country, self.priority)

    def tog_visited(self):
        if self.visited:
            self.visited = False
        elif not self.visited:
            self.visited = True
