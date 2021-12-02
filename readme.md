[comment]: # " File: readme.md"
[comment]: # "  Copyright (c) 2014-2021 Splunk Inc."
[comment]: # ""
[comment]: # "Licensed under the Apache License, Version 2.0 (the 'License');"
[comment]: # "you may not use this file except in compliance with the License."
[comment]: # "You may obtain a copy of the License at"
[comment]: # ""
[comment]: # "    http://www.apache.org/licenses/LICENSE-2.0"
[comment]: # ""
[comment]: # "Unless required by applicable law or agreed to in writing, software distributed under"
[comment]: # "the License is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,"
[comment]: # "either express or implied. See the License for the specific language governing permissions"
[comment]: # "and limitations under the License."
[comment]: # ""
This app implements actions that manage an OpenDNS Umbrella domain list. OpenDNS allows third party
implementations like Phantom Enterprise to create and manage a list of domains (i.e. add, delete)
via what it calls 'custom integrations'. The Phantom OpenDNS Umbrella App requires such an
integration to be pre-configured on OpenDNS Umbrella. The steps to do this are outlined below:

-   Login to your OpenDNS dashboard and go to Configuration \> System Settings \> Integrations and
    click the "add a new custom integration" button.
-   Set the name of the custom integration to be "Phantom Orchestration Feed"
-   The UI will then present an integration URL. For example:
    **https://s-platform.api.opendns.com/1.0/events?customerKey=bac2bfa7-d134-4b85-a5ed-b1ffec027a91**
    One of the parameters to this URL is the customer key (GUID format). This value will be required
    while configuring the OpenDNS Umbrella asset on Phantom. The OpenDNS Umbrella App on Phantom
    will use this customer key while adding, listing and deleting domains.
-   OpenDNS Umbrella needs to be told to *block* the domain list that is managed by Phantom.
-   Go to Configuration \> Policy Settings \> Security Settings and click on the relevant Security
    Setting. Scroll down and choose 'Block' requests from the 'Phantom Orchestration Feed'

At the end of the above steps OpenDNS Umbrella has been configured to:  

-   Create a 'custom integration' domain list with a *customerKey* for Phantom to use
-   Use the domains belonging to the 'Phantom Orchestration Feed' to block DNS requests.

Next step is to configure an 'OpenDNS Umbrella' asset on Phantom and specify the 'customerKey' and
hit 'Test Connectivity' to validate the configuration.

More information about 'custom integrations' can be found
[here](ihttps://www.opendns.com/enterprise-security/threat-enforcement/features/custom-integrations/)
.  
A support article on the OpenDNS site about configuring custom integration can be found
[here](https://support.opendns.com/entries/67200684-OpenDNS-Umbrella-The-Umbrella-Enforcement-API-for-Custom-Integrations)  
