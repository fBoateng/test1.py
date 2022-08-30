"""class LibReq:
    bookcount = 0

    def __init__(self):
        self.author = [input('Enter author name? ')]
        self.title = [input('Enter book title? ')]
        LibReq.bookcount += 1
        return

    def showbook(self):
        print('These are the available books.')
        print(f'Author: {self.author}')
        print(f'Title: {self.title}')"""

book_list = []
n = int(input('Please enter the number of books you are entering? '))


class LibReq:
    def __init__(self, book_list):
        self.book_list = book_list

    def addbook(self):
        for i in range(0, n):
            info = input('Please enter book title? ')
            book_list.append(info)
        print(f'Books entered are {book_list}')

    def bookrequest(self, requestedbook):
        if requestedbook in book_list:
            print("The book you requested has now been borrowed")
            # self.availablebooks.remove(requestedbook)
            book_list.remove(requestedbook)
        else:
            print("Sorry the book you have requested is currently not in the library")

    def returnbook(self,returnedbook):
        book_list.append(returnedbook)
        print('thank you for returning the book')



LibReq.addbook(book_list)
LibReq.bookrequest(book_list, requestedbook=input('what book will you want to borrow? '))
print(f'Books available now are {book_list}')
LibReq.returnbook(book_list, returnedbook=input('Please enter the book you are returning? '))
print(f'Books available now are {book_list}')

