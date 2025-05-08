# Data Generator of Mobiles and Laptop Sales

A Python-based project designed to analyze data for testing and development purposes about the employees of a compnay in USA.

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

Requirements for the software and other tools to build, test, and run the project:  
- [Python 3.8+](https://www.python.org/downloads/)  
- [pip](https://pip.pypa.io/en/stable/installation/)  

### Installing

Follow these steps to set up the development environment:

1. Clone the repository:  
    ```bash
    git clone https://github.com/SamuRoj/Data_Parsing_Processing
    cd data_analysis
    ```

2. Install dependencies:  
    ```bash
    pip install -r requirements.txt
    ```

3. Execute each step of the notebook (main.ipynb)

## Dataset Structure

| Column Name           | Description                                                                  | Data Type | Statistical Distribution |
|-----------------------|------------------------------------------------------------------------------|-----------|--------------------------|
| **Employee Id**        | Unique identifier for each employee.                                          | String    | Uniform                  |
| **First Name**         | First name of the employee.                                                   | String    | Uniform                  |
| **Last Name**          | Last name of the employee.                                                    | String    | Uniform                  |
| **Email**              | Email address of the employee.                                                | String    | Uniform                  |
| **Phone Number**       | Phone number of the employee.                                                 | String    | Uniform                  |
| **Department**         | Department where the employee works (e.g., HHRR, IT, Marketing).                | String    | Uniform              |
| **Job Title**          | Job title of the employee (e.g., Manager, Developer, Designer).               | String    | Categorical              |
| **Hire Date**          | Date when the employee was hired.                                             | Date      | Uniform                  |
| **Days Service**       | Number of days the employee has been with the company.                        | Integer   | Uniform                  |
| **Base Salary**        | Base salary of the employee in USD.                                           | Integer   | Normal Left Skewed                  |
| **Bonus Percentage**   | Percentage of bonus the employee is eligible for.                             | Integer   | Normal                   |
| **Status**             | Employment status of the employee (e.g., Active, Inactive, Leave).         | String    | Categorical              |
| **Birth Date**         | Date of birth of the employee.                                                | Date      | Uniform                  |
| **Address**            | Residential address of the employee.                                          | String    | Uniform                  |
| **City**               | City where the employee lives.                                                | String    | Categorical              |
| **State**              | State where the employee lives.                                               | String    | Uniform             |
| **Zip Code**           | Postal code of the employee's address.                                        | String    | Uniform              |
| **Country**            | Country where the employee resides.                                           | String    | Uniform              |
| **Gender**             | Gender of the employee.                                                       | String    | Categorical              |
| **Education**          | Highest level of education attained by the employee.                          | String    | Categorical              |
| **Performance Score**  | Performance score of the employee (e.g., rating from reviews).     | Integer   | Normal                   |
| **Last Review Date**   | Date of the last review of the employee.                           | Date      | Uniform                  |
| **Employee Level**     | Level of the employee (e.g., Entry, Mid, Senior).                           | String    | Categorical              |
| **Vacation Days**      | Number of vacation days the employee is entitled to.                          | Integer   | Poisson                  |
| **Sick Days**          | Number of sick days the employee is entitled to.                              | Integer   | Poisson                  |
| **Work Location**      | The location where the employee works (e.g., Office, Remote, Hybrid).                 | String    | Categorical              |
| **Shift**              | Work shift of the employee (e.g., Day, Night, Flexible).                   | String    | Categorical              |
| **Emergency Contact**  | Name of the emergency contact for the employee.                               | String    | Uniform                  |
| **SSN**                | Social Security Number of the employee.                                       | String    | Uniform                  |
| **Bank Account**       | Bank account number of the employee for salary deposits.                      | String    | Uniform                  |


## Running the tests

To ensure the project works as expected, run the automated tests.

### Sample Tests

Run the unit tests to verify the functionality of the data generator:  
```bash
python -m unittest discover -v
```

### Current Coverage

Name                   Stmts   Miss  Cover
------------------------------------------
clean\__init__.py          0      0   100%
clean\clean_data.py       46      0   100%
test\__init__.py           0      0   100%
test\test_dataset.py      20      0   100%
------------------------------------------
TOTAL                     66      0   100%

## Built With

- [Python](https://www.python.org/) - Programming language  

## Authors

- **Samuel Rojas** - - [GitHub Profile](https://github.com/SamuRoj)
