from flask import Flask, render_template, request ,redirect,url_for
from flask.views import MethodView
from functions import deleteBook,readFile,searchBook,textFilePath

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


class ViewBook(MethodView):
    def get(self):
        books = readFile()
        return render_template('viewBooks.html', books= books) 

 
class AddBook(MethodView):
    def get(self):
        return render_template('addBook.html') 

    def post(self):
        title = request.form.get('title')
        Author = request.form.get('author')
        genre = request.form.get('genre')
        Height = request.form.get('height')
        Publisher = request.form.get('publisher')
        book = "\n{},{},{},{},{}".format(title,Author,genre,Height,Publisher)
        with open(textFilePath, 'a') as f: 
            f.write(book)
        return redirect(url_for('viewBooks'))

class ShowRemoveBook(MethodView):
    def get(self):
        books = readFile()
        return render_template('removeBook.html', books= books) 

class RemoveBook(MethodView):
    def get(self,name):
        books = deleteBook(name)
        return render_template('removeBook.html', books= books) 

class SearchDeletingBooks(MethodView):
    def post(self):
        type = request.form.get('type')
        reqBook = request.form.get('inputs').lower()
        books = searchBook(reqBook,type)
        return render_template('removeBook.html', books= books) 

class SearchBooks(MethodView):
    def post(self):
        type = request.form.get('type')
        reqBook = request.form.get('inputs').lower()
        books = searchBook(reqBook,type)
        return render_template('viewBooks.html', books= books) 



app.add_url_rule('/viewBooks', view_func=ViewBook.as_view('viewBooks'))  
app.add_url_rule('/addBook' , view_func=AddBook.as_view('addBook'))
app.add_url_rule('/removeBook' , view_func=ShowRemoveBook.as_view('removeBook'))
app.add_url_rule('/removeBook/<name>' , view_func=RemoveBook.as_view('removeBook/<name>'))
app.add_url_rule('/searchDelBook' , view_func= SearchDeletingBooks.as_view('searchDelBook'))
app.add_url_rule('/searchBook' ,view_func=SearchBooks.as_view('searchBook'))

app.run(debug=True)    