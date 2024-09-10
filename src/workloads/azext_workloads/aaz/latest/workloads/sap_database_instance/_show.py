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
    "workloads sap-database-instance show",
    is_preview=True,
)
class Show(AAZCommand):
    """Show the SAP Database Instance resource.

    :example: Get an overview of the Database Instance in a Virtual instance for SAP solutions (VIS)
        az workloads sap-database-instance show -g <resource-group-name> --sap-virtual-instance-name <vis-name> -n <db-instance-name>

    :example: Get an overview of the Database Instance  using the Azure resource ID of the App server instance
        az workloads sap-database-instance show --id <resource-id>
    """

    _aaz_info = {
        "version": "2023-10-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.workloads/sapvirtualinstances/{}/databaseinstances/{}", "2023-10-01-preview"],
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
        _args_schema.database_instance_name = AAZStrArg(
            options=["-n", "--name", "--database-instance-name"],
            help="Database resource name string modeled as parameter for auto generation to work correctly.",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern="^.*",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.sap_virtual_instance_name = AAZStrArg(
            options=["--vis-name", "--sap-virtual-instance-name"],
            help="The name of the Virtual Instances for SAP solutions resource",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z][a-zA-Z0-9]{2}$",
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.SAPDatabaseInstancesGet(ctx=self.ctx)()
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

    class SAPDatabaseInstancesGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Workloads/sapVirtualInstances/{sapVirtualInstanceName}/databaseInstances/{databaseInstanceName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "databaseInstanceName", self.ctx.args.database_instance_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "sapVirtualInstanceName", self.ctx.args.sap_virtual_instance_name,
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
                    "api-version", "2023-10-01-preview",
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
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.database_sid = AAZStrType(
                serialized_name="databaseSid",
                flags={"read_only": True},
            )
            properties.database_type = AAZStrType(
                serialized_name="databaseType",
                flags={"read_only": True},
            )
            properties.errors = AAZObjectType(
                flags={"read_only": True},
            )
            properties.ip_address = AAZStrType(
                serialized_name="ipAddress",
                flags={"read_only": True},
            )
            properties.load_balancer_details = AAZObjectType(
                serialized_name="loadBalancerDetails",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.status = AAZStrType(
                flags={"read_only": True},
            )
            properties.subnet = AAZStrType(
                flags={"read_only": True},
            )
            properties.vm_details = AAZListType(
                serialized_name="vmDetails",
                flags={"read_only": True},
            )

            errors = cls._schema_on_200.properties.errors
            errors.properties = AAZObjectType()
            _ShowHelper._build_schema_error_definition_read(errors.properties)

            load_balancer_details = cls._schema_on_200.properties.load_balancer_details
            load_balancer_details.id = AAZStrType(
                flags={"read_only": True},
            )

            vm_details = cls._schema_on_200.properties.vm_details
            vm_details.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.vm_details.Element
            _element.status = AAZStrType(
                flags={"read_only": True},
            )
            _element.storage_details = AAZListType(
                serialized_name="storageDetails",
                flags={"read_only": True},
            )
            _element.virtual_machine_id = AAZStrType(
                serialized_name="virtualMachineId",
                flags={"read_only": True},
            )

            storage_details = cls._schema_on_200.properties.vm_details.Element.storage_details
            storage_details.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.vm_details.Element.storage_details.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_error_definition_read = None

    @classmethod
    def _build_schema_error_definition_read(cls, _schema):
        if cls._schema_error_definition_read is not None:
            _schema.code = cls._schema_error_definition_read.code
            _schema.details = cls._schema_error_definition_read.details
            _schema.message = cls._schema_error_definition_read.message
            return

        cls._schema_error_definition_read = _schema_error_definition_read = AAZObjectType()

        error_definition_read = _schema_error_definition_read
        error_definition_read.code = AAZStrType(
            flags={"read_only": True},
        )
        error_definition_read.details = AAZListType(
            flags={"read_only": True},
        )
        error_definition_read.message = AAZStrType(
            flags={"read_only": True},
        )

        details = _schema_error_definition_read.details
        details.Element = AAZObjectType()
        cls._build_schema_error_definition_read(details.Element)

        _schema.code = cls._schema_error_definition_read.code
        _schema.details = cls._schema_error_definition_read.details
        _schema.message = cls._schema_error_definition_read.message


__all__ = ["Show"]
