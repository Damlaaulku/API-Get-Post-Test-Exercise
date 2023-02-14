from datetime import datetime
from decimal import Decimal
from re import sub
import requests


class DataCose:

    def __init__(self):
        self._data = {}
        self.get_response()

    def get_response(self):
        headers = {
            'accept': 'application/json',
            'authorization': 'fFz8Z7OpPTSY7gpAFPrWntoMuo07ACjp'
        }

        response = requests.get('https://challenge-automation-engineer-xij5xxbepq-uc.a.run.app/people/', headers=headers)
        self._data = response.json()
        for people in self._data:
            self.send_request(people)

    def send_request(self, people):
        fields = people.get("fields")
        birth_date = datetime.strptime(fields.get("dateOfBirth"), '%d-%m-%Y')
        lifetime_value = fields.get("lifetime_value")
        json_body ={
            "first_name": fields.get("firstName").strip(),
            "last_name": fields.get("lastName").strip(),
            "birthdate": birth_date.strftime('%Y-%m-%d'),
            "email": fields.get("email"),
            "custom_properties": {
                "airtable_id": people.get("id"),
                "lifetime_value": Decimal(sub(r'[^\d.]', '', lifetime_value))
            },
            "id": people.get("id")
        }
        request = requests.post('https://challenge-automation-engineer-xij5xxbepq-uc.a.run.app/contacts/', auth=("datacose","196D1115456D7"), json=json_body)
        return request.json()

if __name__ == "__main__":
    DataCose()
