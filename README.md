# AWS-EC2-report-generator-using-boto3

This Python project fetches EC2 instance information from AWS and generates an Excel report detailing the instance name, account owner, and the age of the instances (in days) for a given AWS region. It utilizes the **boto3**, **pandas**, and **openpyxl** libraries to interact with AWS and generate the report in Excel format.

`Note:- To be run at GitLab`

## Files in the Repository

1. `env_list.py`: This is the main script responsible for fetching the EC2 instance details and generating the report.
2. `requirements.txt`: Lists the required dependencies to run the script.
3. `.gitlab-ci.yml`: CI/CD pipeline configuration for automating the running of the script in GitLab.

## Dependencies

To run this project, the following Python libraries are required:

* `boto3`: AWS SDK for Python to interact with EC2 instances.
* `pandas`: To organize and manipulate the fetched data.
* `openpyxl`: To create and save the Excel report.

You can install these dependencies using the command:

```bash
pip install -r requirements.txt
```

## Usage

The script can be run from the command line with the following syntax:

```bash
python env_list.py <region_name> <aws_access_key_id> <aws_secret_access_key>
```

* `region_name`: AWS region where the instances are located (e.g., `eu-central-1`).
* `aws_access_key_id`: Your AWS access key ID.
* `aws_secret_access_key`: Your AWS secret access key.

For example:

```bash
python env_list.py eu-central-1 YOUR_ACCESS_KEY_ID YOUR_SECRET_ACCESS_KEY
```

## Output

The script will generate an Excel file with instance information:

* For the `eu-central-1` region: `def_instances_ami_status.xlsx`
* For other regions: `abc_instances_ami_status.xlsx`

The Excel report contains the following columns:

* **Instance Name**: Name of the EC2 instance.
* **Account Owner**: The owner of the account where the instance resides.
* **Age (Days)**: The number of days since the instance was launched.

## Features

* Fetches EC2 instance data based on region.
* Organizes and sorts instances by age.
* Exports the data to an Excel file with proper formatting (headers in bold).

## License

This project is licensed under the MIT License.
Age (Days): The number of days since the instance was launched.
Features
Fetches EC2 instance data based on region.
Organizes and sorts instances by age.
Exports the data to an Excel file with proper formatting (headers in bold).
License
This project is licensed under the MIT License.
