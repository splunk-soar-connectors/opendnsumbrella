# File: opendnsumbrella_consts.py
# Copyright (c) 2014-2021 Splunk Inc.
#
# SPLUNK CONFIDENTIAL - Use or disclosure of this material in whole or in part
# without a valid written license from Splunk Inc. is PROHIBITED.


OPENDNSUMB_JSON_DOMAIN = "domain"
OPENDNSUMB_JSON_CUSTKEY = "customer_key"
OPENDNSUMB_JSON_PAGE_INDEX = "page_index"
OPENDNSUMB_JSON_DOMAIN_LIMIT = "limit"
OPENDNSUMB_JSON_TOTAL_DOMAINS = "total_domains"
OPENDNSUMB_JSON_DISABLE_SAFEGUARDS = "disable_safeguards"
OPENDNSUMB_LIST_UPDATED_WITH_GUID = "REST API returned success with id: {id}"

OPENDNSUMB_ERR_CONNECTIVITY_TEST = "Test Connectivity Failed"
OPENDNSUMB_SUCC_CONNECTIVITY_TEST = "Test Connectivity Passed"
OPENDNSUMB_ERR_SERVER_CONNECTION = "Connection failed"
OPENDNSUMB_ERR_FROM_SERVER = "API failed, Status code: {status}, Message: {message}"
OPENDNSUMB_MSG_GET_DOMAIN_LIST_TEST = "Querying a single domain entry to check credentials"

OPENDNSUMB_USING_BASE_URL = "Using url: {base_url}"

OPENDNSUMB_REST_API_URL = "https://s-platform.api.opendns.com"
OPENDNSUMP_REST_API_VER = '1.0'
OPENDNSUMB_DEFAULT_PAGE_INDEX = 1
OPENDNSUMB_DEFAULT_DOMAIN_LIMIT = 200
