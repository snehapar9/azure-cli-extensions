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
    "blueprint artifact list",
    is_preview=True,
)
class List(AAZCommand):
    """List artifacts for a given blueprint definition.

    :example: List artifcats for a management group blueprint
        az blueprint artifact list --management-group MyManagementGroup --blueprint-name MyBlueprint

    :example: List artifcats for a subscription blueprint
        az blueprint artifact list --subscription MySubscription --blueprint-name MyBlueprint
    """

    _aaz_info = {
        "version": "2018-11-01-preview",
        "resources": [
            ["mgmt-plane", "/{resourcescope}/providers/microsoft.blueprint/blueprints/{}/artifacts", "2018-11-01-preview"],
        ]
    }

    AZ_SUPPORT_PAGINATION = True

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
        _args_schema.blueprint_name = AAZStrArg(
            options=["--blueprint-name"],
            help="Name of the blueprint definition.",
            required=True,
        )
        _args_schema.resource_scope = AAZStrArg(
            options=["--resource-scope"],
            help="The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}').",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.ArtifactsList(ctx=self.ctx)()
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

    class ArtifactsList(AAZHttpOperation):
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
                "/{resourceScope}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/artifacts",
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
                    "blueprintName", self.ctx.args.blueprint_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceScope", self.ctx.args.resource_scope,
                    skip_quote=True,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2018-11-01-preview",
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
                flags={"read_only": True},
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.kind = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            disc_policy_assignment = cls._schema_on_200.value.Element.discriminate_by("kind", "policyAssignment")
            disc_policy_assignment.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )

            properties = cls._schema_on_200.value.Element.discriminate_by("kind", "policyAssignment").properties
            properties.depends_on = AAZListType(
                serialized_name="dependsOn",
            )
            properties.description = AAZStrType()
            properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            properties.parameters = AAZDictType(
                flags={"required": True},
            )
            properties.policy_definition_id = AAZStrType(
                serialized_name="policyDefinitionId",
                flags={"required": True},
            )
            properties.resource_group = AAZStrType(
                serialized_name="resourceGroup",
            )

            depends_on = cls._schema_on_200.value.Element.discriminate_by("kind", "policyAssignment").properties.depends_on
            depends_on.Element = AAZStrType()

            parameters = cls._schema_on_200.value.Element.discriminate_by("kind", "policyAssignment").properties.parameters
            parameters.Element = AAZObjectType()
            _ListHelper._build_schema_parameter_value_read(parameters.Element)

            disc_role_assignment = cls._schema_on_200.value.Element.discriminate_by("kind", "roleAssignment")
            disc_role_assignment.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )

            properties = cls._schema_on_200.value.Element.discriminate_by("kind", "roleAssignment").properties
            properties.depends_on = AAZListType(
                serialized_name="dependsOn",
            )
            properties.description = AAZStrType()
            properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            properties.resource_group = AAZStrType(
                serialized_name="resourceGroup",
            )
            properties.role_definition_id = AAZStrType(
                serialized_name="roleDefinitionId",
                flags={"required": True},
            )

            depends_on = cls._schema_on_200.value.Element.discriminate_by("kind", "roleAssignment").properties.depends_on
            depends_on.Element = AAZStrType()

            disc_template = cls._schema_on_200.value.Element.discriminate_by("kind", "template")
            disc_template.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )

            properties = cls._schema_on_200.value.Element.discriminate_by("kind", "template").properties
            properties.depends_on = AAZListType(
                serialized_name="dependsOn",
            )
            properties.description = AAZStrType()
            properties.display_name = AAZStrType(
                serialized_name="displayName",
            )
            properties.parameters = AAZDictType(
                flags={"required": True},
            )
            properties.resource_group = AAZStrType(
                serialized_name="resourceGroup",
            )

            depends_on = cls._schema_on_200.value.Element.discriminate_by("kind", "template").properties.depends_on
            depends_on.Element = AAZStrType()

            parameters = cls._schema_on_200.value.Element.discriminate_by("kind", "template").properties.parameters
            parameters.Element = AAZObjectType()
            _ListHelper._build_schema_parameter_value_read(parameters.Element)

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""

    _schema_parameter_value_read = None

    @classmethod
    def _build_schema_parameter_value_read(cls, _schema):
        if cls._schema_parameter_value_read is not None:
            _schema.reference = cls._schema_parameter_value_read.reference
            return

        cls._schema_parameter_value_read = _schema_parameter_value_read = AAZObjectType()

        parameter_value_read = _schema_parameter_value_read
        parameter_value_read.reference = AAZObjectType()

        reference = _schema_parameter_value_read.reference
        reference.key_vault = AAZObjectType(
            serialized_name="keyVault",
            flags={"required": True},
        )
        reference.secret_name = AAZStrType(
            serialized_name="secretName",
            flags={"required": True},
        )
        reference.secret_version = AAZStrType(
            serialized_name="secretVersion",
        )

        key_vault = _schema_parameter_value_read.reference.key_vault
        key_vault.id = AAZStrType(
            flags={"required": True},
        )

        _schema.reference = cls._schema_parameter_value_read.reference


__all__ = ["List"]
