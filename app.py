from flask import Flask
app=Flask(__name__)

@app.route('/user/<name>')
def user_page(name):
   return 'User: %s' % name 