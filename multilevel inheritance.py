class Trainer:
  def __init__(self, name, subject):
    self.name = name
    self.subject = subject

  def obj(self):
    print(self.name, self.subject)
x = Trainer("Ishwar", "Python")
x.obj()
class Trainee(Trainer):
      def __init__(self, name, subject):
        self.name = name
        self.subject = subject
x = Trainee("swapnil", "Python")
x.obj()
class Intern(Trainee):
      def __init__(self, name, subject):
        self.name = name
        self.subject = subject
x = Intern("Sandip", "Python")
x.obj()
