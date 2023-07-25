# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------
import os
from azure.cli.testsdk import *
from azext_command_change.custom import meta_diff


class CommandChangeScenario(ScenarioTest):

    def test_diff_meta(self):
        if not os.path.exists("./jsons/az_monitor_meta_before.json") \
                or not os.path.exists("./jsons/az_monitor_meta_after.json"):
            return
        result = meta_diff(base_meta_file="./jsons/az_monitor_meta_before.json",
                           diff_meta_file="./jsons/az_monitor_meta_after.json",
                           output_type="text")
        target_message = [
            "please confirm cmd `monitor private-link-scope scoped-resource show` removed",
            "sub group `monitor private-link-scope private-endpoint-connection cust` removed",
        ]
        for mes in target_message:
            found = False
            for line in result:
                if line.find(mes) > -1:
                    found = True
                    break
            self.assertTrue(found, "target message not found")
