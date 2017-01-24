from flask import Flask
from flask import (flash, render_template, url_for)

from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker

from models import Base, User, Category, Item

app = Flask(__name__)

# connect to database and create db session
engine = create_engine('sqlite:///catlist.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def categoryMenu():
    '''Get categories from DB for menu navigation'''
    categories = session.query(Category).all()
    return categories


@app.route('/')
def mainPage():
    '''The Homepage'''
    cat_menu = categoryMenu()

    items = session.query(Item).order_by(desc(Item.id))
    return render_template('index.html', cat_menu=cat_menu, items=items)


@app.route('/catlover/')  # for testing
@app.route('/catlover/<int:user_id>/')
def showList():
    '''A User's list page '''
    return render_template('list.html')


@app.route('/catlover/delete')  # for testing
@app.route('/catlover/<int:user_id>/delete/', methods=['GET', 'POST'])
def deleteList():
    return render_template('list_delete.html')


@app.route('/category/')  # for testing
@app.route('/category/<int:category_id>/cats/')
def showCategory():
    '''Show items to a specific category.'''
    return render_template('category.html')


@app.route('/catlover/newcat')  # for testing
@app.route('/catlover/<int:user_id>/list/newcat/', methods=['GET', 'POST'])
def addItem():
    '''Handler to add a new Item'''
    return render_template('item_new.html')


@app.route('/cat/')  # for testing
@app.route('/cat/<int:item_id>/')
def showItem():
    '''Handler to Single Item page'''
    return render_template('item.html')


@app.route('/cat/edit')  # for testing
@app.route('/cat/<int:item_id>/edit/', methods=['GET', 'POST'])
def editItem():
    '''To edit an item.'''
    return render_template('item_edit.html')


@app.route('/cat/delete')  # for testing
@app.route('/cat/<int:item_id>/delete/', methods=['GET', 'POST'])
def deleteItem():
    '''To delete an item.'''
    return render_template('item_delete.html')


@app.errorhandler(404)
def notFound(exc):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
