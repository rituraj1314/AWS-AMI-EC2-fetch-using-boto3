import boto3
import pandas as pd
import datetime
import sys
from openpyxl import Workbook
from openpyxl.styles import Font

def fetch_and_generate_report_for_region(region_name, aws_access_key_id, aws_secret_access_key):
    if(region_name == "eu-central-1"):
        print("Fetching instances for abc")
    else:
        print("Fetching instances for def")

    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )
    ec2_client = session.client('ec2')

    # Fetch instances
    response = ec2_client.describe_instances()

    # Initialize list for data
    data = {
        "Instance Name": [],
        "Account Owner": [],
        "Age (Days)": []
    }

    # Iterate over instances and extract details
    for reservation in response.get('Reservations', []):
        for instance in reservation.get('Instances', []):
            instance_name = 'Unknown'
            account_owner = 'Unknown'
            for tag in instance.get('Tags', []):
                if tag['Key'] == 'Name':
                    name_parts = tag['Value'].split('-')
                    if len(name_parts) > 3:
                        instance_name = '-'.join(name_parts[1:-1])
                    else:
                        instance_name = tag['Value']
                elif tag['Key'] == 'account-owner':
                    account_owner = tag['Value']

            launch_date = instance.get('LaunchTime')
            current_date = datetime.datetime.now(datetime.timezone.utc)
            difference = current_date - launch_date
            days_difference = difference.days

            data["Instance Name"].append(instance_name)
            data["Account Owner"].append(account_owner)
            data["Age (Days)"].append(days_difference)

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Sort DataFrame by age in ascending order
    df = df.sort_values(by='Age (Days)', ascending=False)
    # Save DataFrame to Excel with first row in bold
    output_file = 'def_instances_ami_status.xlsx' if region_name == "eu-central-1" else 'abc_instances_ami_status.xlsx'

    wb = Workbook()
    ws = wb.active

    # Write headers
    headers = ["Instance Name", "Account Owner", "Age (Days)"]
    ws.append(headers)
    print("Saving the file")
    # Apply bold font to the first row
    for cell in ws[1]:
        cell.font = Font(bold=True)

    # Write data rows
    for row in df.itertuples(index=False):
        ws.append(list(row))

    # Save workbook
    wb.save(output_file)

    print(f"Data has been written to {output_file}")

if __name__ == "__main__":
    region_name = sys.argv[1]
    aws_access_key_id = sys.argv[2]
    aws_secret_access_key = sys.argv[3]
    fetch_and_generate_report_for_region(region_name, aws_access_key_id, aws_secret_access_key)
    print("Script completed successfully")
