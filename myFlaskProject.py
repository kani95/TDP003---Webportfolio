from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import data

def load_json():
    '''
 
    Function that uses the load-function from the API.

    Parameters:

       None 
     
    Returns:
 
       list: list of all projects (dicts).
  
    '''
    
    db = data.load("data.json")
    return db

def log_error(error):
    '''

    Function that opens a text file and append error message with current date and time.

    Parameter:

      error (str): The error message

    Return:
      
      None

    '''
    
    with open("doc/error_log.txt", "a") as f:
        print(datetime.now(), error, file=f)

    
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    ''' 
    Function that displays the homepage.

    Parameters:
    
       None
    
    Returns:
    
       Render the homepage
        
    '''
    db = data.load("data.json")
    all_projects=data.search(db, sort_by='end_date', sort_order='descending',
                               techniques=None, search="", search_fields=None)
    latest_project=all_projects[0]
    
    return render_template("index.html",l_project=latest_project)

@app.route("/list")
def list():
    '''
    Function that uses the search-function from the API and lists all project that match the search the user input.
    Can also sort by different fields and can present the list in ascending or descending order.

    Parameters:

       None

    Returns:

       Render the list-page.

    '''
    # global db
    db = load_json()
    # get the search from the user using GET method
    search_project = request.args.get("search", "")
    # sort by has default value of None it crashes
    sort_byf = request.args.get("sort_by", "start_date")
    sort_order = request.args.get("sort_order", "desc")
    # get a list of all selected search fields that the user selected
    search_fields = request.args.getlist("search_fields")
    # if no search fields are selected from the user then search through all search fields
    if bool(search_fields) is False:
        search_fields = None
    # if no sort by is selected then use default as start date    
    if bool(sort_byf) is False:
        sort_byf = "start_date"
    if bool(sort_order) is False:
        sort_order = "desc"
    # get a list of all unique techniques that are being used by every project and capitalize the first character 
    all_tech = data.get_techniques(db)
    for index,tech in enumerate(all_tech):
        all_tech[index] = tech.capitalize()
    # get the techniques that the user has selected using POST method, if the user selects no techniques then list all projects
    requested_tech = request.args.getlist("technique")    
    if bool(requested_tech) is False or len(requested_tech) == 0:
        requested_tech = None

    # sort_byf = request.args.get("sort_byf", "start_date")

    # find the projects with the selected techniques using the search method from the API
    # found_projects = data.search(db, sort_by=sort_byf, sort_order='desc',
    #                  techniques=requested_tech, search="", search_fields=None)
    # uses the search funtion from the API and searches thorugh each project depending on the user input   
    found_projects = data.search(db, sort_by=sort_byf, sort_order=sort_order, techniques=requested_tech, search=search_project, search_fields=search_fields)


    # if no project are found with the given search then render list.html with a message to the user that no project could be found with that search 
    if len(found_projects) == 0:
        return render_template("list.html", search=search_project, all_tech=all_tech, technique=requested_tech, projects=found_projects, sort_by=sort_byf, empty_list = True, sort_order=sort_order)
        
   # found_projects = data.search(db, sort_by=sort_byf, sort_order=sort_order,
    #                             techniques=None, search=search_project, search_fields=search_fields)
    
    return render_template("list.html", search=search_project, projects=found_projects, all_tech=all_tech, techniques=requested_tech, sort_by=sort_byf, sort_order=sort_order)

@app.route("/project/<int:id>")
def project(id):
    ''' 
    Function that renders a single project based of the project id given as parameter.
    
    Parameter: 
    
        id (int):The project id

    Returns:
   
        Render the project-page 
    
    '''
    #global db
    db = load_json()
    # uses the get_project() function from the API that return a project where the project_id matches the id given as a parameter
    found_project = data.get_project(db, id)
    # if the project couldn't be found then render a HTML page containing an error message notifying the user about the error.
    if found_project is None:
       return render_template('404.html'), 404
    return render_template("project.html", project=found_project)

@app.route("/academics")
def academics():
    ''' 
    Function that lists the academics I have studied.

    Parameter:

       None
    
    Return:

       Render the academics-page

    ''' 
   # global db

    return render_template("academics.html")


@app.errorhandler(404)
def page_not_found(e):
    '''  
    If the URL dosen't exist then render a HTML page displaying an error message notifying it.
    
    Parameter:
      
       e (int):The error code

    Return:
    
       Render the 404-error-page

    '''

    log_error(e)
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    ''' 
    If internal server error occur then render a HTML page that display a error message notifying it.

    Parameter:
     
       e (int):The error code

    Return:
    
       Render the 500-error-page

    '''

    log_error(e)
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True)
