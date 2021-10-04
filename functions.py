import os

textFilePath = "books_list.txt"

def readFile():
    filesize = os.path.getsize(textFilePath)
    books = []
    if(filesize!=0):  
        with open(textFilePath, 'r') as f: 
            while True:
                line = f.readline().strip('"')
                if not line:
                    break
                books.append(line.split(','))   
    return books   

def deleteBook(name):
    if(name == None):
        return readFile()
    else:
        with open(textFilePath, 'r') as f: 
            data = f.readlines()

        with open(textFilePath, 'w') as f: 
            books=[]
            for line in data:
                book = line.strip('", ').split(",")
                if((name != book[0])):
                    if(line == data[0]):
                        line = line.rstrip('\n')
                    else:
                        line = '\n' + line.rstrip('\n')   
                    f.write(line)
                    books.append(book)  
            return books

def searchBook(input,type):
    filesize = os.path.getsize(textFilePath)
    books = []
    if(filesize!=0): 
        with open(textFilePath, 'r') as f: 
            while True:
                line = f.readline().strip('"')
                if not line:
                    break
                book = line.split(',')
                if((type == "title") & (input in book[0].lower())):
                    books.append(book)  
                elif((type == "author") & (input in book[1].lower())):
                    books.append(book)              
    return books 
