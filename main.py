from flask import Flask,render_template

# Create instance of my application 
app = Flask(__name__)

# Add app endpoints
@app.route('/')

# View function
def homepage():
   return 'IT IS WORKING'

# Sign Up endpoint
@app.route('/signup')
def signup():
  return 'sign up working'

# Sign In endpoint
@app.route('/signin')
def signin():
  return'sign in working' 
# Sign Out endpoint
@app.route('/signout')
def signout():
  return 'sign out working'

#Setting debug Mode to true
if __name__=='__main__':
  app.run(debug=True)
