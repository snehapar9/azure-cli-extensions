# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "automation configuration show",
)
class Show(AAZCommand):
    """Get the configuration identified by configuration name.

    :example: Get the configuration by its name
        az automation configuration show -g rg --automation-account-name myAutomationAccount -n SetupServer
    """

    _aaz_info = {
        "version": "2023-11-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.automation/automationaccounts/{}/configurations/{}", "2023-11-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.automation_account_name = AAZStrArg(
            options=["--account", "--automation-account-name"],
            help="The name of the automation account.",
            required=True,
            id_part="name",
        )
        _args_schema.configuration_name = AAZStrArg(
            options=["-n", "--name", "--configuration-name"],
            help="The configuration name.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.DscConfigurationGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class DscConfigurationGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/configurations/{configurationName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "automationAccountName", self.ctx.args.automation_account_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "configurationName", self.ctx.args.configuration_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-11-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.etag = AAZStrType()
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType()
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.creation_time = AAZStrType(
                serialized_name="creationTime",
            )
            properties.description = AAZStrType()
            properties.job_count = AAZIntType(
                serialized_name="jobCount",
            )
            properties.last_modified_time = AAZStrType(
                serialized_name="lastModifiedTime",
            )
            properties.log_verbose = AAZBoolType(
                serialized_name="logVerbose",
            )
            properties.node_configuration_count = AAZIntType(
                serialized_name="nodeConfigurationCount",
            )
            properties.parameters = AAZDictType()
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            properties.source = AAZObjectType()
            properties.state = AAZStrType()

            parameters = cls._schema_on_200.properties.parameters
            parameters.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.parameters.Element
            _element.default_value = AAZStrType(
                serialized_name="defaultValue",
            )
            _element.is_mandatory = AAZBoolType(
                serialized_name="isMandatory",
            )
            _element.position = AAZIntType()
            _element.type = AAZStrType()

            source = cls._schema_on_200.properties.source
            source.hash = AAZObjectType()
            source.type = AAZStrType()
            source.value = AAZStrType()
            source.version = AAZStrType()

            hash = cls._schema_on_200.properties.source.hash
            hash.algorithm = AAZStrType(
                flags={"required": True},
            )
            hash.value = AAZStrType(
                flags={"required": True},
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""


__all__ = ["Show"]
