import pytest
import requests


def test_file1_method1():
        people = {            
            "first_name": "James",
            "last_name": "Larry",
            "birthdate": "2023-01-30", 
            "email": "jlarry@example.co",
            "custom_properties": {
                "airtable_id": "1",
                "lifetime_value": 125500.0
            }
        }
        result = requests.post('https://challenge-automation-engineer-xij5xxbepq-uc.a.run.app/contacts/', auth=("datacose","196D1115456D7"), json=people).json()
        print(result)
        post_result = {
            "first_name": result["first_name"],
            "last_name": result["last_name"],
            "birthdate": result["birthdate"],
            "email": result["email"],
            "custom_properties": {
                "airtable_id": "1",
                "lifetime_value": result["custom_properties"]["lifetime_value"]
            },
        }
        assert people == post_result, "test failed"