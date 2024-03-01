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
    "astronomer organization list",
)
class List(AAZCommand):
    """List OrganizationResource resources by subscription ID

    :example: ist OrganizationResource resources.
        az astronomer organization list -g MyResourceGroup
    """

    _aaz_info = {
        "version": "2023-08-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/astronomer.astro/organizations", "2023-08-01"],
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/astronomer.astro/organizations", "2023-08-01"],
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
        _args_schema.resource_group = AAZResourceGroupNameArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        condition_0 = has_value(self.ctx.args.resource_group) and has_value(self.ctx.subscription_id)
        condition_1 = has_value(self.ctx.subscription_id) and has_value(self.ctx.args.resource_group) is not True
        if condition_0:
            self.OrganizationsListByResourceGroup(ctx=self.ctx)()
        if condition_1:
            self.OrganizationsListBySubscription(ctx=self.ctx)()
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

    class OrganizationsListByResourceGroup(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Astronomer.Astro/organizations",
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
                    "api-version", "2023-08-01",
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
            _schema_on_200.value = AAZListType(
                flags={"required": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.identity = AAZObjectType()
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.value.Element.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType(
                flags={"required": True},
            )
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.value.Element.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.marketplace = AAZObjectType(
                flags={"required": True},
            )
            properties.partner_organization_properties = AAZObjectType(
                serialized_name="partnerOrganizationProperties",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            properties.user = AAZObjectType(
                flags={"required": True},
            )

            marketplace = cls._schema_on_200.value.Element.properties.marketplace
            marketplace.offer_details = AAZObjectType(
                serialized_name="offerDetails",
                flags={"required": True},
            )
            marketplace.subscription_id = AAZStrType(
                serialized_name="subscriptionId",
                flags={"required": True},
            )
            marketplace.subscription_status = AAZStrType(
                serialized_name="subscriptionStatus",
            )

            offer_details = cls._schema_on_200.value.Element.properties.marketplace.offer_details
            offer_details.offer_id = AAZStrType(
                serialized_name="offerId",
                flags={"required": True},
            )
            offer_details.plan_id = AAZStrType(
                serialized_name="planId",
                flags={"required": True},
            )
            offer_details.plan_name = AAZStrType(
                serialized_name="planName",
            )
            offer_details.publisher_id = AAZStrType(
                serialized_name="publisherId",
                flags={"required": True},
            )
            offer_details.term_id = AAZStrType(
                serialized_name="termId",
            )
            offer_details.term_unit = AAZStrType(
                serialized_name="termUnit",
            )

            partner_organization_properties = cls._schema_on_200.value.Element.properties.partner_organization_properties
            partner_organization_properties.organization_id = AAZStrType(
                serialized_name="organizationId",
            )
            partner_organization_properties.organization_name = AAZStrType(
                serialized_name="organizationName",
                flags={"required": True},
            )
            partner_organization_properties.single_sign_on_properties = AAZObjectType(
                serialized_name="singleSignOnProperties",
            )
            partner_organization_properties.workspace_id = AAZStrType(
                serialized_name="workspaceId",
            )
            partner_organization_properties.workspace_name = AAZStrType(
                serialized_name="workspaceName",
            )

            single_sign_on_properties = cls._schema_on_200.value.Element.properties.partner_organization_properties.single_sign_on_properties
            single_sign_on_properties.aad_domains = AAZListType(
                serialized_name="aadDomains",
            )
            single_sign_on_properties.enterprise_app_id = AAZStrType(
                serialized_name="enterpriseAppId",
            )
            single_sign_on_properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            single_sign_on_properties.single_sign_on_state = AAZStrType(
                serialized_name="singleSignOnState",
            )
            single_sign_on_properties.single_sign_on_url = AAZStrType(
                serialized_name="singleSignOnUrl",
            )

            aad_domains = cls._schema_on_200.value.Element.properties.partner_organization_properties.single_sign_on_properties.aad_domains
            aad_domains.Element = AAZStrType()

            user = cls._schema_on_200.value.Element.properties.user
            user.email_address = AAZStrType(
                serialized_name="emailAddress",
                flags={"required": True},
            )
            user.first_name = AAZStrType(
                serialized_name="firstName",
                flags={"required": True},
            )
            user.last_name = AAZStrType(
                serialized_name="lastName",
                flags={"required": True},
            )
            user.phone_number = AAZStrType(
                serialized_name="phoneNumber",
            )
            user.upn = AAZStrType()

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

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200

    class OrganizationsListBySubscription(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/providers/Astronomer.Astro/organizations",
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
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-08-01",
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
            _schema_on_200.value = AAZListType(
                flags={"required": True},
            )

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.identity = AAZObjectType()
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            identity = cls._schema_on_200.value.Element.identity
            identity.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )
            identity.tenant_id = AAZStrType(
                serialized_name="tenantId",
                flags={"read_only": True},
            )
            identity.type = AAZStrType(
                flags={"required": True},
            )
            identity.user_assigned_identities = AAZDictType(
                serialized_name="userAssignedIdentities",
            )

            user_assigned_identities = cls._schema_on_200.value.Element.identity.user_assigned_identities
            user_assigned_identities.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.identity.user_assigned_identities.Element
            _element.client_id = AAZStrType(
                serialized_name="clientId",
                flags={"read_only": True},
            )
            _element.principal_id = AAZStrType(
                serialized_name="principalId",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.marketplace = AAZObjectType(
                flags={"required": True},
            )
            properties.partner_organization_properties = AAZObjectType(
                serialized_name="partnerOrganizationProperties",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            properties.user = AAZObjectType(
                flags={"required": True},
            )

            marketplace = cls._schema_on_200.value.Element.properties.marketplace
            marketplace.offer_details = AAZObjectType(
                serialized_name="offerDetails",
                flags={"required": True},
            )
            marketplace.subscription_id = AAZStrType(
                serialized_name="subscriptionId",
                flags={"required": True},
            )
            marketplace.subscription_status = AAZStrType(
                serialized_name="subscriptionStatus",
            )

            offer_details = cls._schema_on_200.value.Element.properties.marketplace.offer_details
            offer_details.offer_id = AAZStrType(
                serialized_name="offerId",
                flags={"required": True},
            )
            offer_details.plan_id = AAZStrType(
                serialized_name="planId",
                flags={"required": True},
            )
            offer_details.plan_name = AAZStrType(
                serialized_name="planName",
            )
            offer_details.publisher_id = AAZStrType(
                serialized_name="publisherId",
                flags={"required": True},
            )
            offer_details.term_id = AAZStrType(
                serialized_name="termId",
            )
            offer_details.term_unit = AAZStrType(
                serialized_name="termUnit",
            )

            partner_organization_properties = cls._schema_on_200.value.Element.properties.partner_organization_properties
            partner_organization_properties.organization_id = AAZStrType(
                serialized_name="organizationId",
            )
            partner_organization_properties.organization_name = AAZStrType(
                serialized_name="organizationName",
                flags={"required": True},
            )
            partner_organization_properties.single_sign_on_properties = AAZObjectType(
                serialized_name="singleSignOnProperties",
            )
            partner_organization_properties.workspace_id = AAZStrType(
                serialized_name="workspaceId",
            )
            partner_organization_properties.workspace_name = AAZStrType(
                serialized_name="workspaceName",
            )

            single_sign_on_properties = cls._schema_on_200.value.Element.properties.partner_organization_properties.single_sign_on_properties
            single_sign_on_properties.aad_domains = AAZListType(
                serialized_name="aadDomains",
            )
            single_sign_on_properties.enterprise_app_id = AAZStrType(
                serialized_name="enterpriseAppId",
            )
            single_sign_on_properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
            )
            single_sign_on_properties.single_sign_on_state = AAZStrType(
                serialized_name="singleSignOnState",
            )
            single_sign_on_properties.single_sign_on_url = AAZStrType(
                serialized_name="singleSignOnUrl",
            )

            aad_domains = cls._schema_on_200.value.Element.properties.partner_organization_properties.single_sign_on_properties.aad_domains
            aad_domains.Element = AAZStrType()

            user = cls._schema_on_200.value.Element.properties.user
            user.email_address = AAZStrType(
                serialized_name="emailAddress",
                flags={"required": True},
            )
            user.first_name = AAZStrType(
                serialized_name="firstName",
                flags={"required": True},
            )
            user.last_name = AAZStrType(
                serialized_name="lastName",
                flags={"required": True},
            )
            user.phone_number = AAZStrType(
                serialized_name="phoneNumber",
            )
            user.upn = AAZStrType()

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

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
