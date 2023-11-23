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

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass


# instancia = ProcessJobs()
# dado_lidos = instancia.read("data/jobs.csv")
# print(dado_lidos)

# instancia = ProcessJobs()
# dados_lidos = instancia.read("data/jobs.csv")
# tipos_empregos_unicos = instancia.get_unique_job_types()
# print(tipos_empregos_unicos)
