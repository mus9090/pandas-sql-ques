import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    newdf = pd.merge(employee, department, left_on="departmentId", right_on="id")

    max_salary = newdf.groupby("name_y")["salary"].transform("max")

    result = newdf[newdf["salary"] == max_salary]

    return result[["name_y", "name_x", "salary"]].rename(columns={
        "name_y": "Department",
        "name_x": "Employee",
        "salary": "Salary"
    })