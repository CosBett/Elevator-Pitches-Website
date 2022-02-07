from flask import Flask

# Create instance of my application 
app = Flask(__name__)

# Add app endpoints
@app.route('/')

# View function
def homepage():
   return 'IT IS WORKING'

# Sign Up endpoint
def signup():
  return 'sign up working'

# Sign In endpoint
def signin():
  return'sign in working' 
# Sign Out endpoint
def signout():
  return 'sign out working'

#Setting debug Mode to true
if __name__=='__main__':
  app.run(debug=True)
