from flask import Flask

# Create instance of my application 
app = Flask(__name__)

# Add app endpoints
@app.route('/')

# View function
def homepage():
   return 'IT IS WORKING'
   
#Setting debug Mode to true
if __name__=='__main__':
  app.run(debug=True)
