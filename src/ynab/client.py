"""
HTTP client for talking to the YNAB API.
"""

import json
import requests

import file as f

# Could get the server-last-seen value out of the response as well so that I can stash it
# Otherwise, I can just do a really naive fetch all the data every time
# Totally wipe / reinsert everything every time. Honestly that's okay I think

# TODO: Put timestamp in cached json value ?


class YnabClient:
    """
    Makes requests to the YNAB API.
    """

    def __init__(self, token, use_cache: bool = True):
        self._api_url = "https://api.youneedabudget.com/v1/"
        self._headers = {"Authorization": "Bearer " + token}
        self._use_cache = use_cache

    def _request(self, uri, resource):
        cache_path = f"./.cache/{resource}.json"
        cached = f.read(cache_path)

        if self._use_cache and cached is not None:
            return json.loads(cached)

        res = requests.get(uri, headers=self._headers)
        data = res.json()

        if res.ok:
            resources = data["data"][resource]
            f.write(cache_path, json.dumps(resources))
            return resources
        else:
            return data["error"]

    def _get_resource(self, resource: str, resource_id: str = ""):
        uri = self._api_url + resource + resource_id
        return self._request(uri, resource)

    def _get_budget_resource(self, budget_id, resource):
        uri = self._api_url + "budgets/" + budget_id + "/" + resource
        return self._request(uri, resource)

    def get_budgets(self):
        """
        Fetch Budgets from YNAB.
        I only use one budget, so the goal here is just to get the ID
        for my one budget.
        """
        return self._get_resource("budgets")

    def get_transactions(self, budget_id):
        """
        A transaction is the fundamental entity in YNAB that we care about.
        It is an instance of spending a specific amount of money at a specific place.
        """
        return self._get_budget_resource(budget_id, "transactions")
