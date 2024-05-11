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
    "support no-subscription tickets list",
)
class List(AAZCommand):
    """List all the support tickets. <br/><br/>You can also filter the support tickets by <i>Status</i>, <i>CreatedDate</i>, <i>ServiceId</i>, and <i>ProblemClassificationId</i> using the $filter parameter. Output will be a paged result with <i>nextLink</i>, using which you can retrieve the next set of support tickets. <br/><br/>Support ticket data is available for 18 months after ticket creation. If a ticket was created more than 18 months ago, a request for data might cause an error. Default is CreatedDate >= one week.

    :example: List support tickets for a no subscription
        az support no-subscription tickets list

    :example: List support tickets in open state for a no subscription
        az support no-subscription tickets list --filter "Status eq 'Open'"

    :example: List support tickets in updating state for a no subscription
        az support no-subscription tickets list --filter "Status eq 'Updating'"

    :example: List support tickets with a certain problem classification id for a no subscription
        az support no-subscription tickets list --filter "ProblemClassificationId eq 'problem_classification_guid'"

    :example: List support tickets created on or after a certain date and in open state for a no subscription
        az support no-subscription tickets list --filter "CreatedDate ge 2024-01-01T22:08:51Z and Status eq 'Open'"

    :example: List support tickets with a certain service id for a no subscription
        az support no-subscription tickets list --filter "ServiceId eq 'service_guid'"
    """

    _aaz_info = {
        "version": "2024-04-01",
        "resources": [
            ["mgmt-plane", "/providers/microsoft.support/supporttickets", "2024-04-01"],
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
        _args_schema.filter = AAZStrArg(
            options=["--filter"],
            help="The filter to apply on the operation. We support 'OData v4.0' filter semantics. Status, ServiceId, and ProblemClassificationId filters can only be used with Equals ('eq') operator. For CreatedDate filter, the supported operators are Greater Than ('gt') and Greater Than or Equals ('ge'). When using both filters, combine them using the logical 'and'.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.SupportTicketsNoSubscriptionList(ctx=self.ctx)()
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

    class SupportTicketsNoSubscriptionList(AAZHttpOperation):
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
                "/providers/Microsoft.Support/supportTickets",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "$filter", self.ctx.args.filter,
                ),
                **self.serialize_query_param(
                    "api-version", "2024-04-01",
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
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.advanced_diagnostic_consent = AAZStrType(
                serialized_name="advancedDiagnosticConsent",
                flags={"required": True},
            )
            properties.contact_details = AAZObjectType(
                serialized_name="contactDetails",
                flags={"required": True},
            )
            properties.created_date = AAZStrType(
                serialized_name="createdDate",
                flags={"read_only": True},
            )
            properties.description = AAZStrType(
                flags={"required": True},
            )
            properties.enrollment_id = AAZStrType(
                serialized_name="enrollmentId",
            )
            properties.file_workspace_name = AAZStrType(
                serialized_name="fileWorkspaceName",
            )
            properties.is_temporary_ticket = AAZStrType(
                serialized_name="isTemporaryTicket",
                flags={"read_only": True},
            )
            properties.modified_date = AAZStrType(
                serialized_name="modifiedDate",
                flags={"read_only": True},
            )
            properties.problem_classification_display_name = AAZStrType(
                serialized_name="problemClassificationDisplayName",
                flags={"read_only": True},
            )
            properties.problem_classification_id = AAZStrType(
                serialized_name="problemClassificationId",
                flags={"required": True},
            )
            properties.problem_scoping_questions = AAZStrType(
                serialized_name="problemScopingQuestions",
            )
            properties.problem_start_time = AAZStrType(
                serialized_name="problemStartTime",
            )
            properties.quota_ticket_details = AAZObjectType(
                serialized_name="quotaTicketDetails",
            )
            properties.require24_x7_response = AAZBoolType(
                serialized_name="require24X7Response",
            )
            properties.secondary_consent = AAZListType(
                serialized_name="secondaryConsent",
            )
            properties.service_display_name = AAZStrType(
                serialized_name="serviceDisplayName",
                flags={"read_only": True},
            )
            properties.service_id = AAZStrType(
                serialized_name="serviceId",
                flags={"required": True},
            )
            properties.service_level_agreement = AAZObjectType(
                serialized_name="serviceLevelAgreement",
            )
            properties.severity = AAZStrType(
                flags={"required": True},
            )
            properties.status = AAZStrType(
                flags={"read_only": True},
            )
            properties.support_engineer = AAZObjectType(
                serialized_name="supportEngineer",
            )
            properties.support_plan_display_name = AAZStrType(
                serialized_name="supportPlanDisplayName",
                flags={"read_only": True},
            )
            properties.support_plan_id = AAZStrType(
                serialized_name="supportPlanId",
            )
            properties.support_plan_type = AAZStrType(
                serialized_name="supportPlanType",
                flags={"read_only": True},
            )
            properties.support_ticket_id = AAZStrType(
                serialized_name="supportTicketId",
            )
            properties.technical_ticket_details = AAZObjectType(
                serialized_name="technicalTicketDetails",
            )
            properties.title = AAZStrType(
                flags={"required": True},
            )

            contact_details = cls._schema_on_200.value.Element.properties.contact_details
            contact_details.additional_email_addresses = AAZListType(
                serialized_name="additionalEmailAddresses",
            )
            contact_details.country = AAZStrType(
                flags={"required": True},
            )
            contact_details.first_name = AAZStrType(
                serialized_name="firstName",
                flags={"required": True},
            )
            contact_details.last_name = AAZStrType(
                serialized_name="lastName",
                flags={"required": True},
            )
            contact_details.phone_number = AAZStrType(
                serialized_name="phoneNumber",
            )
            contact_details.preferred_contact_method = AAZStrType(
                serialized_name="preferredContactMethod",
                flags={"required": True},
            )
            contact_details.preferred_support_language = AAZStrType(
                serialized_name="preferredSupportLanguage",
                flags={"required": True},
            )
            contact_details.preferred_time_zone = AAZStrType(
                serialized_name="preferredTimeZone",
                flags={"required": True},
            )
            contact_details.primary_email_address = AAZStrType(
                serialized_name="primaryEmailAddress",
                flags={"required": True},
            )

            additional_email_addresses = cls._schema_on_200.value.Element.properties.contact_details.additional_email_addresses
            additional_email_addresses.Element = AAZStrType()

            quota_ticket_details = cls._schema_on_200.value.Element.properties.quota_ticket_details
            quota_ticket_details.quota_change_request_sub_type = AAZStrType(
                serialized_name="quotaChangeRequestSubType",
            )
            quota_ticket_details.quota_change_request_version = AAZStrType(
                serialized_name="quotaChangeRequestVersion",
            )
            quota_ticket_details.quota_change_requests = AAZListType(
                serialized_name="quotaChangeRequests",
            )

            quota_change_requests = cls._schema_on_200.value.Element.properties.quota_ticket_details.quota_change_requests
            quota_change_requests.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.quota_ticket_details.quota_change_requests.Element
            _element.payload = AAZStrType()
            _element.region = AAZStrType()

            secondary_consent = cls._schema_on_200.value.Element.properties.secondary_consent
            secondary_consent.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.secondary_consent.Element
            _element.type = AAZStrType()
            _element.user_consent = AAZStrType(
                serialized_name="userConsent",
            )

            service_level_agreement = cls._schema_on_200.value.Element.properties.service_level_agreement
            service_level_agreement.expiration_time = AAZStrType(
                serialized_name="expirationTime",
                flags={"read_only": True},
            )
            service_level_agreement.sla_minutes = AAZIntType(
                serialized_name="slaMinutes",
                flags={"read_only": True},
            )
            service_level_agreement.start_time = AAZStrType(
                serialized_name="startTime",
                flags={"read_only": True},
            )

            support_engineer = cls._schema_on_200.value.Element.properties.support_engineer
            support_engineer.email_address = AAZStrType(
                serialized_name="emailAddress",
                flags={"read_only": True},
            )

            technical_ticket_details = cls._schema_on_200.value.Element.properties.technical_ticket_details
            technical_ticket_details.resource_id = AAZStrType(
                serialized_name="resourceId",
            )

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
