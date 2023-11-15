from faker import Faker
import random
import time

fake = Faker()

data = {
    "count": 10,
    "next": "https://api.callhub.io/v1/contacts/?page=3",
    "previous": "https://api.callhub.io/v1/contacts/",
    "results": [],
}

for _ in range(10):
    first_name = fake.first_name()
    last_name = fake.last_name()
    address = fake.street_address()
    city = fake.city()
    state = fake.state_abbr()
    zipcode = fake.zipcode()
    phone = fake.phone_number()
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"
    id = random.randint(1000000000000000000, 9999999999999999999)
    url = f"https://api.callhub.io/v1/contacts/{id}/"
    created_date = time.strftime("%Y-%m-%dT%H:%M:%S.%fZ", time.gmtime())

    person = {
        "url": url,
        "id": id,
        "pk_str": str(id),
        "owner": "owner@example.com",
        "phonebooks": ["https://api.callhub.io/v1/phonebooks/3095579218512184334/"],
        "contact": phone,
        "mobile": phone,
        "last_name": last_name,
        "first_name": first_name,
        "country_code": "US",
        "email": email,
        "created_date": created_date,
        "address": address,
        "city": city,
        "tags": [],
        "street_address_line1": None,
        "state": state,
        "zipcode": zipcode,
        "company_name": "",
        "company_website": "",
        "job_title": "",
        "custom_fields": "null",
    }

    data["results"].append(person)

print(data)
