# --
# File: opendnsumbrella_connector.py
#
# Copyright (c) Phantom Cyber Corporation, 2014-2018
#
# This unpublished material is proprietary to Phantom Cyber.
# All rights reserved. The methods and
# techniques described herein are considered trade secrets
# and/or confidential. Reproduction or distribution, in whole
# or in part, is forbidden except by express written permission
# of Phantom Cyber.
#
# --


OPENDNSUMB_JSON_DOMAIN = "domain"
OPENDNSUMB_JSON_CUSTKEY = "customer_key"
OPENDNSUMB_JSON_APIKEY = "api_key"
OPENDNSUMB_JSON_APISECRET = "api_secret"
OPENDNSUMB_JSON_PAGE_INDEX = "page_index"
OPENDNSUMB_JSON_DOMAIN_LIMIT = "limit"
OPENDNSUMB_JSON_TOTAL_DOMAINS = "total_domains"
OPENDNSUMB_JSON_DISABLE_SAFEGUARDS = "disable_safeguards"
OPENDNSUMB_LIST_UPDATED_WITH_GUID = "REST API returned success with id: {id}"
OPENDNSUMB_LIST_RETRIEVED = "Successfully retrieved destination lists"
OPENDNSUMB_DESTINATION_ADDED = "Successfully added destination to list"
OPENDNSUMB_DESTINATION_REMOVED = "Successfully removed destination from list"

OPENDNSUMB_ERR_CONNECTIVITY_TEST = "Connectivity test failed"
OPENDNSUMB_SUCC_CONNECTIVITY_TEST = "Connectivity test passed"
OPENDNSUMB_ERR_SERVER_CONNECTION = "Connection failed"
OPENDNSUMB_ERR_FROM_SERVER = "API failed, Status code: {status}, Message: {message}"
OPENDNSUMB_MSG_GET_DOMAIN_LIST_TEST = "Querying a single domain entry to check credentials"

OPENDNSUMB_USING_BASE_URL = "Using url: {base_url}"

OPENDNSUMB_REST_API_URL = "https://s-platform.api.opendns.com"
OPENDNSUMP_REST_API_VER = '1.0'
OPENDNSUMB_DEFAULT_PAGE_INDEX = 1
OPENDNSUMB_DEFAULT_DOMAIN_LIMIT = 200
