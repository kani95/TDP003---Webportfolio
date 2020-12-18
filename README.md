# Description
Webportofolio for displaying information about different programming projects
done during university studies. 

# How it works
Reads a json file that contains information about projects. An API (data.py) is used to communicate between the database (data.json) and the server (myFlaskProject.py). The server is able to generate templates for projects using jinja2.

Check "doc" for more information about all the functions used by the server.

# User manual
To run the server open the terminal and type in "python3 myFLaskProject.py" and then you will
see the url for the server. Use that url in a browser and then you should see the home website. To add or edit projects, just open "data.json" and either append a new project in a similiar fashion or edit a current one. For more information view "systemdokumentation.pdf" under catalogue "doc".

# Testing API-functions
To test the API-functions use "data_test.py". Further information about testing the API functions can be found in "data_test.py".   

#Installation
To read more about the required software for running this and how to install these, go to the doc catalogue and open "installationmanual.pdf". 


# Package-structure
Press the "display source" button to view the structure properly!!

my-portofolio/
├── data.json
├── data.py
├── data_test.py
├── doc
│   ├── error_log.txt
│   ├── flask_server.pdf
│   └── installationmanual.pdf
├── Dockerfile
├── myFlaskProject.py
├── __pycache__
│   └── data.cpython-38.pyc
├── README.md
├── static
│   ├── images
│   │   ├── 300x180.png
│   │   ├── crypt.png
│   │   ├── dev.png
│   │   ├── df_big.png
│   │   ├── df_small.png
│   │   ├── favicon.ico
│   │   ├── html_and_css.png
│   │   ├── img_avatar.jpg
│   │   ├── port.jpg
│   │   ├── simple_website.png
│   │   ├── socials.png
│   │   ├── tag.png
│   │   └── web.png
│   └── style
│       ├── bootstrap.min.css
│       ├── bootstrap-select.min.css
│       ├── self.jpg
│       └── styles.css
└── templates
    ├── 404.html
    ├── 500.html
    ├── error_layout.html
    ├── index.html
    ├── layout.html
    ├── list.html
    ├── project.html
    └── techniques.html


