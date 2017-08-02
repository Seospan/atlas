import requests
import json

base_url = "https://graph.atlassolutions.com"
version = "v2.8"
token = "EAAHDx0xcJroBAHO0DIZA9UsNMo5fPPTTQxJEeWflNvarlCQdZAFiRV0tSVhWVx34f1eYuXM6SbjpnyhfQyihiNxs38QxXGkjVBKLt1lRZCzWJzKKJZAubyVFetDb7EWAQCsyROffZAHvXXqmDpJCoQMKw1V4nNbFBQv9iXZC7gwk2g4gllo0HOVU8h4aIDkSwGO1WDOzjdFziJyLajl97ZC"
headers = {'Content-Type': 'application/json', 'Accept':'application/json'}

#r = requests.get(base_url+"/"+version+"/me/companies?access_token="+token)
#print(r.json()['data'])

mec_id = "11237200399751"

report_details = [
    {
        "name": "Test Report",
        "version": 1,
        "description": "",
        "definition": {
            "report_type": "column_determined",
            "column_definitions": [
                {
                    "area": "serving",
                    "category": "standard",
                    "key": "ad_id",
                    "name": "Ad ID",
                    "attribution_model": "null",
                    "aggregation_usage": "dimension"
                },
            ],
            "date_range": {
                "type": "relative",
                "date_unit": "day",
                "quantity": "2",
                "time_zone": "America/New_York"
            },
            "time_zone": "America/New_York",
            "crosstab_columns": [],
        },
        "file_format": "xlsx",
        "is_email_enabled": False,
        "email_addresses": [],
        "email_suffix": ""
    }
]
#print(type(report_details))
print(type(json.dumps(report_details)))
#report_creation = requests.post(base_url+"/"+version+"/"+mec_id+"/reports?access_token="+token, data = json.dumps(report_details), headers=headers)
#report_creation = requests.post(base_url+"/"+version+"/"+mec_id+"/reports?access_token="+token, json = report_details, headers=headers)

report_creation = requests.post(base_url+"/"+version+"/11237205327717/report_schedules?access_token="+token, data = json.dumps(report_details), headers=headers)
print(report_creation.raw)
print(report_creation.url)
print(report_creation.status_code)
print(report_creation.text)
