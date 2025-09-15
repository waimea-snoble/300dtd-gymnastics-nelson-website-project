#===========================================================
# YOUR PROJECT TITLE HERE
# YOUR NAME HERE
#-----------------------------------------------------------
# BRIEF DESCRIPTION OF YOUR PROJECT HERE
#===========================================================


from flask import Flask, render_template, request, flash, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import html

from app.helpers.session import init_session
from app.helpers.db      import connect_db
from app.helpers.errors  import init_error, not_found_error
from app.helpers.logging import init_logging
from app.helpers.auth    import login_required
from app.helpers.time    import init_datetime, utc_timestamp, utc_timestamp_now


# Create the app
app = Flask(__name__)

# Configure app
init_session(app)   # Setup a session for messages, etc.
init_logging(app)   # Log requests
init_error(app)     # Handle errors and exceptions
init_datetime(app)  # Handle UTC dates in timestamps


#-----------------------------------------------------------
# Home page route
#-----------------------------------------------------------
@app.get("/")
def show_all_tasks():
    with connect_db() as client:
        # Get all the things from the DB
        sql = """
            SELECT tasks.id,
                   tasks.name,
                   tasks.signed_up

            FROM tasks
        """
        params=[]
        result = client.execute(sql, params)
        tasks = result.rows

        # And show them on the page
        return render_template("pages/home.jinja", tasks=tasks)
    

#-----------------------------------------------------------
#  Update the volunteer status for a task
#-----------------------------------------------------------
# @app.get("/update_volunteer_status/<int:id>")
# def update_volunteer(id):
#     with connect_db() as client:
#         # Toggle signed_up state
#         sql = """
#             UPDATE tasks
#             SET signed_up = NOT signed_up
#             WHERE id = ?
#         """
        
#         params = [id]
#         client.execute(sql, params)

#         return redirect("/")

    
#-----------------------------------------------------------
# Route for adding a thing, using data posted from a form
# - Restricted to logged in users
#-----------------------------------------------------------
# @app.post("/volunteer/")
# @login_required
# def volunteer_task(task_id):

#     # Get the user id from the session
#     user_id = session["user_id"]

#     with connect_db() as client:

#         # Add the thing to the DB
#         sql = "INSERT INTO volunteers (user_id, task_id) VALUES (?, ?)"
#         params = [user_id, task_id]
#         client.execute(sql, params)

#         # Go back to the home page
#         flash(f"Thank you for signing up")
#         return redirect("/")

#-----------------------------------------------------------
# Favouriting route
#-----------------------------------------------------------
@app.get("/volunteer/<int:task_id>")
@login_required
def toggle_volunteer(task_id):
    # Get the user's ID
    user_id = session["user_id"]
 
    with connect_db() as client:
        # Check if this exercise is favourited
        sql = "SELECT * FROM volunteers WHERE user_id = ? AND task_id = ?"
        params = [user_id, task_id]
        params2 = [task_id]
        result = client.execute(sql, params)
 



        if result.rows:
            # Already signed up so un signup
            sql = "DELETE FROM volunteers WHERE user_id = ? AND task_id = ?"
            client.execute(sql, params)
            flash("Task no longer signed up", "Success")
        else:
            # not signed up so sign up
            sql = "INSERT INTO volunteers (user_id, task_id) VALUES (?, ?)"
            client.execute(sql, params)
            flash("Task now signed up", "success")

                    # Toggle signed_up state
        sql = """
            UPDATE tasks
            SET signed_up = signed_up + 1
            WHERE id = ?
        """
        
        client.execute(sql, params2)
 
    # Redirect back to the current page
    return redirect(request.referrer or "/")

# #-----------------------------------------------------------
# # About page route
# #-----------------------------------------------------------
# @app.get("/about/")
# def about():
#     return render_template("pages/about.jinja")


# #-----------------------------------------------------------
# # About page route
# #-----------------------------------------------------------
# @app.get("/about/")
# def about():
#     return render_template("pages/about.jinja")


#-----------------------------------------------------------
# Things page route - Show all the things, and new thing form
#-----------------------------------------------------------
@app.route("/personal/")
def personal():
    user_id = session["user_id"]  # Get the logged-in user
    with connect_db() as client:
        sql = """

                    SELECT 
                        tasks.id,
                        tasks.name,
                        tasks.description,
                        tasks.signed_up,
                        tasks.completed
                    FROM volunteers
                    JOIN tasks ON volunteers.task_id = tasks.id
                    WHERE volunteers.user_id = ?

            
        """
        result = client.execute(sql, [user_id])
        tasks = result.rows
    return render_template("pages/personal.jinja", tasks=tasks)



#-----------------------------------------------------------
# Personal Check box
#-----------------------------------------------------------
@app.get("/toggle-personal/<int:id>")
def toggle_personal(id):
    with connect_db() as client:
        # Toggle the completed state
        sql = "UPDATE tasks SET completed = NOT completed WHERE id = ?"
        client.execute(sql, [id])

        # Fetch all tasks for this user
        sql = """
            SELECT tasks.id, tasks.name, tasks.description,
                tasks.signed_up, tasks.completed
            FROM volunteers
            JOIN tasks ON volunteers.task_id = tasks.id
            WHERE volunteers.user_id = ?
        """
        user_id = session["user_id"]  # make sure user is logged in
        result = client.execute(sql, [user_id])
        tasks = result.rows

    return render_template("pages/personal.jinja", tasks=tasks)


#-----------------------------------------------------------
# Thing page route - Show details of a single thing
#-----------------------------------------------------------
@app.get("/task/<int:id>")
def show_one_task(id):
    with connect_db() as client:
        # Get the task details from the DB
        sql = """
            SELECT tasks.id,
                   tasks.name,
                   tasks.description,
                   tasks.signed_up,
                   tasks.completed

            FROM tasks

            WHERE tasks.id=?
        """
        params = [id]
        result = client.execute(sql, params)

        # Did we get a result?
        if result.rows:
            # yes, so show it on the page
            task = result.rows[0]
            return render_template("pages/task.jinja", task=task)

        else:
            # No, so show error
            return not_found_error()
        

#-----------------------------------------------------------
# Home page route
#-----------------------------------------------------------
@app.get("/admin-home/")
def show_admin_home():
    with connect_db() as client:
        # Get all the things from the DB
        sql = """

                    SELECT 
                        users.id,
                        users.name
                    FROM volunteers
                    JOIN users ON volunteers.user_id = users.id
                    WHERE volunteers.task_id = ?

            
        """
        params=[]
        result = client.execute(sql, params)
        users = result.rows

        # And show them on the page
        return render_template("pages/home.jinja", users=users)




# #-----------------------------------------------------------
# # Thing admin page route - Show details of a single thing
# #-----------------------------------------------------------
# @app.get("/task/<int:id>")
# def show_one_task(id):
#     with connect_db() as client:
#         # Get the task details from the DB, including the owner info
#         sql = """
#             SELECT things.id,
#                    things.name,
#                    things.user_id,
#                    users.name AS owner

#             FROM things
#             JOIN users ON things.user_id = users.id

#             WHERE things.id=?
#         """
#         params = [id]
#         result = client.execute(sql, params)

#         # Did we get a result?
#         if result.rows:
#             # yes, so show it on the page
#             thing = result.rows[0]
#             return render_template("pages/thing.jinja", thing=thing)

#         else:
#             # No, so show error
#             return not_found_error()


#-----------------------------------------------------------
# Route for adding a thing, using data posted from a form
# - Restricted to logged in users
#-----------------------------------------------------------
@app.post("/add")
@login_required
def add_a_task():
    # Get the data from the form
    name  = request.form.get("name")
    description = request.form.get("description")
    required_amount = request.form.get("required_amount")


    # Sanitise the text inputs
    name = html.escape(name)

    # Get the user id from the session
    user_id = session["user_id"]

    with connect_db() as client:
        # Add the thing to the DB
        sql = "INSERT INTO tasks (name, description, required_amount) VALUES (?, ?, ?)"
        params = [name, description, required_amount]
        client.execute(sql, params)

        # Go back to the home page
        flash(f"Task '{name}' added", "success")
        return redirect("/")


#-----------------------------------------------------------
# Route for deleting a thing, Id given in the route
# - Restricted to logged in users
#-----------------------------------------------------------
@app.get("/delete/<int:id>")
@login_required
def delete_a_task(id):

        # Check if the logged-in user is admin
    if int(session.get("user_admin", 0)) != 1:
        flash("You are not allowed to delete tasks", "danger")
        return redirect("/")
    
    else:
        with connect_db() as client:
            # Delete the thing from the DB only if we own it
            sql = "DELETE FROM tasks WHERE id=?"
            
            params = [id]
            client.execute(sql, params)

            sql = "DELETE FROM volunteers WHERE task_id=?"

            params = [id]
            client.execute(sql, params)
            # Go back to the home page
            flash("Thing deleted", "success")
            return redirect("/")







#-----------------------------------------------------------
# User registration form route
#-----------------------------------------------------------
@app.get("/register")
def register_form():
    return render_template("pages/register.jinja")

#-----------------------------------------------------------
# User login form route
#-----------------------------------------------------------
@app.get("/personal-route")
def personal_list():
    return render_template("pages/personal.jinja")
  

#-----------------------------------------------------------
# User login form route
#-----------------------------------------------------------
@app.get("/login")
def login_form():
    return render_template("pages/login.jinja")


#-----------------------------------------------------------
# Route for adding a user when registration form submitted
#-----------------------------------------------------------
@app.post("/add-user")
def add_user():
    # Get the data from the form
    name = request.form.get("name")
    username = request.form.get("username")
    password = request.form.get("password")
    phone = request.form.get("phone")
    

    with connect_db() as client:
        # Attempt to find an existing record for that user
        sql = "SELECT * FROM users WHERE username = ?"
        params = [username]
        result = client.execute(sql, params)

        # No existing record found, so safe to add the user
        if not result.rows:
            # Sanitise the name
            name = html.escape(name)

            # Salt and hash the password
            hash = generate_password_hash(password)

            # Add the user to the users table
            sql = "INSERT INTO users (name, username, password_hash, phone) VALUES (?, ?, ?, ?)"
            params = [name, username, hash, phone]
            client.execute(sql, params)

            # And let them know it was successful and they can login
            flash("Registration successful", "success")
            return redirect("/login")

        # Found an existing record, so prompt to try again
        flash("Username already exists. Try again...", "error")
        return redirect("/register")


#-----------------------------------------------------------
# Route for processing a user login
#-----------------------------------------------------------
@app.post("/login-user")
def login_user():
    # Get the login form data
    username = request.form.get("username")
    password = request.form.get("password")

    with connect_db() as client:
        # Attempt to find a record for that user
        sql = "SELECT * FROM users WHERE username = ?"
        params = [username]
        result = client.execute(sql, params)

        # Did we find a record?
        if result.rows:
            # Yes, so check password
            user = result.rows[0]
            hash = user["password_hash"]

            # Hash matches?
            if check_password_hash(hash, password):
                # Yes, so save info in the session
                session["user_id"]   = user["id"]
                session["user_name"] = user["name"]
                session["logged_in"] = True
                session["user_admin"]   = user["admin"]

                # And head back to the home page
                flash("Login successful", "success")
                return redirect("/")

        # Either username not found, or password was wrong
        flash("Invalid credentials", "error")
        return redirect("/login")


#-----------------------------------------------------------
# Route for processing a user logout
#-----------------------------------------------------------
@app.get("/logout")
def logout():
    # Clear the details from the session
    session.pop("user_id", None)
    session.pop("user_name", None)
    session.pop("user_logged_in", None)
    session.pop("user_admin", None)

    # And head back to the home page
    flash("Logged out successfully", "success")
    return redirect("/")

