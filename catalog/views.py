from flask import Flask
from flask import (flash, render_template, url_for, request, redirect)

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
    menuNav = session.query(Category).all()
    return menuNav


@app.route('/')
def mainPage():
    '''The Homepage'''
    menuNav = categoryMenu()

    items = session.query(Item).order_by(desc(Item.id))
    return render_template('index.html', menuNav=menuNav, items=items)


@app.route('/catlover/<int:user_id>/')
def showList(user_id):
    '''A User's list page '''
    menuNav = categoryMenu()

    user = session.query(User).filter_by(id=user_id).one()
    items = (session.query(Item).filter_by(user_id=user_id).order_by(
             desc(Item.category_id)).all())
    return render_template('list.html',
                           menuNav=menuNav,
                           user=user,
                           items=items)


@app.route('/catlover/<int:user_id>/delete/', methods=['GET', 'POST'])
def deleteList(user_id):
    menuNav = categoryMenu()

    user = session.query(User).filter_by(id=user_id).one()
    items = session.query(Item).filter_by(user_id=user_id).all()

    if request.method == 'POST':
        for item in items:
            session.delete(item)
            print "List deleted!"

        session.delete(user)
        print "User deleted!"
        session.commit()
        return redirect(url_for('mainPage'))
    else:
        return render_template('list_delete.html', menuNav=menuNav, user=user)


@app.route('/category/')  # for testing
@app.route('/category/<int:category_id>/cats/')
def showCategory():
    '''Show items to a specific category.'''
    menuNav = categoryMenu()
    return render_template('category.html', menuNav=menuNav)


@app.route('/catlover/newcat')  # for testing
@app.route('/catlover/<int:user_id>/list/newcat/', methods=['GET', 'POST'])
def addItem():
    '''Handler to add a new Item'''
    menuNav = categoryMenu()
    return render_template('item_new.html', menuNav=menuNav)


@app.route('/cat/')  # for testing
@app.route('/cat/<int:item_id>/')
def showItem():
    '''Handler to Single Item page'''
    menuNav = categoryMenu()
    return render_template('item.html', menuNav=menuNav)


@app.route('/cat/edit')  # for testing
@app.route('/cat/<int:item_id>/edit/', methods=['GET', 'POST'])
def editItem():
    '''To edit an item.'''
    menuNav = categoryMenu()
    return render_template('item_edit.html', menuNav=menuNav)


@app.route('/cat/delete')  # for testing
@app.route('/cat/<int:item_id>/delete/', methods=['GET', 'POST'])
def deleteItem():
    '''To delete an item.'''
    menuNav = categoryMenu()
    return render_template('item_delete.html', menuNav=menuNav)


@app.errorhandler(404)
def notFound(exc):
    menuNav = categoryMenu()
    return render_template('404.html', menuNav=menuNav), 404

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
