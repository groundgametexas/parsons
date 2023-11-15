sample_users_response = {
    "count": 1,
    "next": None,
    "previous": None,
    "results": [
        {
            "url": "https://api.callhub.io/v1/users/6783/",
            "username": "readme",
            "email": "hello@callhub.io",
            "bphones": ["https://api.callhub.io/v1/bphone/49765/"],
            "phonebooks": [
                "https://api.callhub.io/v1/phonebooks/78220/",
                "https://api.callhub.io/v1/phonebooks/72819/",
            ],
            "voice_broadcasts": ["https://api.callhub.io/v1/voice_broadcasts/22604/"],
            "sms_campaigns": [
                "https://api.callhub.io/v1/sms_campaigns/51262/",
                "https://api.callhub.io/v1/sms_campaigns/17466/",
                "https://api.callhub.io/v1/sms_campaigns/12873/",
                "https://api.callhub.io/v1/sms_campaigns/113459/",
                "https://api.callhub.io/v1/sms_campaigns/10564/",
                "https://api.callhub.io/v1/sms_campaigns/184564/",
            ],
            "callcenter_campaigns": [
                "https://api.callhub.io/v1/callcenter_campaigns/2441/",
                "https://api.callhub.io/v1/callcenter_campaigns/1024/",
                "https://api.callhub.io/v1/callcenter_campaigns/9450/",
                "https://api.callhub.io/v1/callcenter_campaigns/14562/",
                "https://api.callhub.io/v1/callcenter_campaigns/1700/",
                "https://api.callhub.io/v1/callcenter_campaigns/6324/",
                "https://api.callhub.io/v1/callcenter_campaigns/6124/",
                "https://api.callhub.io/v1/callcenter_campaigns/8149/",
            ],
        }
    ],
}


fake_contacts_data = {
    "count": 99999,
    "next": "https://api.callhub.io/v1/contacts/?page=3",
    "previous": "https://api.callhub.io/v1/contacts/",
    "results": [
        {
            "url": "https://api.callhub.io/v1/contacts/2668997876889779098/",
            "id": 2668997876889779098,
            "pk_str": "2668997876889779098",
            "owner": "owner@example.com",
            "phonebooks": ["https://api.callhub.io/v1/phonebooks/3095579218512184334/"],
            "contact": "(750)397-9316",
            "mobile": "(750)397-9316",
            "last_name": "Beltran",
            "first_name": "Pamela",
            "country_code": "US",
            "email": "pamela.beltran@example.com",
            "created_date": "2023-11-15T18:20:26.fZ",
            "address": "855 Zuniga Valleys",
            "city": "Duffyborough",
            "tags": [],
            "street_address_line1": None,
            "state": "AS",
            "zipcode": "35311",
            "company_name": "",
            "company_website": "",
            "job_title": "",
            "custom_fields": "null",
        },
        {
            "url": "https://api.callhub.io/v1/contacts/4350655856540923327/",
            "id": 4350655856540923327,
            "pk_str": "4350655856540923327",
            "owner": "owner@example.com",
            "phonebooks": ["https://api.callhub.io/v1/phonebooks/3095579218512184334/"],
            "contact": "(403)584-9430x9998",
            "mobile": "(403)584-9430x9998",
            "last_name": "Gallagher",
            "first_name": "Daryl",
            "country_code": "US",
            "email": "daryl.gallagher@example.com",
            "created_date": "2023-11-15T18:20:26.fZ",
            "address": "91179 Holt Trafficway",
            "city": "Tinamouth",
            "tags": [],
            "street_address_line1": None,
            "state": "AR",
            "zipcode": "55721",
            "company_name": "",
            "company_website": "",
            "job_title": "",
            "custom_fields": "null",
        },
        {
            "url": "https://api.callhub.io/v1/contacts/8266820286885042015/",
            "id": 8266820286885042015,
            "pk_str": "8266820286885042015",
            "owner": "owner@example.com",
            "phonebooks": ["https://api.callhub.io/v1/phonebooks/3095579218512184334/"],
            "contact": "6592611772",
            "mobile": "6592611772",
            "last_name": "Whitney",
            "first_name": "John",
            "country_code": "US",
            "email": "john.whitney@example.com",
            "created_date": "2023-11-15T18:20:26.fZ",
            "address": "7144 Sarah Station Apt. 504",
            "city": "South Marcusstad",
            "tags": [],
            "street_address_line1": None,
            "state": "NE",
            "zipcode": "39178",
            "company_name": "",
            "company_website": "",
            "job_title": "",
            "custom_fields": "null",
        },
        {
            "url": "https://api.callhub.io/v1/contacts/7272165290822209374/",
            "id": 7272165290822209374,
            "pk_str": "7272165290822209374",
            "owner": "owner@example.com",
            "phonebooks": ["https://api.callhub.io/v1/phonebooks/3095579218512184334/"],
            "contact": "7573656934",
            "mobile": "7573656934",
            "last_name": "Jones",
            "first_name": "Morgan",
            "country_code": "US",
            "email": "morgan.jones@example.com",
            "created_date": "2023-11-15T18:20:26.fZ",
            "address": "760 Scott Mountains Apt. 251",
            "city": "South Patriciafort",
            "tags": [],
            "street_address_line1": None,
            "state": "SD",
            "zipcode": "10793",
            "company_name": "",
            "company_website": "",
            "job_title": "",
            "custom_fields": "null",
        },
        {
            "url": "https://api.callhub.io/v1/contacts/4288700836033639775/",
            "id": 4288700836033639775,
            "pk_str": "4288700836033639775",
            "owner": "owner@example.com",
            "phonebooks": ["https://api.callhub.io/v1/phonebooks/3095579218512184334/"],
            "contact": "+1-825-824-2613",
            "mobile": "+1-825-824-2613",
            "last_name": "Meyer",
            "first_name": "Patricia",
            "country_code": "US",
            "email": "patricia.meyer@example.com",
            "created_date": "2023-11-15T18:20:26.fZ",
            "address": "08282 Johnson Stream Suite 373",
            "city": "Lake Joan",
            "tags": [],
            "street_address_line1": None,
            "state": "MS",
            "zipcode": "05429",
            "company_name": "",
            "company_website": "",
            "job_title": "",
            "custom_fields": "null",
        },
        {
            "url": "https://api.callhub.io/v1/contacts/8459040613713130424/",
            "id": 8459040613713130424,
            "pk_str": "8459040613713130424",
            "owner": "owner@example.com",
            "phonebooks": ["https://api.callhub.io/v1/phonebooks/3095579218512184334/"],
            "contact": "001-582-687-6419x12499",
            "mobile": "001-582-687-6419x12499",
            "last_name": "Greer",
            "first_name": "Kathleen",
            "country_code": "US",
            "email": "kathleen.greer@example.com",
            "created_date": "2023-11-15T18:20:26.fZ",
            "address": "244 Wendy Branch",
            "city": "Lake Michelleborough",
            "tags": [],
            "street_address_line1": None,
            "state": "KY",
            "zipcode": "42787",
            "company_name": "",
            "company_website": "",
            "job_title": "",
            "custom_fields": "null",
        },
        {
            "url": "https://api.callhub.io/v1/contacts/6434439012459100120/",
            "id": 6434439012459100120,
            "pk_str": "6434439012459100120",
            "owner": "owner@example.com",
            "phonebooks": ["https://api.callhub.io/v1/phonebooks/3095579218512184334/"],
            "contact": "(389)925-2155",
            "mobile": "(389)925-2155",
            "last_name": "Frey",
            "first_name": "Madison",
            "country_code": "US",
            "email": "madison.frey@example.com",
            "created_date": "2023-11-15T18:20:26.fZ",
            "address": "560 Farmer Row",
            "city": "South Chadhaven",
            "tags": [],
            "street_address_line1": None,
            "state": "OR",
            "zipcode": "94001",
            "company_name": "",
            "company_website": "",
            "job_title": "",
            "custom_fields": "null",
        },
        {
            "url": "https://api.callhub.io/v1/contacts/5108536931301404372/",
            "id": 5108536931301404372,
            "pk_str": "5108536931301404372",
            "owner": "owner@example.com",
            "phonebooks": ["https://api.callhub.io/v1/phonebooks/3095579218512184334/"],
            "contact": "6226183335",
            "mobile": "6226183335",
            "last_name": "Ruiz",
            "first_name": "Derrick",
            "country_code": "US",
            "email": "derrick.ruiz@example.com",
            "created_date": "2023-11-15T18:20:26.fZ",
            "address": "25563 Michael Valleys Apt. 919",
            "city": "Davilaburgh",
            "tags": [],
            "street_address_line1": None,
            "state": "OH",
            "zipcode": "99652",
            "company_name": "",
            "company_website": "",
            "job_title": "",
            "custom_fields": "null",
        },
        {
            "url": "https://api.callhub.io/v1/contacts/2174665575312854714/",
            "id": 2174665575312854714,
            "pk_str": "2174665575312854714",
            "owner": "owner@example.com",
            "phonebooks": ["https://api.callhub.io/v1/phonebooks/3095579218512184334/"],
            "contact": "611.982.1478x4504",
            "mobile": "611.982.1478x4504",
            "last_name": "Arias",
            "first_name": "Misty",
            "country_code": "US",
            "email": "misty.arias@example.com",
            "created_date": "2023-11-15T18:20:26.fZ",
            "address": "579 William Trace",
            "city": "South Kevintown",
            "tags": [],
            "street_address_line1": None,
            "state": "AZ",
            "zipcode": "57964",
            "company_name": "",
            "company_website": "",
            "job_title": "",
            "custom_fields": "null",
        },
        {
            "url": "https://api.callhub.io/v1/contacts/3328498878567343270/",
            "id": 3328498878567343270,
            "pk_str": "3328498878567343270",
            "owner": "owner@example.com",
            "phonebooks": ["https://api.callhub.io/v1/phonebooks/3095579218512184334/"],
            "contact": "716-656-8428",
            "mobile": "716-656-8428",
            "last_name": "Hayes",
            "first_name": "Sheri",
            "country_code": "US",
            "email": "sheri.hayes@example.com",
            "created_date": "2023-11-15T18:20:26.fZ",
            "address": "0711 Michael Mount Suite 403",
            "city": "Jamesbury",
            "tags": [],
            "street_address_line1": None,
            "state": "NC",
            "zipcode": "09305",
            "company_name": "",
            "company_website": "",
            "job_title": "",
            "custom_fields": "null",
        },
    ],
}
