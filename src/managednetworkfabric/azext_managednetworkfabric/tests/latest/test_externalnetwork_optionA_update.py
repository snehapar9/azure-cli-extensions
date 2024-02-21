# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# --------------------------------------------------------------------------------------------
# pylint: disable=too-few-public-methods,unnecessary-pass,unused-argument

"""
External Network tests scenarios
"""

from azure.cli.testsdk import ScenarioTest, ResourceGroupPreparer
from .config import CONFIG


def setup_scenario1(test):
    ''' Env setup_scenario1 '''
    pass


def cleanup_scenario1(test):
    '''Env cleanup_scenario1 '''
    pass


def call_scenario1(test):
    ''' # Testcase: scenario1'''
    setup_scenario1(test)
    step_update_s1(test, checks=[])
    step_show(test, checks=[])
    step_list_resource_group(test, checks=[])
    cleanup_scenario1(test)


def step_show(test, checks=None):
    '''externalnetwork show operation'''
    if checks is None:
        checks = []
    test.cmd(
        'az networkfabric externalnetwork show --resource-name {name} --l3domain {l3domain} --resource-group {rg}')


def step_update_s1(test, checks=None):
    '''externalnetwork update operation'''
    if checks is None:
        checks = []
    test.cmd(
        'az networkfabric externalnetwork update --resource-group {rg} --l3domain {l3domain} --resource-name {name} --peering-option {s2_peering_option} --option-a-properties {updatedOptionAProperties} --nni-id {nni_Id} ', checks=checks)


def step_list_resource_group(test, checks=None):
    '''externalnetwork list by resource group operation'''
    if checks is None:
        checks = []
    test.cmd(
        'az networkfabric externalnetwork list --resource-group {rg} --l3domain {l3domain}')


class GA_ExternalNetworkOptionAUpdateScenarioTest1(ScenarioTest):
    ''' External Network Scenario test'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.kwargs.update({
            'name': CONFIG.get('EXTERNAL_NETWORK', 'updateName'),
            'rg': CONFIG.get('EXTERNAL_NETWORK', 'updateResourceGroup'),
            'l3domain': CONFIG.get('EXTERNAL_NETWORK', 'updatel3domain'),
            's2_peering_option': CONFIG.get('EXTERNAL_NETWORK', 's2_peering_option'),
            'updatedOptionAProperties': CONFIG.get('EXTERNAL_NETWORK', 'updated_option_a_properties'),
            'nni_Id': CONFIG.get('EXTERNAL_NETWORK', 'nni_Id')
        })

    def test_GA_externalnetwork_optionA_update_scenario1(self):
        ''' test scenario for externalnetwork CRUD operations'''
        call_scenario1(self)
