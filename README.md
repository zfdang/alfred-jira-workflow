# Alfred JIRA Workflow

this workflow allows you to open JIRA ticket by inputing ticket number only.

## Step.1 Update Project Lists

Visit the below URL to get all projects list of your JIRA system:

> http://host:port/rest/api/2/project

and save the result to file [projects.json](projects.json)

## Step.2 Set JIRA host

[jira.json](jira.json)

## Step.3 Open JIRA ticket in Alfred with keyword "jira"

alfred > jira 1234

![image](screenshot.jpg)

All possible tickets will be shown, and you can select any of them and open it in default browser.


