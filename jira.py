# coding=utf-8

from feedback import Feedback
import urllib2
import urllib
import json
import sys
import os.path

JIRA_HOST = "http://jira.freewheel.tv"
JIRA_PORT = "80"
PROJECTS = ["CLIENTHELP", "MRM", "FDB", "QOS", "OPS"]

# load JIRA host:port
if os.path.exists('jira.json'):
    config_file = file('jira.json', 'r')
    result = json.load(config_file)
    JIRA_HOST = result['host']
    JIRA_PORT = result['port']

jira_url = "%s:%s" % (JIRA_HOST, JIRA_PORT)
if not jira_url.endswith("/"):
    jira_url += "/"

# load all projects
if os.path.exists("projects.json"):
    project_file = file("projects.json", "r")
    results = json.load(project_file)
    if len(results) > 0:
        PROJECTS = []
        for project in results:
            PROJECTS.append(project['key'])
PROJECTS.sort()

# generate options for ticket number
if len(sys.argv) == 2:
    query = urllib.quote(sys.argv[1])

    feeds = Feedback()

    for project in PROJECTS:
        ticket_url = "%sbrowse/%s-%s" % (jira_url, project, query)
        feeds.add_item(title="%s-%s" % (project, query), subtitle=ticket_url, valid='YES', arg=ticket_url, icon='icon.png')

    print feeds