"""
LinkedIn Jobs API: A Quick Start Example
See more at: https://apify.com/johnvc/linkedin-jobs-api?fpr=9n7kx3
Input schema: https://apify.com/johnvc/linkedin-jobs-api/input-schema?fpr=9n7kx3

This script shows how to call the LinkedIn Jobs API on Apify from Python and
read its structured JSON output. Search public LinkedIn job listings by keyword,
location, seniority, and job type, and get one clean row per job (title, company,
location, salary, seniority, employment type, apply link, and more).

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# Kept small on purpose: one keyword-and-location search with maxJobs set to 5,
# so your first run stays cheap (you pay per job returned). Raise maxJobs, add
# filters (experienceLevel, jobType, remote, timeRange), or pass a list of
# specific postings in jobUrls to collect more.
run_input = {
    "keyword": "python developer",
    "location": "New York",
    # "experienceLevel": "mid-senior",   # internship, entry, associate, mid-senior, director, executive
    # "jobType": "full-time",            # full-time, part-time, contract, temporary, internship, volunteer
    # "remote": True,                    # return only remote roles
    # "timeRange": "past-week",          # past-day, past-week, past-month
    "maxJobs": 5,
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/linkedin-jobs-api").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset
# (apify-client 3.x returns a Run object; use .default_dataset_id, not run["..."])
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} job(s).\n")

# Show a few key fields from each job.
for item in items:
    print(f"Title:      {item.get('title')}")
    print(f"Company:    {item.get('companyName')}")
    print(f"Location:   {item.get('location')}")
    print(f"Seniority:  {item.get('seniorityLevel')}")
    print(f"Type:       {item.get('employmentType')}")
    print(f"Salary:     {item.get('salary')}")
    print(f"Posted:     {item.get('postedDate')}")
    print(f"Applicants: {item.get('numApplicants')}")
    print(f"Apply:      {item.get('applyUrl')}")
    print(f"URL:        {item.get('jobUrl')}")
    print(f"Summary:    {item.get('summary')}")
    print("-" * 60)
