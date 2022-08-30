a = input('Please enter author\'s name? ').title()
c = input('Please enter the category? ').title()
t = input('Please enter the title? ').title()
s = input('Is it available? ').title()


class LibraryBooks:
    def __init__(self, author, category, title, status):
        self.author = author
        self.category = category
        self.title = title
        self.status = status

    def display(self):
        print('Author name:', self.author)
        print('Category:', self.category)
        print('Title:', self.title)
        print('Status:', self.status)


book1 = LibraryBooks(author=a, category=c, title=t, status=s)
book1.display()
print(type(s))
print('***************')
request = LibraryBooks(author=a, category=c, title=t, status=s)
req = input('Please enter the title or author of a book? ').title()
print(type(request.status))
if request.status == 'True' and request.title == req or request.author == req:
    print('Book is available.')
else:
    print('Book is unavailable.')

'''book1 = LibraryBooks(author='Mankiw', category='Economics', title='Intro to Economics', status=True)
print('Author: ', book1.author)
print('Category: ', book1.category)
print('Title: ', book1.title)
print('Availability: ', book1.status)'''

print('=====================')

# book2 = LibraryBooks(author='George. R.R. Martin', category='Fantasy', title='A Game Of Thrones', status=False)
# print('Author: ', book2.author)
# print('Category: ', book2.category)
# print('Title: ', book2.title)
# print('Availability: ', book2.status)
