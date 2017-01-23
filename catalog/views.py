from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def mainPage():
    '''The Homepage'''
    return render_template('index.html')


@app.route('/catlover/')  # for testing
@app.route('/catlover/<int:user_id>/')
def showList(user_id):
    '''A User's list page '''
    return render_template('list.html')


@app.route('/catlover/delete')  # for testing
@app.route('/catlover/<int:user_id>/delete/', methods=['GET', 'POST'])
def deleteList(user_id):
    return render_template('list_delete.html')


@app.route('/category/')  # for testing
@app.route('/category/<int:category_id>/cats/')
def showCategory(category_id):
    '''Show items to a specific category.'''
    return render_template('category.html')


@app.route('/catlover/newcat')  # for testing
@app.route('/catlover/<int:user_id>/list/newcat/', methods=['GET', 'POST'])
def addItem(user_id):
    '''Handler to add a new Item'''
    return render_template('item_new.html')


@app.route('/cat/')  # for testing
@app.route('/cat/<int:item_id>/')
def showItem(item_id):
    '''Handler to Single Item page'''
    return render_template('item.html')


@app.route('/cat/edit')  # for testing
@app.route('/cat/<int:item_id>/edit/', methods=['GET', 'POST'])
def editItem(item_id, category_name=None):
    '''To edit an item.'''
    return render_template('item_edit.html')


@app.route('/cat/delete')  # for testing
@app.route('/cat/<int:item_id>/delete/', methods=['GET', 'POST'])
def deleteItem(item_id):
    '''To delete an item.'''
    return render_template('item_delete.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
