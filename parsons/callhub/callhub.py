from requests import request as _request
from parsons.utilities.api_connector import APIConnector
from parsons.etl.table import Table
import os
import logging

logger = logging.getLogger(__name__)

CALLHUB_URI = "https://api.callhub.io/v1/"


class CallHub(object):
    """
    Instantiate CallHub Class

    The CallHub class allows you to interact with the CallHub API.
    https://developer.callhub.io/reference/

    `Args:`
        api_key: str
            An api key issued by Call Hub:
            Instructions on how to access this api_key can be found here:
            https://support.callhub.io/hc/en-us/articles/900001359603-Where-to-find-my-API-key-

            Alternatively, set the environment variable ``CALLHUB_API_KEY``.

    `Returns:`
        CallHub Class
    """

    def __init__(self, api_key=None):
        self.uri = CALLHUB_URI
        self.api_key = api_key or os.environ.get("CALLHUB_API_KEY")
        self.headers = {"Authorization": "Token " + self.api_key}
        self.client = APIConnector(CALLHUB_URI, headers=self.headers)

        if not self.api_key:
            logger.info(
                "CallHub API Key missing. Calling methods that rely on private"
                " endpoints will fail."
            )

    # Creating internal request methods to handle pagination and authentication

    def _request(self, url, req_type="GET", post_data=None, args=None, auth=True):
        if auth:
            if not self.api_key:
                raise TypeError("This method requires an api key.")
            else:
                header = {"Authorization": "Token " + self.api_key}
        else:
            header = None

        r = _request(req_type, url, json=post_data, params=args, headers=header)

        r.raise_for_status()

        if "error" in r.json():
            raise ValueError("API Error:" + str(r.json()["error"]))

        return r

    def _request_paginate(self, url, req_type="GET", args=None, auth=True):
        r = self._request(url, req_type=req_type, args=args, auth=auth)

        json = r.json()["results"]

        while r.json()["next"]:
            r = self._request(r.json()["next"], req_type=req_type, auth=auth)
            json.extend(r.json()["results"])

        return Table(json)

    # Creating methods to handle the different endpoints
    # I will be organizing these in the same order as the API documentation for CallHub

    # Contacts, Phonebooks

    def post_contacts(
        self,
        contact: str,
        mobile: str,
        last_name: str,
        first_name: str,
        country_code: str,
        email: str,
        address: str,
        city: str,
        state: str,
        company_name: str,
        company_website: str,
        job_title: str,
        phonebook_id,
    ):
        """
        Create contacts in a phonebook

        `Args:`
            contact: str
                The phone number of the contact
            mobile: str
                The mobile number of the contact
            last_name: str
                The last name of the contact
            first_name: str
                The first name of the contact
            country_code: str
                The country code of the contact
                2 letter country code.
                This is used to add the country prefix to the phone numbers, if necessary.
                See the full list of 2 letter country codes here
                http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
            email: str
                The email of the contact
            address: str
                The address of the contact
            city: str
                The city of the contact
            state: str
                The state of the contact
            company_name: str
                Name of the company/organisation the contact belongs to
            company_website: str
                Website of the company/organisation the contact belongs to
            job_title: str
                Job title of the contact
        `Returns:`
            Parsons Table
                See :ref:`parsons-table` for output options.
        """
        data = {
            "contact": contact,
            "mobile": mobile,
            "last_name": last_name,
            "first_name": first_name,
            "country_code": country_code,
            "email": email,
            "address": address,
            "city": city,
            "state": state,
            "company_name": company_name,
            "company_website": company_website,
            "job_title": job_title,
        }

        r = self._request_paginate(
            self.uri + "phonebooks/" + phonebook_id + "/contacts/",
            req_type="POST",
            post_data=data,
        )
        # Return empty table if no results
        if r.status_code == 201:
            return Table(r.json())
        else:
            raise Exception("Error: " + str(r.status_code) + " " + str(r.json()))

    def get_contacts(self):
        """
        Get all contacts

        `Returns:`
            Parsons Table
                See :ref:`parsons-table` for output options.
        """
        tbl = self._request_paginate(self.uri + "contacts/")
        # Return empty table if no results
        if tbl.num_rows == 0:
            return Table()
        else:
            return tbl

    def get_phonebooks(self):
        """
        Get all phonebooks

        `Returns:`
            Parsons Table
                See :ref:`parsons-table` for output options.
        """
        tbl = self._request_paginate(self.uri + "phonebooks/")
        # Return empty table if no results
        if tbl.num_rows == 0:
            return Table()
        else:
            return tbl

    def put_contacts(
        self,
        id: str,
        contact: str,
        mobile: str,
        last_name: str,
        first_name: str,
        country_code: str,
        email: str,
        address: str,
        city: str,
        state: str,
        company_name: str,
        company_website: str,
        job_title: str,
    ):
        """
        Update a contact

        `Args:`
            id: str
                The id of the contact to update
        `Returns:`
            Parsons Table
                See :ref:`parsons-table` for output options.
        """
        r = self._request_paginate(self.uri + "contacts/" + id + "/")
        # Return empty table if no results
        if r.status_code == 200:
            return Table(r.json())
        else:
            raise Exception("Error: " + str(r.status_code) + " " + str(r.json()))

    def delete_contacts(self, id: str):
        """
        Delete a contact

        `Args:`
            id: str
                The id of the contact to delete
        `Returns:`
            Status Code
        """
        r = self._request_paginate(self.uri + "contacts/" + id + "/", req_type="DELETE")
        # Return empty table if no results
        if r.status_code == 204:
            return r.status_code
        else:
            raise Exception("Error: " + str(r.status_code) + " " + str(r.json()))

    # Webhooks TODO

    # Call Center Campaigns TODO

    # Voice Broadcasts TODO

    def get_voice_broadcasts(self):
        """
        Get all voice broadcasts

        `Returns:`
            Parsons Table
                See :ref:`parsons-table` for output options.
        """
        tbl = self._request_paginate(self.uri + "voice_broadcasts/")
        # Return empty table if no results
        if tbl.num_rows == 0:
            return Table()
        else:
            return tbl

    # SMS Campaigns TODO

    def get_sms_campaigns(self):
        """
        Get all SMS campaigns

        `Returns:`
            Parsons Table
                See :ref:`parsons-table` for output options.
        """
        tbl = self._request_paginate(self.uri + "sms_campaigns/")
        # Return empty table if no results
        if tbl.num_rows == 0:
            return Table()
        else:
            return tbl

    # Users

    def get_users(self, limit=None, offset=None):
        """
        Get all users

        `Args:`
            limit: str
                Limit the number of users returned
            offset: str
                Offset the number of users returned

        `Returns:`
            Parsons Table
                See :ref:`parsons-table` for output options.
        """
        args = {"limit": limit, "offset": offset}
        tbl = self._request_paginate(self.uri + "users/", args=args)
        # Return empty table if no results
        if tbl.num_rows == 0:
            return Table()
        else:
            return tbl

    # Do Not Call
    # TODO: Add DNC List and DNC Contact methods
    # https://developers.callhub.io/api/#dnc-lists

    def post_dnc_contacts(self, dnc, phone_number):
        """
        Add a contact to a dnc list

        `Args:`
            dnc: str
                URL of the DNC list that the phone number belongs to
            phone_number: str
                Phone number of the contact.

        `Returns:`
            Parsons Table
                See :ref:`parsons-table` for output options.
        """
        url = self.uri + "dnc_contacts/"
        post_data = {"dnc": dnc, "phone_number": phone_number}
        r = self._request(url, req_type="POST", post_data=post_data)

        # Below I have found that if I send the same phone number that already exists in the
        # DNC list it raises:
        # requests.exceptions.HTTPError: 400 Client Error:
        # Bad Request for url: https://api.callhub.io/v1/dnc_contacts/
        # I need to handle this when trying to send numbers that may already exist in the DNC list
        if r.status_code == 201:
            return r.json()
        else:
            raise Exception(f"Error adding DNC contact: {r.status_code} - {r.text}")

    def get_dnc_contacts(self):
        """
        Get all dnc contacts

        `Returns:`
            Parsons Table
                See :ref:`parsons-table` for output options.
        """
        tbl = self._request_paginate(self.uri + "dnc_contacts/")
        # Return empty table if no results
        if tbl.num_rows == 0:
            return Table()
        else:
            return tbl

    def put_dnc_contacts(self, id, dnc, phone_number):
        """
        Update a dnc contact

        `Args:`
            dnc_contact_id: str
                ID of the dnc contact to update
            dnc: str
                URL of the DNC list that the phone number belongs to
            phone_number: str
                Phone number of the contact.

        `Returns:`
            Parsons Table
                See :ref:`parsons-table` for output options.
        """
        url = self.uri + f"dnc_contacts/{id}/"
        put_data = {"dnc": dnc, "phone_number": phone_number}
        r = self._request(url, req_type="PUT", put_data=put_data)

        if r.status_code == 200:
            return Table(r.json())
        else:
            raise Exception(f"Error updating DNC contact: {r.status_code} - {r.text}")

    # TODO Something is wrong with this method.
    # It is deleting the contact but it's returning an error.

    def delete_dnc_contacts(self, dnc_contact_id):
        """
        Delete a dnc contact

        `Args:`
            dnc_contact_id: str
                ID of the dnc contact to delete

        `Returns:`
            None
        """
        url = self.uri + f"dnc_contacts/{dnc_contact_id}/"
        r = self._request(url, req_type="DELETE")

        if r.status_code == 204:
            return r.status_code
        else:
            raise Exception(f"Error deleting DNC contact: {r.status_code} - {r.text}")

    def post_dnc_lists(self, name):
        """
        Create a DNC list

        `Args:`
            name: str
                Name of the DNC list

        `Returns:`
            Parsons Table
                See :ref:`parsons-table` for output options.
        """
        url = self.uri + "dnc_lists/"
        post_data = {"name": name}
        r = self._request(url, req_type="POST", post_data=post_data)

        if r.status_code == 201:
            return r.json()
        else:
            raise Exception(f"Error creating DNC list: {r.status_code} - {r.text}")

    def get_dnc_lists(self, limit=None, offset=None):
        """
        Get all dnc lists

        `Args:`
            limit: str
                Limit the number of dnc lists returned
            offset: str
                Offset the number of dnc lists returned

        `Returns:`
            Parsons Table
                See :ref:`parsons-table` for output options.
        """
        args = {"limit": limit, "offset": offset}
        tbl = self._request_paginate(self.uri + "dnc_lists/", args=args)
        # Return empty table if no results
        if tbl.num_rows == 0:
            return Table()
        else:
            return tbl

    # Agents TODO

    # Teams TODO

    # Agent Console TODO

    # Agent Campaigns TODO

    # Subscriber TODO

    # Conference TODO

    # Preview Dialer TODO

    # Peer to Peer Texting TODO

    # Analytics TODO
