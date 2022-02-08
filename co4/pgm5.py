class Publisher:
    def __init__(self,name):
        self.name=name;
    def display(self):
        print("Publisher:",self.name)
class Book(Publisher):
    def __init__(self,name,title,author):
        Publisher.__init__(self,name)
        self.title=title
        self.author=author
    def display(self):
        Publisher.display(self)
        print("Title:",self.title);
        print("Author:",self.author);
class Python(Book):
    def __init__(self,name,title,author,price,pages):
        Book.__init__(self,name,title,author)
        self.price=price
        self.pages=pages
    def display(self):
        Book.display(self)
        print("Price:",self.price);
        print("Pages:",self.pages);
s1=Python("MR BOOKS","PYTHON","JOSEPH",500,600)
s1.display()
#co4 last qn
