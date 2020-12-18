import json

# def match(db, argument, key):
#     return filter(lambda person: person[argument] == key, db)

def load(filename):
    """Loads JSON formatted project data from a file and 
       returns a list of all projects, sorted after number.
       return None if """
    try:        
        with open(filename) as f:
            data = json.load(f)
    except:
        return None
            
    all_projects = []
    for project in data:
        all_projects.append(project)
           
    all_projects = sorted(all_projects, key=lambda x: x['project_id'])
        
    return all_projects


def get_project_count(db):
    """Returns the number of projects"""
    return len(db)


def get_project(db, id):
    """Fetches the project with the specified id from the specified list.
    If the specified project id does not exist, None is returned."""

    for project in db:
        if project['project_id'] == id:
            return project
    return None


def get_techniques(db):
    """Fetches a list of all the techniques from the 
    specified project list in lexicographical order."""
    all_techniques = []

    for project in db:
       current_techniques = project['techniques_used']
       # If there are no techniques in the current project
       # go to the next project.
       if len(current_techniques) == 0:
           continue
       for technique in current_techniques:
           technique = technique.lower() 
           if technique not in all_techniques:
               all_techniques.append(technique)
    all_techniques = sorted(all_techniques)
    return all_techniques

def get_technique_stats(db):
    """Collects and returns project_id and project_name 
    for all techniques in the specified project list."""
    techniques_stats = {}

    # Create a list for all techniques as elements
    # for all projects
    techniques = get_techniques(db)
    for tech in techniques:
        techniques_stats[str(tech)] = []

    for project in db:
        current_techniques = project['techniques_used']
        if len(current_techniques) == 0:
            continue
        for technique in current_techniques:
            technique = technique.lower() 
            techniques_stats[technique].append(
                {"id": project["project_id"], "name": project["project_name"]})

    return techniques_stats


################### SEARCH HELPER FUNCTIONS ###################

def check_techniques(project, techniques):
    """Check for matching techniques in the given project
    returns a bool value."""
    # Create list of all techniques
    project_techniques = [tech.lower() for tech in project['techniques_used']]

    # default value, all techniques
    if techniques is None:
        return True
    if techniques is not None:
        func = lambda x: x if x.isdigit() else x.lower()
        techniques = [func(str(tech)) for tech in techniques]
        if len(techniques) != 0:
            for tech in techniques:
                string_of_techniques = " ".join(project_techniques)
                if tech not in string_of_techniques:
                    return False
            return True
        return True
    
def append_search(search_result, technique_in_project, project):
    """Checks if the current project has the required techniques
       if true appends the project to the other matched results."""
    
    if technique_in_project == True:
        search_result.append(project)


def sort_results(search_result, sort_order, sort_by):
    """Sorts the matched projects according to a specific field(sort_by)
       and in descending or ascending order."""
    if sort_order == 'asc':
        order_by = False
    else:
        order_by = True

    # Create a function that check if the object is a string if true convert the string to lowercase.
    func = lambda x: x[sort_by].lower() if (isinstance(x[sort_by],str)) else x[sort_by]
    # Sorts search_result based on "sort_by" in either descending or ascending order depending on "order_by".
    search_result = sorted(search_result, key=func, reverse=order_by)
    return search_result
    

################### SEARCH HELPER FUNCTIONS ###################


def search(db, sort_by='start_date', sort_order='desc',
           techniques=None, search=None, search_fields=None):

    search_result = []
    
    for project in db:

        
        technique_in_project = check_techniques(project, techniques)                    
        if technique_in_project == False:
            continue
        # Append current project to search_results
        if search is None:
            append_search(search_result, technique_in_project, project)
            continue
        # Create an object with all the keys in the current project.
        if search_fields is None:
            search_fields = project.keys()
        # if search_fields is an empty list return an empty list
        elif bool(search_fields) is False:
            return []
            
        if type(search) == str:
                search = search.lower()
        for field in search_fields:
            field = field.lower()
            # get the field value for the current project
            key_value = str(project[field]).lower()
            if search in key_value:
                append_search(search_result, technique_in_project, project)
                break
        
    return sort_results(search_result, sort_order, sort_by)
      
