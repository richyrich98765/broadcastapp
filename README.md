Flask running in Docker, using tiangolo’s flask-python-uwsgi-nginx-alpine image as a base.

So there’s more to learn: building my own nginx on alpine, understanding uwsgi, why this dude recommends Starlette instead of Flask (says it’s ‘800%’ improvement on performance, whatever that means…)

Base
https://hub.docker.com/r/tiangolo/uwsgi-nginx-flask

My Flask app: test-flask-app
This app itself comes from Microsoft’s VSCode pages 
https://code.visualstudio.com/docs/python/tutorial-flask

Tree
.
|- .gitignore
|- LICENSE
|- README.md
|- requirements.txt – (python freeze > requirements.txt) (cut-down)
|- uwsgi.ini - defines entry point, and app instance.
|- main.py – entry point, where the app instance made available
|- hello_app
   |- __init__.py – creates the app instance and pulls in views
   |- views.py
   |- static
      |- style.css
      |- data.json
   |- templates
      |- layout.html
      |- home.html
      |- contact.html
      |- about.html
      |- hello_there.html


GitHub
https://github.com/richyrich98765/test-flask-app

Dockerfile
```
# base image
FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine-2020-12-19

# GIT repo
ARG GITREPOBASE="https://github.com/richyrich98765"
ARG GITREPO="test-flask-app"

# build the image from the GIT repo, keeping only the
# necessary bits, to reduce image size
RUN apk add --no-cache git && \
    git clone ${GITREPOBASE}/${GITREPO}.git && \
    apk del git && \
    cp -R ${GITREPO}/* . && \
    rm -R ${GITREPO} && \
    pip install -r requirements.txt

# Set up paths for the static files
ENV STATIC_URL /hello_app/static
ENV STATIC_PATH hello_app/static

# nginx running on port 80
EXPOSE 80
```

Description
Tiangolo’s image provides the base alpine – python – nginx, with uWSGI installed. This image also does the entry point / command thingy, so one isn’t present in the Dockerfile.
It will look for a file main.py, and uses that as the starting point of the app.
My main.py just pulls in hello_app’s app instance. The app is instantiated inside the hello_app package’s __init__.py. That file also pulls in the view, and when we start to add database stuff, the table code too.

Build and Run
'''
docker build --tag flaskdo . 
docker container run --rm --publish 80:80 --detach --name flaskdo flaskdo:latest
'''
