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
    "networkfabric nni list",
)
class List(AAZCommand):
    """List all Network To Network Interconnects in the provided resource group

    :example: List the Network To Network Interconnects for Resource Group
        az networkfabric nni list --resource-group "example-rg" --fabric "example-fabric"
    """

    _aaz_info = {
        "version": "2024-02-15-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.managednetworkfabric/networkfabrics/{}/networktonetworkinterconnects", "2024-02-15-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.fabric_name = AAZStrArg(
            options=["--fabric", "--fabric-name"],
            help="Name of the Network Fabric.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.NetworkToNetworkInterconnectsListByNetworkFabric(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class NetworkToNetworkInterconnectsListByNetworkFabric(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics/{networkFabricName}/networkToNetworkInterconnects",
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
                    "networkFabricName", self.ctx.args.fabric_name,
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
                    "api-version", "2024-02-15-preview",
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
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.administrative_state = AAZStrType(
                serialized_name="administrativeState",
                flags={"read_only": True},
            )
            properties.configuration_state = AAZStrType(
                serialized_name="configurationState",
                flags={"read_only": True},
            )
            properties.egress_acl_id = AAZStrType(
                serialized_name="egressAclId",
                nullable=True,
            )
            properties.export_route_policy = AAZObjectType(
                serialized_name="exportRoutePolicy",
            )
            properties.import_route_policy = AAZObjectType(
                serialized_name="importRoutePolicy",
            )
            properties.ingress_acl_id = AAZStrType(
                serialized_name="ingressAclId",
                nullable=True,
            )
            properties.is_management_type = AAZStrType(
                serialized_name="isManagementType",
            )
            properties.layer2_configuration = AAZObjectType(
                serialized_name="layer2Configuration",
            )
            properties.nni_type = AAZStrType(
                serialized_name="nniType",
            )
            properties.npb_static_route_configuration = AAZObjectType(
                serialized_name="npbStaticRouteConfiguration",
            )
            properties.option_b_layer3_configuration = AAZObjectType(
                serialized_name="optionBLayer3Configuration",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.use_option_b = AAZStrType(
                serialized_name="useOptionB",
                flags={"required": True},
            )

            export_route_policy = cls._schema_on_200.value.Element.properties.export_route_policy
            export_route_policy.export_ipv4_route_policy_id = AAZStrType(
                serialized_name="exportIpv4RoutePolicyId",
                nullable=True,
            )
            export_route_policy.export_ipv6_route_policy_id = AAZStrType(
                serialized_name="exportIpv6RoutePolicyId",
                nullable=True,
            )

            import_route_policy = cls._schema_on_200.value.Element.properties.import_route_policy
            import_route_policy.import_ipv4_route_policy_id = AAZStrType(
                serialized_name="importIpv4RoutePolicyId",
                nullable=True,
            )
            import_route_policy.import_ipv6_route_policy_id = AAZStrType(
                serialized_name="importIpv6RoutePolicyId",
                nullable=True,
            )

            layer2_configuration = cls._schema_on_200.value.Element.properties.layer2_configuration
            layer2_configuration.interfaces = AAZListType()
            layer2_configuration.mtu = AAZIntType()

            interfaces = cls._schema_on_200.value.Element.properties.layer2_configuration.interfaces
            interfaces.Element = AAZStrType()

            npb_static_route_configuration = cls._schema_on_200.value.Element.properties.npb_static_route_configuration
            npb_static_route_configuration.bfd_configuration = AAZObjectType(
                serialized_name="bfdConfiguration",
            )
            npb_static_route_configuration.ipv4_routes = AAZListType(
                serialized_name="ipv4Routes",
            )
            npb_static_route_configuration.ipv6_routes = AAZListType(
                serialized_name="ipv6Routes",
            )

            bfd_configuration = cls._schema_on_200.value.Element.properties.npb_static_route_configuration.bfd_configuration
            bfd_configuration.administrative_state = AAZStrType(
                serialized_name="administrativeState",
                flags={"read_only": True},
            )
            bfd_configuration.interval_in_milli_seconds = AAZIntType(
                serialized_name="intervalInMilliSeconds",
            )
            bfd_configuration.multiplier = AAZIntType()

            ipv4_routes = cls._schema_on_200.value.Element.properties.npb_static_route_configuration.ipv4_routes
            ipv4_routes.Element = AAZObjectType()
            _ListHelper._build_schema_static_route_properties_read(ipv4_routes.Element)

            ipv6_routes = cls._schema_on_200.value.Element.properties.npb_static_route_configuration.ipv6_routes
            ipv6_routes.Element = AAZObjectType()
            _ListHelper._build_schema_static_route_properties_read(ipv6_routes.Element)

            option_b_layer3_configuration = cls._schema_on_200.value.Element.properties.option_b_layer3_configuration
            option_b_layer3_configuration.fabric_asn = AAZIntType(
                serialized_name="fabricASN",
                flags={"read_only": True},
            )
            option_b_layer3_configuration.peer_asn = AAZIntType(
                serialized_name="peerASN",
                flags={"required": True},
            )
            option_b_layer3_configuration.primary_ipv4_prefix = AAZStrType(
                serialized_name="primaryIpv4Prefix",
            )
            option_b_layer3_configuration.primary_ipv6_prefix = AAZStrType(
                serialized_name="primaryIpv6Prefix",
                nullable=True,
            )
            option_b_layer3_configuration.secondary_ipv4_prefix = AAZStrType(
                serialized_name="secondaryIpv4Prefix",
            )
            option_b_layer3_configuration.secondary_ipv6_prefix = AAZStrType(
                serialized_name="secondaryIpv6Prefix",
                nullable=True,
            )
            option_b_layer3_configuration.vlan_id = AAZIntType(
                serialized_name="vlanId",
                flags={"required": True},
            )

            system_data = cls._schema_on_200.value.Element.system_data
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

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""

    _schema_static_route_properties_read = None

    @classmethod
    def _build_schema_static_route_properties_read(cls, _schema):
        if cls._schema_static_route_properties_read is not None:
            _schema.next_hop = cls._schema_static_route_properties_read.next_hop
            _schema.prefix = cls._schema_static_route_properties_read.prefix
            return

        cls._schema_static_route_properties_read = _schema_static_route_properties_read = AAZObjectType()

        static_route_properties_read = _schema_static_route_properties_read
        static_route_properties_read.next_hop = AAZListType(
            serialized_name="nextHop",
            flags={"required": True},
        )
        static_route_properties_read.prefix = AAZStrType(
            flags={"required": True},
        )

        next_hop = _schema_static_route_properties_read.next_hop
        next_hop.Element = AAZStrType()

        _schema.next_hop = cls._schema_static_route_properties_read.next_hop
        _schema.prefix = cls._schema_static_route_properties_read.prefix


__all__ = ["List"]
