import job_classes

class JobsRunner:

    @staticmethod
    def __run_job(
        job: dict,
        prev_job_result: dict | None
    ) -> dict | None:
        """
        Run the job.
    
        Parameters
        ----------
        job : dict
            The job and its options.
        prev_job_result : None
            Result of the previous job.
        Returns
        -------
        dict | None
            Either return dictionary of the result
            or nothing in case of console output
        """
        classname = job.get("jobtype")

        if classname == "tSqliteInput":
            curr_job = job_classes.tSqliteInput(**job)
            prev_job_result = curr_job.get_data()

        elif classname == "tConsoleOutput":
            curr_job = job_classes.tConsoleOutput()
            curr_job.display(prev_job_result)
            prev_job_result = None
        return prev_job_result

    @staticmethod
    def run_jobs(jobs: list[dict]) -> None:
        """
        Run the jobs.
    
        Parameters
        ----------
        jobs : list[dict]
            The list of jobs.
        prev_job_result : None
            Result of the previous job.
        Returns
        -------
        None
        """
        prev_job_result = None
        for job in jobs:
            prev_job_result = JobsRunner.__run_job(
                job=job,
                prev_job_result=prev_job_result
            )
        
