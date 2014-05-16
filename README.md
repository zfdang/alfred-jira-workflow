# Alfred JIRA Workflow

this workflow allows you to open JIRA tickets by inputing ticket number only.

## Step.1 Get Project Lists

Visit the below URL to get all project lists of your JIRA system:

> http://host:port/rest/api/2/project

and save the result to file projects.json

## Step.2 Set JIRA host

> jira.json


## Step.3 Open JIRA tickets in Alfred

alfred > jira 1234

![image](screenshot.jpg)

All possible ticket will be shown, and you can select any of them and open it in browser.


