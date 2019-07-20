import os
from bottle import (get, post, redirect, request, route, run, static_file,
                    template)
import utils

# Static Routes

@get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="./js")

@get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./css")

@get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="./images")

@route('/')
def index():
    sectionTemplate = "./templates/home.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = {})

@route('/browse')
def Browse():
    sectionTemplate = "./templates/browse.tpl"
    return template("./pages/browse.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = {})

@route('/search')
def Search():
    sectionTemplate = "./templates/search.tpl"
    return template("./pages/search.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData = {})

run(host='0.0.0.0', debug=True, reloader=True, port=os.environ.get('PORT', 5000))
