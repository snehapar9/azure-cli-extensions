# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command_group(
    "network firewall policy rule-collection-group collection",
)
class __CMDGroup(AAZCommandGroup):
    """Manage and configure Azure firewall policy rule collections in the rule collection group.

    Currently, Azure Firewall policy support two kinds of rule collections which are Filter collection and NAT collection. There are three kinds of rules which are application rule, network rule and nat rule.
            NAT collection support having a list of nat rule. Filter collection support including a list of rules(network rule or application rule) in it. But all of rules should be the same type.
    """
    pass


__all__ = ["__CMDGroup"]
