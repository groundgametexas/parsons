from urllib.parse import urlencode
import requests
import os
from parsons import Table
from typing import Optional
import json


class LegiScanError(Exception):
    """Exception raised for errors in the LegiScan API.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message


class Legiscan:
    """Interact with the LegiScan API."""

    BASE_URL = "http://api.legiscan.com/?key={0}&op={1}&{2}"

    def __init__(
        self,
        api_key: str = None,
    ):
        self.api_key = api_key or os.getenv("LEGISCAN_API_KEY")

    def _url(
        self,
        operation,
        params=None,
    ):
        """Build a URL for querying the API.

        Args:
            operation (str): The operation to perform.
            params (dict, optional): The parameters for the operation.

        Returns:
            str: The constructed URL.

        """
        if not isinstance(params, str) and params is not None:
            params = urlencode(params)
        elif params is None:
            params = ""
        return self.BASE_URL.format(self.api_key, operation, params)

    def _get(self, url):
        """Get and parse JSON from API for a given URL.

        Args:
            url (str): The URL to send the GET request to.

        Returns:
            dict: The parsed JSON response from the API.

        Raises:
            LegiScanError: If the request fails or if the API returns an error.

        """
        req = requests.get(url)
        if not req.ok:
            raise LegiScanError(
                "Request returned {0}: {1}".format(req.status_code, url)
            )
        data = json.loads(req.content)
        if data["status"] == "ERROR":
            raise LegiScanError(data["alert"]["message"])
        return data

    def get_session_list(
        self,
        state=None,
    ):
        """
        Get a list of all sessions for a state.
        This method hits the getSessionList endpoint.

        `Args:`
            state: str
                The state to get sessions for
        `Returns:`
            The response from the API
        """
        endpoint = "getSessionList"

        params = {"key": self.api_key, "op": endpoint}

        if state:
            params["state"] = state

        url = self._url(endpoint, params)
        response = self._get(url)

        return response

    def get_session_list_tbl(
        self,
        state: Optional[str] = None,
    ):
        """
        Get a list of all sessions for a state

        `Args:`
            state: str, optional
                The state to get sessions for
        `Returns:`
            A Parsons table of the response from the API
        """
        endpoint = "getSessionList"

        params = {"key": self.api_key, "op": endpoint}

        if state:
            params["state"] = state

        url = self._url(endpoint, params)
        response = self._get(url)

        return Table(response["sessions"])

    def get_master_list(
        self,
        state=None,
        session_id=None,
    ):
        """
        Get a list of all bills for a state

        `Args:`
            state: str
                The state to get bills for
        `Returns:`
            The response from the API
        """
        endpoint = "getMasterList"

        params = {"key": self.api_key, "op": endpoint}

        if state:
            params["state"] = state

        if session_id:
            params["session"] = str(session_id)

        url = self._url(endpoint, params)
        response = self._get(url)

        return response

    def get_master_list_tbl(
        self,
        state: Optional[str] = None,
        session_id: Optional[str] = None,
    ):
        """
        Get a list of all bills for a state

        `Args:`
            state: str, optional
                The state to get bills for
        `Returns:`
            A Parsons table of the response from the API
        """
        endpoint = "getMasterList"

        params = {"key": self.api_key, "op": endpoint}

        if state:
            params["state"] = state

        if session_id:
            params["session"] = str(session_id)

        url = self._url(endpoint, params)
        response = self._get(url)

        return Table(response["masterlist"])

    def get_session_people(
        self,
        session_id,
    ):
        """
        Get a list of all people for a session

        `Args:`
            session_id: str
                The session to get people for
        `Returns:`
            The response from the API
        """
        endpoint = "getSessionPeople"

        params = {"key": self.api_key, "op": endpoint}

        if session_id:
            params["id"] = str(session_id)

        url = self._url(endpoint, params)
        response = self._get(url)

        return response

    def get_bill(
        self,
        bill_id=None,
    ):
        """
        Get a bill by ID

        `Args:`
            bill_id: str
                The bill ID
        `Returns:`
            The response from the API
        """
        endpoint = "getBill"

        params = {"key": self.api_key, "op": endpoint}

        if bill_id:
            params["id"] = str(bill_id)

        url = self._url(endpoint, params)
        response = self._get(url)

        return response

    def get_dataset_list(
        self,
        state=None,
        year=None,
    ):
        """
        Get list of available datasets, with optional state and year filtering.
        """
        endpoint = "getDatasetList"

        params = {"key": self.api_key, "op": endpoint}

        if state:
            params["state"] = state

        if year:
            params["year"] = str(year)

        url = self._url(endpoint, params)
        response = self._get(url)
        dataset_list = response[
            "datasetlist"
        ]  # This is necessary to get the actual data

        return dataset_list

    def get_dataset(
        self,
        id,
        access_key=None,
    ):
        """
        Get list of available datasets, with optional state and year filtering.
        """
        endpoint = "getDataset"

        params = {"key": self.api_key, "op": endpoint}

        if id:
            params["id"] = str(id)

        if access_key:
            params["access_key"] = str(access_key)

        url = self._url(endpoint, params)
        response = self._get(url)
        dataset = response["dataset"]  # This is necessary to get the actual data

        return dataset
