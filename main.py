import json
import job_classes

with open('run.json', 'r') as file:
    jobs = json.load(file)


prevjob = None
for job in jobs:
    classname = job.get("jobtype")

    if classname == "tsqlite":
        curr_job = job_classes.tsqlite(**job)
        prevjob = curr_job.get_data()
 
    elif classname == "tconsole":
        print(prevjob)
 
    # elif bike == "tFileDelimited":
