try:
    with open('example.txt') as file_handler:
        for line in file_handler:
            print(line)

except:
    print('An error occurred.')


try:
    raise ImportError
except ImportError:
    print('Caught ImportError')

try:
    raise Exception('It was very poor.')
except:
    print('Error is massive.')

try:
    raise ImportError('Poor import')
except ImportError as error:
    print(type(error))
    print(error.args)
    print(error)

try:
    1/0
except ZeroDivisionError:
    print('Divide Zero')
finally:
    print('Clear up')
try:
    print('This is the try part.')
except IOError:
    print('IOError')
else:
    print('This is the else the else part ')