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
    "network manager connect-config update",
)
class Update(AAZCommand):
    """Update a new network manager connectivity configuration
    """

    _aaz_info = {
        "version": "2022-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/networkmanagers/{}/connectivityconfigurations/{}", "2022-01-01"],
        ]
    }

    AZ_SUPPORT_GENERIC_UPDATE = True

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
        _args_schema.configuration_name = AAZStrArg(
            options=["--configuration-name"],
            help="The name of the network manager connectivity configuration.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.network_manager_name = AAZStrArg(
            options=["-n", "--name", "--network-manager-name"],
            help="The name of the network manager.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.applies_to_groups = AAZListArg(
            options=["--applies-to-groups"],
            arg_group="Properties",
            help="Groups for configuration",
        )
        _args_schema.connectivity_topology = AAZStrArg(
            options=["--connectivity-topology"],
            arg_group="Properties",
            help="Connectivity topology type.",
            enum={"HubAndSpoke": "HubAndSpoke", "Mesh": "Mesh"},
        )
        _args_schema.delete_existing_peering = AAZStrArg(
            options=["--delete-existing-peering"],
            arg_group="Properties",
            help="Flag if need to remove current existing peerings.",
            nullable=True,
            enum={"False": "False", "True": "True"},
        )
        _args_schema.description = AAZStrArg(
            options=["--description"],
            arg_group="Properties",
            help="A description of the connectivity configuration.",
            nullable=True,
        )
        _args_schema.hubs = AAZListArg(
            options=["--hubs"],
            arg_group="Properties",
            help="List of hubItems",
            nullable=True,
        )
        _args_schema.is_global = AAZStrArg(
            options=["--is-global"],
            arg_group="Properties",
            help="Flag if global mesh is supported.",
            nullable=True,
            enum={"False": "False", "True": "True"},
        )

        applies_to_groups = cls._args_schema.applies_to_groups
        applies_to_groups.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.applies_to_groups.Element
        _element.group_connectivity = AAZStrArg(
            options=["group-connectivity"],
            help="Group connectivity type.",
            enum={"DirectlyConnected": "DirectlyConnected", "None": "None"},
        )
        _element.is_global = AAZStrArg(
            options=["is-global"],
            help="Flag if global is supported.",
            nullable=True,
            enum={"False": "False", "True": "True"},
        )
        _element.network_group_id = AAZStrArg(
            options=["network-group-id"],
            help="Network group Id.",
        )
        _element.use_hub_gateway = AAZStrArg(
            options=["use-hub-gateway"],
            help="Flag if need to use hub gateway.",
            nullable=True,
            enum={"False": "False", "True": "True"},
        )

        hubs = cls._args_schema.hubs
        hubs.Element = AAZObjectArg(
            nullable=True,
        )

        _element = cls._args_schema.hubs.Element
        _element.resource_id = AAZStrArg(
            options=["resource-id"],
            help="Resource Id.",
            nullable=True,
        )
        _element.resource_type = AAZStrArg(
            options=["resource-type"],
            help="Resource Type.",
            nullable=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ConnectivityConfigurationsGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        self.ConnectivityConfigurationsCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class ConnectivityConfigurationsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkManagers/{networkManagerName}/connectivityConfigurations/{configurationName}",
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
                    "configurationName", self.ctx.args.configuration_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "networkManagerName", self.ctx.args.network_manager_name,
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
                    "api-version", "2022-01-01",
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
            _UpdateHelper._build_schema_connectivity_configuration_read(cls._schema_on_200)

            return cls._schema_on_200

    class ConnectivityConfigurationsCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkManagers/{networkManagerName}/connectivityConfigurations/{configurationName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "configurationName", self.ctx.args.configuration_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "networkManagerName", self.ctx.args.network_manager_name,
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
                    "api-version", "2022-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_connectivity_configuration_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("appliesToGroups", AAZListType, ".applies_to_groups", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("connectivityTopology", AAZStrType, ".connectivity_topology", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("deleteExistingPeering", AAZStrType, ".delete_existing_peering")
                properties.set_prop("description", AAZStrType, ".description")
                properties.set_prop("hubs", AAZListType, ".hubs")
                properties.set_prop("isGlobal", AAZStrType, ".is_global")

            applies_to_groups = _builder.get(".properties.appliesToGroups")
            if applies_to_groups is not None:
                applies_to_groups.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.appliesToGroups[]")
            if _elements is not None:
                _elements.set_prop("groupConnectivity", AAZStrType, ".group_connectivity", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("isGlobal", AAZStrType, ".is_global")
                _elements.set_prop("networkGroupId", AAZStrType, ".network_group_id", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("useHubGateway", AAZStrType, ".use_hub_gateway")

            hubs = _builder.get(".properties.hubs")
            if hubs is not None:
                hubs.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.hubs[]")
            if _elements is not None:
                _elements.set_prop("resourceId", AAZStrType, ".resource_id")
                _elements.set_prop("resourceType", AAZStrType, ".resource_type")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_connectivity_configuration_read = None

    @classmethod
    def _build_schema_connectivity_configuration_read(cls, _schema):
        if cls._schema_connectivity_configuration_read is not None:
            _schema.etag = cls._schema_connectivity_configuration_read.etag
            _schema.id = cls._schema_connectivity_configuration_read.id
            _schema.name = cls._schema_connectivity_configuration_read.name
            _schema.properties = cls._schema_connectivity_configuration_read.properties
            _schema.system_data = cls._schema_connectivity_configuration_read.system_data
            _schema.type = cls._schema_connectivity_configuration_read.type
            return

        cls._schema_connectivity_configuration_read = _schema_connectivity_configuration_read = AAZObjectType()

        connectivity_configuration_read = _schema_connectivity_configuration_read
        connectivity_configuration_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        connectivity_configuration_read.id = AAZStrType(
            flags={"read_only": True},
        )
        connectivity_configuration_read.name = AAZStrType(
            flags={"read_only": True},
        )
        connectivity_configuration_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        connectivity_configuration_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        connectivity_configuration_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_connectivity_configuration_read.properties
        properties.applies_to_groups = AAZListType(
            serialized_name="appliesToGroups",
            flags={"required": True},
        )
        properties.connectivity_topology = AAZStrType(
            serialized_name="connectivityTopology",
            flags={"required": True},
        )
        properties.delete_existing_peering = AAZStrType(
            serialized_name="deleteExistingPeering",
        )
        properties.description = AAZStrType()
        properties.hubs = AAZListType()
        properties.is_global = AAZStrType(
            serialized_name="isGlobal",
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )

        applies_to_groups = _schema_connectivity_configuration_read.properties.applies_to_groups
        applies_to_groups.Element = AAZObjectType()

        _element = _schema_connectivity_configuration_read.properties.applies_to_groups.Element
        _element.group_connectivity = AAZStrType(
            serialized_name="groupConnectivity",
            flags={"required": True},
        )
        _element.is_global = AAZStrType(
            serialized_name="isGlobal",
        )
        _element.network_group_id = AAZStrType(
            serialized_name="networkGroupId",
            flags={"required": True},
        )
        _element.use_hub_gateway = AAZStrType(
            serialized_name="useHubGateway",
        )

        hubs = _schema_connectivity_configuration_read.properties.hubs
        hubs.Element = AAZObjectType()

        _element = _schema_connectivity_configuration_read.properties.hubs.Element
        _element.resource_id = AAZStrType(
            serialized_name="resourceId",
        )
        _element.resource_type = AAZStrType(
            serialized_name="resourceType",
        )

        system_data = _schema_connectivity_configuration_read.system_data
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

        _schema.etag = cls._schema_connectivity_configuration_read.etag
        _schema.id = cls._schema_connectivity_configuration_read.id
        _schema.name = cls._schema_connectivity_configuration_read.name
        _schema.properties = cls._schema_connectivity_configuration_read.properties
        _schema.system_data = cls._schema_connectivity_configuration_read.system_data
        _schema.type = cls._schema_connectivity_configuration_read.type


__all__ = ["Update"]
