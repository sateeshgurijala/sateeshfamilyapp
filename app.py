from flask import Flask, render_template

app = Flask(__name__)


# Home route, displaying the family tree (just a placeholder for now)
@app.route('/')
def home():
    return render_template('home.html')


# Member profile route, showing details for a family member
@app.route('/member/<int:id>')
def member_profile(id):
    # Simulated member data for now
    members = {
        1: {
            "name": "Sateesh Gurijala",
            "relation": "Father",
            "bio": "The root of the family tree. Loves coding and family.",
            "image": "https://via.placeholder.com/150"
        }
    }

    # Get the member based on the ID provided
    member = members.get(id)

    # If member is not found, return a 404 error
    if not member:
        return "Member not found", 404

    # Render the profile page and pass the member data
    return render_template('profile.html', member=member)


# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
