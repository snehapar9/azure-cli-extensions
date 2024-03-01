# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer)
from azure.cli.testsdk.scenario_tests import AllowLargeResponse


class AstronomerScenario(ScenarioTest):

    @AllowLargeResponse(size_kb=10240)
    @ResourceGroupPreparer(name_prefix='cli_test_astronomer', location="eastus")
    def test_astronomer(self, resource_group):
        self.kwargs.update({
            'astronomer_name': self.create_random_name("astronomer", 15),
            'workspace_name': self.create_random_name("workspace", 15),
            'organization_name': self.create_random_name("organization", 20),
        })

        self.cmd('az astronomer organization create --resource-group {rg} --name {astronomer_name} --location "eastus" '
                 '--marketplace {{"subscription-id":"61641157-140c-4b97-b365-30ff76d9f82e",'
                 '"offer-details":{{"publisher-id":"astronomer1591719760654","offer-id":"astro","plan-id":"astro-paygo",'
                 '"plan-name":"\'Monthly Pay-As-You-Go\'","term-unit":"Monthly","term-id":"gmz7xq9ge3py"}}}} '
                 '--partner-organization {{"organization-name":{organization_name},"workspace-name":{workspace_name},'
                 '"single-sign-on-properties":{{"aad-domains":[""MicrosoftCustomerLed.onmicrosoft.com""]}}}} --user {{"first-name":"gaurav","last-name":"bang","email-address":"gauravbang@microsoft.com"}} ',
                 checks=[self.check('name', '{astronomer_name}'),
                         self.check('marketplace.offerDetails.offerId', "astro"),
                         self.check('marketplace.offerDetails.planId', "astro-paygo"),
                         self.check('partnerOrganizationProperties.organizationName', '{organization_name}'),
                         self.check('partnerOrganizationProperties.singleSignOnProperties.aadDomains[0]', "MicrosoftCustomerLed.onmicrosoft.com"),
                         self.check('provisioningState', 'Succeeded')])

        self.cmd('az astronomer organization list --resource-group {rg}', self.check('type(@)', 'array'),)
        self.cmd('az astronomer organization update --resource-group {rg} --name {astronomer_name} --tags {{"key1":"value1"}}')
        self.cmd('az astronomer organization show --resource-group {rg} --name {astronomer_name}',
                 self.check('tags', '{{\'key1\': \'value1\'}}'))
        self.cmd('az astronomer organization delete --resource-group {rg} --name {astronomer_name} -y')
