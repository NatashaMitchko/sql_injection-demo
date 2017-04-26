from flask import Flask, render_template, request, session

app = Flask(__name__)

@app.route('/')
def index():
    """Homepage"""
    # username = request.args.get("username")
    # password = request.args.get("password")
    return render_template('login.html')
                            # username=username,
                            # password=password)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)