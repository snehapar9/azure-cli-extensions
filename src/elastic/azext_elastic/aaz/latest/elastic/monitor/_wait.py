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
    "elastic monitor wait",
)
class Wait(AAZWaitCommand):
    """Place the CLI in a waiting state until a condition is met.
    """

    _aaz_info = {
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.elastic/monitors/{}", "2023-02-01-preview"],
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
        _args_schema.monitor_name = AAZStrArg(
            options=["-n", "--name", "--monitor-name"],
            help="Monitor resource name",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.MonitorsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=False)
        return result

    class MonitorsGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Elastic/monitors/{monitorName}",
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
                    "monitorName", self.ctx.args.monitor_name,
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
                    "api-version", "2023-02-01-preview",
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
            _schema_on_200.identity = AAZObjectType()
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType()
            _schema_on_200.sku = AAZObjectType()
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType()

            properties = cls._schema_on_200.properties
            properties.elastic_properties = AAZObjectType(
                serialized_name="elasticProperties",
            )
            properties.generate_api_key = AAZBoolType(
                serialized_name="generateApiKey",
            )
            properties.liftr_resource_category = AAZStrType(
                serialized_name="liftrResourceCategory",
                flags={"read_only": True},
            )
            properties.liftr_resource_preference = AAZIntType(
                serialized_name="liftrResourcePreference",
                flags={"read_only": True},
            )
            properties.monitoring_status = AAZStrType(
                serialized_name="monitoringStatus",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            properties.version = AAZStrType()

            elastic_properties = cls._schema_on_200.properties.elastic_properties
            elastic_properties.elastic_cloud_deployment = AAZObjectType(
                serialized_name="elasticCloudDeployment",
            )
            elastic_properties.elastic_cloud_user = AAZObjectType(
                serialized_name="elasticCloudUser",
            )

            elastic_cloud_deployment = cls._schema_on_200.properties.elastic_properties.elastic_cloud_deployment
            elastic_cloud_deployment.azure_subscription_id = AAZStrType(
                serialized_name="azureSubscriptionId",
                flags={"read_only": True},
            )
            elastic_cloud_deployment.deployment_id = AAZStrType(
                serialized_name="deploymentId",
                flags={"read_only": True},
            )
            elastic_cloud_deployment.elasticsearch_region = AAZStrType(
                serialized_name="elasticsearchRegion",
                flags={"read_only": True},
            )
            elastic_cloud_deployment.elasticsearch_service_url = AAZStrType(
                serialized_name="elasticsearchServiceUrl",
                flags={"read_only": True},
            )
            elastic_cloud_deployment.kibana_service_url = AAZStrType(
                serialized_name="kibanaServiceUrl",
                flags={"read_only": True},
            )
            elastic_cloud_deployment.kibana_sso_url = AAZStrType(
                serialized_name="kibanaSsoUrl",
                flags={"read_only": True},
            )
            elastic_cloud_deployment.name = AAZStrType(
                flags={"read_only": True},
            )

            elastic_cloud_user = cls._schema_on_200.properties.elastic_properties.elastic_cloud_user
            elastic_cloud_user.elastic_cloud_sso_default_url = AAZStrType(
                serialized_name="elasticCloudSsoDefaultUrl",
                flags={"read_only": True},
            )
            elastic_cloud_user.email_address = AAZStrType(
                serialized_name="emailAddress",
                flags={"read_only": True},
            )
            elastic_cloud_user.id = AAZStrType(
                flags={"read_only": True},
            )

            sku = cls._schema_on_200.sku
            sku.name = AAZStrType(
                flags={"required": True},
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


class _WaitHelper:
    """Helper class for Wait"""


__all__ = ["Wait"]
