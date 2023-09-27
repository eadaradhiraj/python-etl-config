import json
import job_classes

with open('run.json', 'r') as file:
    jobs = json.load(file)


prevjob = None
for job in jobs:
    classname = job.get("jobtype")

    if classname == "tSqliteInput":
        curr_job = job_classes.tSqliteInput(**job)
        prevjob = curr_job.get_data()
 
    elif classname == "tConsoleOutput":
        curr_job = job_classes.tConsoleOutput()
        curr_job.display(prevjob)
        prevjob = None
