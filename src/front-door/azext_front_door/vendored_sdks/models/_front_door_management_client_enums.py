# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines the action to take on rule match."""

    ALLOW = "Allow"
    BLOCK = "Block"
    LOG = "Log"
    REDIRECT = "Redirect"
    ANOMALY_SCORING = "AnomalyScoring"
    JS_CHALLENGE = "JSChallenge"


class AggregationInterval(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The aggregation interval of the Timeseries."""

    HOURLY = "Hourly"
    DAILY = "Daily"


class Availability(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether the name is available."""

    AVAILABLE = "Available"
    UNAVAILABLE = "Unavailable"


class BackendEnabledState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether to enable use of this backend. Permitted values are 'Enabled' or 'Disabled'."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class CustomHttpsProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning status of Custom Https of the frontendEndpoint."""

    ENABLING = "Enabling"
    ENABLED = "Enabled"
    DISABLING = "Disabling"
    DISABLED = "Disabled"
    FAILED = "Failed"


class CustomHttpsProvisioningSubstate(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning substate shows the progress of custom HTTPS enabling/disabling process step by
    step.
    """

    SUBMITTING_DOMAIN_CONTROL_VALIDATION_REQUEST = "SubmittingDomainControlValidationRequest"
    PENDING_DOMAIN_CONTROL_VALIDATION_R_EQUEST_APPROVAL = "PendingDomainControlValidationREquestApproval"
    DOMAIN_CONTROL_VALIDATION_REQUEST_APPROVED = "DomainControlValidationRequestApproved"
    DOMAIN_CONTROL_VALIDATION_REQUEST_REJECTED = "DomainControlValidationRequestRejected"
    DOMAIN_CONTROL_VALIDATION_REQUEST_TIMED_OUT = "DomainControlValidationRequestTimedOut"
    ISSUING_CERTIFICATE = "IssuingCertificate"
    DEPLOYING_CERTIFICATE = "DeployingCertificate"
    CERTIFICATE_DEPLOYED = "CertificateDeployed"
    DELETING_CERTIFICATE = "DeletingCertificate"
    CERTIFICATE_DELETED = "CertificateDeleted"


class CustomRuleEnabledState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes if the custom rule is in enabled or disabled state. Defaults to Enabled if not
    specified.
    """

    DISABLED = "Disabled"
    ENABLED = "Enabled"


class DynamicCompressionEnabled(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether to use dynamic compression for cached content."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class EndpointType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of endpoint."""

    AFD = "AFD"
    AZURE_REGION = "AzureRegion"
    CDN = "CDN"
    ATM = "ATM"


class EnforceCertificateNameCheckEnabledState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether to enforce certificate name check on HTTPS requests to all backend pools. No effect on
    non-HTTPS requests.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class FrontDoorCertificateSource(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines the source of the SSL certificate."""

    AZURE_KEY_VAULT = "AzureKeyVault"
    FRONT_DOOR = "FrontDoor"


class FrontDoorCertificateType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines the type of the certificate used for secure connections to a frontendEndpoint."""

    DEDICATED = "Dedicated"


class FrontDoorEnabledState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Operational status of the Front Door load balancer. Permitted values are 'Enabled' or
    'Disabled'.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class FrontDoorForwardingProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Protocol this rule will use when forwarding traffic to backends."""

    HTTP_ONLY = "HttpOnly"
    HTTPS_ONLY = "HttpsOnly"
    MATCH_REQUEST = "MatchRequest"


class FrontDoorHealthProbeMethod(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Configures which HTTP method to use to probe the backends defined under backendPools."""

    GET = "GET"
    HEAD = "HEAD"


class FrontDoorProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Accepted protocol schemes."""

    HTTP = "Http"
    HTTPS = "Https"


class FrontDoorQuery(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Treatment of URL query terms when forming the cache key."""

    STRIP_NONE = "StripNone"
    STRIP_ALL = "StripAll"
    STRIP_ONLY = "StripOnly"
    STRIP_ALL_EXCEPT = "StripAllExcept"


class FrontDoorRedirectProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The protocol of the destination to where the traffic is redirected."""

    HTTP_ONLY = "HttpOnly"
    HTTPS_ONLY = "HttpsOnly"
    MATCH_REQUEST = "MatchRequest"


class FrontDoorRedirectType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The redirect type the rule will use when redirecting traffic."""

    MOVED = "Moved"
    FOUND = "Found"
    TEMPORARY_REDIRECT = "TemporaryRedirect"
    PERMANENT_REDIRECT = "PermanentRedirect"


class FrontDoorResourceState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Resource status of the Front Door or Front Door SubResource."""

    CREATING = "Creating"
    ENABLING = "Enabling"
    ENABLED = "Enabled"
    DISABLING = "Disabling"
    DISABLED = "Disabled"
    DELETING = "Deleting"
    MIGRATING = "Migrating"
    MIGRATED = "Migrated"


class FrontDoorTlsProtocolType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines the TLS extension protocol that is used for secure delivery."""

    SERVER_NAME_INDICATION = "ServerNameIndication"


class HeaderActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Which type of manipulation to apply to the header."""

    APPEND = "Append"
    DELETE = "Delete"
    OVERWRITE = "Overwrite"


class HealthProbeEnabled(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether to enable health probes to be made against backends defined under backendPools. Health
    probes can only be disabled if there is a single enabled backend in single enabled backend
    pool.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class LatencyScorecardAggregationInterval(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """LatencyScorecardAggregationInterval."""

    DAILY = "Daily"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"


class ManagedRuleEnabledState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes if the managed rule is in enabled or disabled state."""

    DISABLED = "Disabled"
    ENABLED = "Enabled"


class ManagedRuleExclusionMatchVariable(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The variable type to be excluded."""

    REQUEST_HEADER_NAMES = "RequestHeaderNames"
    REQUEST_COOKIE_NAMES = "RequestCookieNames"
    QUERY_STRING_ARG_NAMES = "QueryStringArgNames"
    REQUEST_BODY_POST_ARG_NAMES = "RequestBodyPostArgNames"
    REQUEST_BODY_JSON_ARG_NAMES = "RequestBodyJsonArgNames"


class ManagedRuleExclusionSelectorMatchOperator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Comparison operator to apply to the selector when specifying which elements in the collection
    this exclusion applies to.
    """

    EQUALS = "Equals"
    CONTAINS = "Contains"
    STARTS_WITH = "StartsWith"
    ENDS_WITH = "EndsWith"
    EQUALS_ANY = "EqualsAny"


class ManagedRuleSetActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines the action to take when a managed rule set score threshold is met."""

    BLOCK = "Block"
    LOG = "Log"
    REDIRECT = "Redirect"


class MatchProcessingBehavior(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """If this rule is a match should the rules engine continue running the remaining rules or stop.
    If not present, defaults to Continue.
    """

    CONTINUE_ENUM = "Continue"
    STOP = "Stop"


class MatchVariable(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Request variable to compare with."""

    REMOTE_ADDR = "RemoteAddr"
    REQUEST_METHOD = "RequestMethod"
    QUERY_STRING = "QueryString"
    POST_ARGS = "PostArgs"
    REQUEST_URI = "RequestUri"
    REQUEST_HEADER = "RequestHeader"
    REQUEST_BODY = "RequestBody"
    COOKIES = "Cookies"
    SOCKET_ADDR = "SocketAddr"


class MinimumTLSVersion(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The minimum TLS version required from the clients to establish an SSL handshake with Front
    Door.
    """

    ONE0 = "1.0"
    ONE2 = "1.2"


class NetworkExperimentResourceState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines the server side resource status."""

    CREATING = "Creating"
    ENABLING = "Enabling"
    ENABLED = "Enabled"
    DISABLING = "Disabling"
    DISABLED = "Disabled"
    DELETING = "Deleting"


class NetworkOperationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of the Azure async operation."""

    IN_PROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"


class Operator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Comparison type to use for matching with the variable value."""

    ANY = "Any"
    IP_MATCH = "IPMatch"
    GEO_MATCH = "GeoMatch"
    EQUAL = "Equal"
    CONTAINS = "Contains"
    LESS_THAN = "LessThan"
    GREATER_THAN = "GreaterThan"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    BEGINS_WITH = "BeginsWith"
    ENDS_WITH = "EndsWith"
    REG_EX = "RegEx"


class PolicyEnabledState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes if the policy is in enabled or disabled state. Defaults to Enabled if not specified."""

    DISABLED = "Disabled"
    ENABLED = "Enabled"


class PolicyMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes if it is in detection mode or prevention mode at policy level."""

    PREVENTION = "Prevention"
    DETECTION = "Detection"


class PolicyRequestBodyCheck(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes if policy managed rules will inspect the request body content."""

    DISABLED = "Disabled"
    ENABLED = "Enabled"


class PolicyResourceState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Resource status of the policy."""

    CREATING = "Creating"
    ENABLING = "Enabling"
    ENABLED = "Enabled"
    DISABLING = "Disabling"
    DISABLED = "Disabled"
    DELETING = "Deleting"


class PrivateEndpointStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The Approval status for the connection to the Private Link."""

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"
    TIMEOUT = "Timeout"


class ResourceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of Front Door resource used in CheckNameAvailability."""

    MICROSOFT_NETWORK_FRONT_DOORS = "Microsoft.Network/frontDoors"
    MICROSOFT_NETWORK_FRONT_DOORS_FRONTEND_ENDPOINTS = "Microsoft.Network/frontDoors/frontendEndpoints"


class RoutingRuleEnabledState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether to enable use of this rule. Permitted values are 'Enabled' or 'Disabled'."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class RulesEngineMatchVariable(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Match Variable."""

    IS_MOBILE = "IsMobile"
    REMOTE_ADDR = "RemoteAddr"
    REQUEST_METHOD = "RequestMethod"
    QUERY_STRING = "QueryString"
    POST_ARGS = "PostArgs"
    REQUEST_URI = "RequestUri"
    REQUEST_PATH = "RequestPath"
    REQUEST_FILENAME = "RequestFilename"
    REQUEST_FILENAME_EXTENSION = "RequestFilenameExtension"
    REQUEST_HEADER = "RequestHeader"
    REQUEST_BODY = "RequestBody"
    REQUEST_SCHEME = "RequestScheme"


class RulesEngineOperator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes operator to apply to the match condition."""

    ANY = "Any"
    IP_MATCH = "IPMatch"
    GEO_MATCH = "GeoMatch"
    EQUAL = "Equal"
    CONTAINS = "Contains"
    LESS_THAN = "LessThan"
    GREATER_THAN = "GreaterThan"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    BEGINS_WITH = "BeginsWith"
    ENDS_WITH = "EndsWith"


class RuleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes type of rule."""

    MATCH_RULE = "MatchRule"
    RATE_LIMIT_RULE = "RateLimitRule"


class ScrubbingRuleEntryMatchOperator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """When matchVariable is a collection, operate on the selector to specify which elements in the
    collection this rule applies to.
    """

    EQUALS_ANY = "EqualsAny"
    EQUALS = "Equals"


class ScrubbingRuleEntryMatchVariable(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The variable to be scrubbed from the logs."""

    REQUEST_IP_ADDRESS = "RequestIPAddress"
    REQUEST_URI = "RequestUri"
    QUERY_STRING_ARG_NAMES = "QueryStringArgNames"
    REQUEST_HEADER_NAMES = "RequestHeaderNames"
    REQUEST_COOKIE_NAMES = "RequestCookieNames"
    REQUEST_BODY_POST_ARG_NAMES = "RequestBodyPostArgNames"
    REQUEST_BODY_JSON_ARG_NAMES = "RequestBodyJsonArgNames"


class ScrubbingRuleEntryState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines the state of a log scrubbing rule. Default value is enabled."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class SessionAffinityEnabledState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether to allow session affinity on this host. Valid options are 'Enabled' or 'Disabled'."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class SkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name of the pricing tier."""

    CLASSIC_AZURE_FRONT_DOOR = "Classic_AzureFrontDoor"
    STANDARD_AZURE_FRONT_DOOR = "Standard_AzureFrontDoor"
    PREMIUM_AZURE_FRONT_DOOR = "Premium_AzureFrontDoor"


class State(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The state of the Experiment."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class TimeseriesAggregationInterval(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """TimeseriesAggregationInterval."""

    HOURLY = "Hourly"
    DAILY = "Daily"


class TimeseriesType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of Timeseries."""

    MEASUREMENT_COUNTS = "MeasurementCounts"
    LATENCY_P50 = "LatencyP50"
    LATENCY_P75 = "LatencyP75"
    LATENCY_P95 = "LatencyP95"


class Transform(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes what transforms are applied before matching."""

    LOWERCASE = "Lowercase"
    UPPERCASE = "Uppercase"
    TRIM = "Trim"
    URL_DECODE = "UrlDecode"
    URL_ENCODE = "UrlEncode"
    REMOVE_NULLS = "RemoveNulls"


class TransformType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes what transforms applied before matching."""

    LOWERCASE = "Lowercase"
    UPPERCASE = "Uppercase"
    TRIM = "Trim"
    URL_DECODE = "UrlDecode"
    URL_ENCODE = "UrlEncode"
    REMOVE_NULLS = "RemoveNulls"


class VariableName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes the supported variable for group by."""

    SOCKET_ADDR = "SocketAddr"
    GEO_LOCATION = "GeoLocation"
    NONE = "None"


class WebApplicationFirewallScrubbingState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the log scrubbing config. Default value is Enabled."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"
