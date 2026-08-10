from flask import Flask, request, render_template_string

from db import initialize_database, add_user, find_user


app = Flask(__name__)


initialize_database()


@app.route("/")
def home():

    return """
    <h1>Secure Coding Review</h1>

    <p>Welcome to our test application.</p>

    <a href="/login">Login</a><br>
    <a href="/register">Register</a>
    """


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        add_user(username, email, password)

        return f"""
        <h2>Registration Successful</h2>

        <p>Username: {username}</p>
        <p>Email: {email}</p>
        <p>Password: {password}</p>
        """

    return """
    <h2>Register</h2>

    <form method="POST">

        <label>Username:</label>
        <input type="text" name="username">

        <br><br>

        <label>Email:</label>
        <input type="email" name="email">

        <br><br>

        <label>Password:</label>
        <input type="password" name="password">

        <br><br>

        <button type="submit">Register</button>

    </form>
    """


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = find_user(username)

        if user and user["password"] == password:

            return f"""
            <h2>Login Successful</h2>

            <p>Welcome {username}</p>
            """

        return """
        <h2>Login Failed</h2>
        <p>Invalid username or password.</p>
        """

    return """
    <h2>Login</h2>

    <form method="POST">

        <label>Username:</label>
        <input type="text" name="username">

        <br><br>

        <label>Password:</label>
        <input type="password" name="password">

        <br><br>

        <button type="submit">Login</button>

    </form>
    """


if __name__ == "__main__":

    app.run(
        debug=True,
        use_reloader=False
    )