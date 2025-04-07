from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/member/<int:id>')
def member_profile(id):
    return f"<h2>Member Profile Page for ID: {id}</h2><p>This is where biodata will go.</p>"

if __name__ == '__main__':
    app.run()
