from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @abstractmethod
    def display(): pass

#Write MyBook class
#questa questa classe estende la classe Book
class MyBook(Book):
    #prima di tutto devo ricevere i valori dalla classe padre che a sua volta è abstratta
    def __init__(self, title, author, price):
        super().__init__(title, author)
        self.price = price

    #self.price = price
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.price)


title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()