from flask import Flask,render_template

# Create instance of my application 
app = Flask(__name__)

# Add app endpoints
@app.route('/')

# View function
def homepage():
   return render_template('index.html')

# Sign Up endpoint
@app.route('/signup')
def signup():
  return render_template('signup.html')

# Sign In endpoint
@app.route('/signin')
def signin():
  return render_template('signin.html')
# Sign Out endpoint
@app.route('/signout')
def signout():
  return render_template('signout.html')

#Setting debug Mode to true
if __name__=='__main__':
  app.run(debug=True)
