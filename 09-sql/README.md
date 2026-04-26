# SQL Homework: Employee Database

This project completes the Employee Database SQL challenge, "A Mystery in Two Parts." The work models employee data from six CSV files, builds a PostgreSQL schema, runs analysis queries, and includes the optional salary-by-title bonus analysis.

## Background

The assignment uses historical Pewlett Hackard employee records from the 1980s and 1990s. The goal is to design tables for the source CSVs, import the data into SQL, and answer business questions about employees, departments, managers, salaries, and titles.

## Files

- `EmployeeSQL/table.sql` - table schema with primary keys, foreign keys, data types, and constraints.
- `EmployeeSQL/queries.sql` - SQL queries for the required data analysis questions.
- `data/departments.csv` - department lookup data.
- `data/dept_emp.csv` - employee-to-department assignment data.
- `data/dept_manager.csv` - department manager assignment data.
- `data/employees.csv` - employee profile data.
- `data/salaries.csv` - employee salary data.
- `data/titles.csv` - employee title history data.
- `ERD/QuickDBD-Mason\`s SQL Diagram.png` - exported entity relationship diagram.
- `ERD/QuickDBD-Mason\`s SQL Diagram.pdf` - PDF version of the ERD.
- `sql_bonus/sql_bonus.ipynb` - optional bonus notebook using SQLAlchemy, Pandas, and Matplotlib.
- `output_data/Salary vs. Title.png` - exported bonus chart.
- `HW guideline/README.md` - original homework instructions used as the project guideline.

## Data Modeling

The ERD sketches the relationships between the six source CSV files before loading them into PostgreSQL.

![Employee Database ERD](ERD/QuickDBD-Mason%60s%20SQL%20Diagram.png)

## Data Engineering

The schema in `EmployeeSQL/table.sql` creates these tables:

- `departments`
- `employees`
- `dept_emp`
- `dept_manager`
- `salaries`
- `titles`

The schema defines primary keys and foreign key relationships so employee, department, salary, manager, and title records can be queried together.

## Data Analysis

`EmployeeSQL/queries.sql` answers the required questions:

- Employee number, last name, first name, gender, and salary.
- Employees hired in 1986.
- Manager for each department with department number, department name, employee number, name, and employment dates.
- Department for each employee.
- Employees named Hercules whose last name begins with `B`.
- Employees in the Sales department.
- Employees in the Sales and Development departments.
- Frequency count of employee last names in descending order.

## Bonus Analysis

The bonus notebook imports the SQL database into Pandas with SQLAlchemy, merges salaries with titles, calculates average salary by title, and exports a bar chart.

![Salary vs. Title](output_data/Salary%20vs.%20Title.png)

## How To Review

1. Create a local PostgreSQL database for the challenge.
2. Run `EmployeeSQL/table.sql` to create the schema.
3. Import each CSV from `data` into its matching SQL table.
4. Run `EmployeeSQL/queries.sql` to review the required results.
5. Open `sql_bonus/sql_bonus.ipynb` to review the optional bonus analysis.

## Notes

- The bonus notebook contains a local SQLAlchemy connection string and may need to be updated for your PostgreSQL username, password, host, port, and database name.
- Local database config files, Python cache files, Jupyter checkpoint folders, and homework guideline files are ignored by `09-sql/.gitignore`.
