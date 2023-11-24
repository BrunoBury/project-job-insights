from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salary = float("-inf")
        for job in self.jobs_list:
            salary = job.get("max_salary", "")
            if salary and salary.isdigit():
                salary = int(salary)
                max_salary = max(max_salary, salary)

        return max_salary if max_salary != float("-inf") else 0

    def get_min_salary(self) -> int:
        min_salary = float("inf")
        for job in self.jobs_list:
            salary = job.get("min_salary", "")
            if salary and salary.isdigit():
                salary = int(salary)
                min_salary = min(min_salary, salary)

        return min_salary if min_salary != float("inf") else 0

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
