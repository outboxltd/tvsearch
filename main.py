import os
from bottle import (get, post, redirect, request, route, run, static_file,error,template,jinja2_view)
from jinja2 import Template
import json
import utils

# testing
with open('./data/143.json') as the_file:
    data = json.load(the_file)

episodes = data['_embedded']['episodes']
# testing





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


@route('/about')
@jinja2_view('about.html', template_lookup=['pages'])
def index2():
    sectionTemplate = "./templates/browse.tpl"
    return {'name': "shmulik" ,"tricks": ["קפיצה בחבל", "תפיסת חתולים", "האכלת כלבים אחרים"],'episodes': episodes }

run(host='0.0.0.0', debug=True, reloader=True, port=os.environ.get('PORT', 5000))
