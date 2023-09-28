from etylpyconfig import JobsRunner

jobs = [
  {"jobtype": "tSqliteInput", "location": "Chinook_Sqlite.sqlite", "tablename": "Track"},
  {"jobtype": "tConsoleOutput"}
]

JobsRunner.run_jobs(jobs=jobs)
