import json
import datetime
import sys

data = sys.argv[1]

# read in JSON file
with open(data, 'r') as f:
    data = json.load(f)

# get current date
today = datetime.datetime.now().date()

unique_domains = set()

for domain in data['search_result']:
    expiry_date = datetime.datetime.strptime(domain['expiry_date'], '%Y-%m-%d').date()
    if expiry_date >= today:
        if domain['domain_name'] not in unique_domains:
            unique_domains.add(domain['domain_name'])
            print(domain['domain_name'])