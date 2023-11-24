from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path) -> List[Dict]:
        with open(path, "r", newline="", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            self.jobs_list = list(csv_reader)
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        job_types = set()
        for job in self.jobs_list:
            job_types.add(job["job_type"])
        return job_types

    def filter_by_multiple_criteria(
        self, jobs: List[Dict], filter_criteria: Dict
    ) -> List[dict]:
        if not isinstance(filter_criteria, dict):
            raise TypeError("filter_criteria must be a dictionary")

        filtered_jobs = jobs[:]

        for key, value in filter_criteria.items():
            filtered_jobs = [
                job for job in filtered_jobs if job.get(key) == value
            ]

        return filtered_jobs


# instancia = ProcessJobs()
# dado_lidos = instancia.read("data/jobs.csv")
# print(dado_lidos)

# instancia = ProcessJobs()
# dados_lidos = instancia.read("data/jobs.csv")
# tipos_empregos_unicos = instancia.get_unique_job_types()
# print(tipos_empregos_unicos)
