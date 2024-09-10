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
    "monitor data-collection rule log-analytics add",
)
class Add(AAZCommand):
    """Add Log Analytics destinations of a data collection rule.

    :example: Add Log Analytics destinations of a data collection rule
        az monitor data-collection rule log-analytics add --rule-name myCollectionRule --resource-group myResourceGroup --name workspace2 --resource-id /subscriptions/703362b3-f2784e4b-9179-c76eaf41ffc2/resourceGroups/myResourceGroup/providers/Microsoft.OperationalInsights/workspaces/workspace2
    """

    _aaz_info = {
        "version": "2023-03-11",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.insights/datacollectionrules/{}", "2023-03-11", "properties.destinations.logAnalytics[]"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self.SubresourceSelector(ctx=self.ctx, name="subresource")
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
        _args_schema.data_collection_rule_name = AAZStrArg(
            options=["--rule-name", "--data-collection-rule-name"],
            help="The name of the data collection rule. The name is case insensitive.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="A friendly name for the destination. This name should be unique across all destinations (regardless of type) within the data collection rule.",
            required=True,
        )
        _args_schema.workspace_resource_id = AAZStrArg(
            options=["--resource-id", "--workspace-resource-id"],
            help="The resource ID of the Log Analytics workspace.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.DataCollectionRulesGet(ctx=self.ctx)()
        self.pre_instance_create()
        self.InstanceCreateByJson(ctx=self.ctx)()
        self.post_instance_create(self.ctx.selectors.subresource.required())
        self.DataCollectionRulesCreate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_create(self):
        pass

    @register_callback
    def post_instance_create(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.selectors.subresource.required(), client_flatten=True)
        return result

    class SubresourceSelector(AAZJsonSelector):

        def _get(self):
            result = self.ctx.vars.instance
            result = result.properties.destinations.logAnalytics
            filters = enumerate(result)
            filters = filter(
                lambda e: e[1].name == self.ctx.args.name,
                filters
            )
            idx = next(filters)[0]
            return result[idx]

        def _set(self, value):
            result = self.ctx.vars.instance
            result = result.properties.destinations.logAnalytics
            filters = enumerate(result)
            filters = filter(
                lambda e: e[1].name == self.ctx.args.name,
                filters
            )
            idx = next(filters, [len(result)])[0]
            result[idx] = value
            return

    class DataCollectionRulesGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/dataCollectionRules/{dataCollectionRuleName}",
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
                    "dataCollectionRuleName", self.ctx.args.data_collection_rule_name,
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
                    "api-version", "2023-03-11",
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
            _AddHelper._build_schema_data_collection_rule_resource_read(cls._schema_on_200)

            return cls._schema_on_200

    class DataCollectionRulesCreate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/dataCollectionRules/{dataCollectionRuleName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "dataCollectionRuleName", self.ctx.args.data_collection_rule_name,
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
                    "api-version", "2023-03-11",
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
            _AddHelper._build_schema_data_collection_rule_resource_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceCreateByJson(AAZJsonInstanceCreateOperation):

        def __call__(self, *args, **kwargs):
            self.ctx.selectors.subresource.set(self._create_instance())

        def _create_instance(self):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType
            )
            _builder.set_prop("name", AAZStrType, ".name")
            _builder.set_prop("workspaceResourceId", AAZStrType, ".workspace_resource_id")

            return _instance_value


class _AddHelper:
    """Helper class for Add"""

    _schema_data_collection_rule_resource_read = None

    @classmethod
    def _build_schema_data_collection_rule_resource_read(cls, _schema):
        if cls._schema_data_collection_rule_resource_read is not None:
            _schema.etag = cls._schema_data_collection_rule_resource_read.etag
            _schema.id = cls._schema_data_collection_rule_resource_read.id
            _schema.identity = cls._schema_data_collection_rule_resource_read.identity
            _schema.kind = cls._schema_data_collection_rule_resource_read.kind
            _schema.location = cls._schema_data_collection_rule_resource_read.location
            _schema.name = cls._schema_data_collection_rule_resource_read.name
            _schema.properties = cls._schema_data_collection_rule_resource_read.properties
            _schema.system_data = cls._schema_data_collection_rule_resource_read.system_data
            _schema.tags = cls._schema_data_collection_rule_resource_read.tags
            _schema.type = cls._schema_data_collection_rule_resource_read.type
            return

        cls._schema_data_collection_rule_resource_read = _schema_data_collection_rule_resource_read = AAZObjectType()

        data_collection_rule_resource_read = _schema_data_collection_rule_resource_read
        data_collection_rule_resource_read.etag = AAZStrType(
            flags={"read_only": True},
        )
        data_collection_rule_resource_read.id = AAZStrType(
            flags={"read_only": True},
        )
        data_collection_rule_resource_read.identity = AAZObjectType()
        data_collection_rule_resource_read.kind = AAZStrType()
        data_collection_rule_resource_read.location = AAZStrType(
            flags={"required": True},
        )
        data_collection_rule_resource_read.name = AAZStrType(
            flags={"read_only": True},
        )
        data_collection_rule_resource_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        data_collection_rule_resource_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        data_collection_rule_resource_read.tags = AAZDictType()
        data_collection_rule_resource_read.type = AAZStrType(
            flags={"read_only": True},
        )

        identity = _schema_data_collection_rule_resource_read.identity
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

        user_assigned_identities = _schema_data_collection_rule_resource_read.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectType(
            nullable=True,
        )

        _element = _schema_data_collection_rule_resource_read.identity.user_assigned_identities.Element
        _element.client_id = AAZStrType(
            serialized_name="clientId",
            flags={"read_only": True},
        )
        _element.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )

        properties = _schema_data_collection_rule_resource_read.properties
        properties.agent_settings = AAZObjectType(
            serialized_name="agentSettings",
        )
        properties.data_collection_endpoint_id = AAZStrType(
            serialized_name="dataCollectionEndpointId",
        )
        properties.data_flows = AAZListType(
            serialized_name="dataFlows",
        )
        properties.data_sources = AAZObjectType(
            serialized_name="dataSources",
        )
        properties.description = AAZStrType()
        properties.destinations = AAZObjectType()
        properties.endpoints = AAZObjectType(
            flags={"read_only": True},
        )
        properties.immutable_id = AAZStrType(
            serialized_name="immutableId",
            flags={"read_only": True},
        )
        properties.metadata = AAZObjectType(
            flags={"read_only": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.references = AAZObjectType()
        properties.stream_declarations = AAZDictType(
            serialized_name="streamDeclarations",
        )

        agent_settings = _schema_data_collection_rule_resource_read.properties.agent_settings
        agent_settings.logs = AAZListType()

        logs = _schema_data_collection_rule_resource_read.properties.agent_settings.logs
        logs.Element = AAZObjectType()

        _element = _schema_data_collection_rule_resource_read.properties.agent_settings.logs.Element
        _element.name = AAZStrType()
        _element.value = AAZStrType()

        data_flows = _schema_data_collection_rule_resource_read.properties.data_flows
        data_flows.Element = AAZObjectType()

        _element = _schema_data_collection_rule_resource_read.properties.data_flows.Element
        _element.built_in_transform = AAZStrType(
            serialized_name="builtInTransform",
        )
        _element.capture_overflow = AAZBoolType(
            serialized_name="captureOverflow",
        )
        _element.destinations = AAZListType()
        _element.output_stream = AAZStrType(
            serialized_name="outputStream",
        )
        _element.streams = AAZListType()
        _element.transform_kql = AAZStrType(
            serialized_name="transformKql",
        )

        destinations = _schema_data_collection_rule_resource_read.properties.data_flows.Element.destinations
        destinations.Element = AAZStrType()

        streams = _schema_data_collection_rule_resource_read.properties.data_flows.Element.streams
        streams.Element = AAZStrType()

        data_sources = _schema_data_collection_rule_resource_read.properties.data_sources
        data_sources.data_imports = AAZObjectType(
            serialized_name="dataImports",
        )
        data_sources.extensions = AAZListType()
        data_sources.iis_logs = AAZListType(
            serialized_name="iisLogs",
        )
        data_sources.log_files = AAZListType(
            serialized_name="logFiles",
        )
        data_sources.performance_counters = AAZListType(
            serialized_name="performanceCounters",
        )
        data_sources.platform_telemetry = AAZListType(
            serialized_name="platformTelemetry",
        )
        data_sources.prometheus_forwarder = AAZListType(
            serialized_name="prometheusForwarder",
        )
        data_sources.syslog = AAZListType()
        data_sources.windows_event_logs = AAZListType(
            serialized_name="windowsEventLogs",
        )
        data_sources.windows_firewall_logs = AAZListType(
            serialized_name="windowsFirewallLogs",
        )

        data_imports = _schema_data_collection_rule_resource_read.properties.data_sources.data_imports
        data_imports.event_hub = AAZObjectType(
            serialized_name="eventHub",
        )

        event_hub = _schema_data_collection_rule_resource_read.properties.data_sources.data_imports.event_hub
        event_hub.consumer_group = AAZStrType(
            serialized_name="consumerGroup",
        )
        event_hub.name = AAZStrType()
        event_hub.stream = AAZStrType()

        extensions = _schema_data_collection_rule_resource_read.properties.data_sources.extensions
        extensions.Element = AAZObjectType()

        _element = _schema_data_collection_rule_resource_read.properties.data_sources.extensions.Element
        _element.extension_name = AAZStrType(
            serialized_name="extensionName",
            flags={"required": True},
        )
        _element.extension_settings = AAZFreeFormDictType(
            serialized_name="extensionSettings",
        )
        _element.input_data_sources = AAZListType(
            serialized_name="inputDataSources",
        )
        _element.name = AAZStrType()
        _element.streams = AAZListType()

        input_data_sources = _schema_data_collection_rule_resource_read.properties.data_sources.extensions.Element.input_data_sources
        input_data_sources.Element = AAZStrType()

        streams = _schema_data_collection_rule_resource_read.properties.data_sources.extensions.Element.streams
        streams.Element = AAZStrType()

        iis_logs = _schema_data_collection_rule_resource_read.properties.data_sources.iis_logs
        iis_logs.Element = AAZObjectType()

        _element = _schema_data_collection_rule_resource_read.properties.data_sources.iis_logs.Element
        _element.log_directories = AAZListType(
            serialized_name="logDirectories",
        )
        _element.name = AAZStrType()
        _element.streams = AAZListType(
            flags={"required": True},
        )
        _element.transform_kql = AAZStrType(
            serialized_name="transformKql",
        )

        log_directories = _schema_data_collection_rule_resource_read.properties.data_sources.iis_logs.Element.log_directories
        log_directories.Element = AAZStrType()

        streams = _schema_data_collection_rule_resource_read.properties.data_sources.iis_logs.Element.streams
        streams.Element = AAZStrType()

        log_files = _schema_data_collection_rule_resource_read.properties.data_sources.log_files
        log_files.Element = AAZObjectType()

        _element = _schema_data_collection_rule_resource_read.properties.data_sources.log_files.Element
        _element.file_patterns = AAZListType(
            serialized_name="filePatterns",
            flags={"required": True},
        )
        _element.format = AAZStrType(
            flags={"required": True},
        )
        _element.name = AAZStrType()
        _element.settings = AAZObjectType()
        _element.streams = AAZListType(
            flags={"required": True},
        )
        _element.transform_kql = AAZStrType(
            serialized_name="transformKql",
        )

        file_patterns = _schema_data_collection_rule_resource_read.properties.data_sources.log_files.Element.file_patterns
        file_patterns.Element = AAZStrType()

        settings = _schema_data_collection_rule_resource_read.properties.data_sources.log_files.Element.settings
        settings.text = AAZObjectType()

        text = _schema_data_collection_rule_resource_read.properties.data_sources.log_files.Element.settings.text
        text.record_start_timestamp_format = AAZStrType(
            serialized_name="recordStartTimestampFormat",
            flags={"required": True},
        )

        streams = _schema_data_collection_rule_resource_read.properties.data_sources.log_files.Element.streams
        streams.Element = AAZStrType()

        performance_counters = _schema_data_collection_rule_resource_read.properties.data_sources.performance_counters
        performance_counters.Element = AAZObjectType()

        _element = _schema_data_collection_rule_resource_read.properties.data_sources.performance_counters.Element
        _element.counter_specifiers = AAZListType(
            serialized_name="counterSpecifiers",
        )
        _element.name = AAZStrType()
        _element.sampling_frequency_in_seconds = AAZIntType(
            serialized_name="samplingFrequencyInSeconds",
        )
        _element.streams = AAZListType()
        _element.transform_kql = AAZStrType(
            serialized_name="transformKql",
        )

        counter_specifiers = _schema_data_collection_rule_resource_read.properties.data_sources.performance_counters.Element.counter_specifiers
        counter_specifiers.Element = AAZStrType()

        streams = _schema_data_collection_rule_resource_read.properties.data_sources.performance_counters.Element.streams
        streams.Element = AAZStrType()

        platform_telemetry = _schema_data_collection_rule_resource_read.properties.data_sources.platform_telemetry
        platform_telemetry.Element = AAZObjectType()

        _element = _schema_data_collection_rule_resource_read.properties.data_sources.platform_telemetry.Element
        _element.name = AAZStrType()
        _element.streams = AAZListType(
            flags={"required": True},
        )

        streams = _schema_data_collection_rule_resource_read.properties.data_sources.platform_telemetry.Element.streams
        streams.Element = AAZStrType()

        prometheus_forwarder = _schema_data_collection_rule_resource_read.properties.data_sources.prometheus_forwarder
        prometheus_forwarder.Element = AAZObjectType()

        _element = _schema_data_collection_rule_resource_read.properties.data_sources.prometheus_forwarder.Element
        _element.label_include_filter = AAZDictType(
            serialized_name="labelIncludeFilter",
        )
        _element.name = AAZStrType()
        _element.streams = AAZListType()

        label_include_filter = _schema_data_collection_rule_resource_read.properties.data_sources.prometheus_forwarder.Element.label_include_filter
        label_include_filter.Element = AAZStrType()

        streams = _schema_data_collection_rule_resource_read.properties.data_sources.prometheus_forwarder.Element.streams
        streams.Element = AAZStrType()

        syslog = _schema_data_collection_rule_resource_read.properties.data_sources.syslog
        syslog.Element = AAZObjectType()

        _element = _schema_data_collection_rule_resource_read.properties.data_sources.syslog.Element
        _element.facility_names = AAZListType(
            serialized_name="facilityNames",
        )
        _element.log_levels = AAZListType(
            serialized_name="logLevels",
        )
        _element.name = AAZStrType()
        _element.streams = AAZListType()
        _element.transform_kql = AAZStrType(
            serialized_name="transformKql",
        )

        facility_names = _schema_data_collection_rule_resource_read.properties.data_sources.syslog.Element.facility_names
        facility_names.Element = AAZStrType()

        log_levels = _schema_data_collection_rule_resource_read.properties.data_sources.syslog.Element.log_levels
        log_levels.Element = AAZStrType()

        streams = _schema_data_collection_rule_resource_read.properties.data_sources.syslog.Element.streams
        streams.Element = AAZStrType()

        windows_event_logs = _schema_data_collection_rule_resource_read.properties.data_sources.windows_event_logs
        windows_event_logs.Element = AAZObjectType()

        _element = _schema_data_collection_rule_resource_read.properties.data_sources.windows_event_logs.Element
        _element.name = AAZStrType()
        _element.streams = AAZListType()
        _element.transform_kql = AAZStrType(
            serialized_name="transformKql",
        )
        _element.x_path_queries = AAZListType(
            serialized_name="xPathQueries",
        )

        streams = _schema_data_collection_rule_resource_read.properties.data_sources.windows_event_logs.Element.streams
        streams.Element = AAZStrType()

        x_path_queries = _schema_data_collection_rule_resource_read.properties.data_sources.windows_event_logs.Element.x_path_queries
        x_path_queries.Element = AAZStrType()

        windows_firewall_logs = _schema_data_collection_rule_resource_read.properties.data_sources.windows_firewall_logs
        windows_firewall_logs.Element = AAZObjectType()

        _element = _schema_data_collection_rule_resource_read.properties.data_sources.windows_firewall_logs.Element
        _element.name = AAZStrType()
        _element.profile_filter = AAZListType(
            serialized_name="profileFilter",
        )
        _element.streams = AAZListType(
            flags={"required": True},
        )

        profile_filter = _schema_data_collection_rule_resource_read.properties.data_sources.windows_firewall_logs.Element.profile_filter
        profile_filter.Element = AAZStrType()

        streams = _schema_data_collection_rule_resource_read.properties.data_sources.windows_firewall_logs.Element.streams
        streams.Element = AAZStrType()

        destinations = _schema_data_collection_rule_resource_read.properties.destinations
        destinations.azure_data_explorer = AAZListType(
            serialized_name="azureDataExplorer",
        )
        destinations.azure_monitor_metrics = AAZObjectType(
            serialized_name="azureMonitorMetrics",
        )
        destinations.event_hubs = AAZListType(
            serialized_name="eventHubs",
        )
        destinations.event_hubs_direct = AAZListType(
            serialized_name="eventHubsDirect",
        )
        destinations.log_analytics = AAZListType(
            serialized_name="logAnalytics",
        )
        destinations.microsoft_fabric = AAZListType(
            serialized_name="microsoftFabric",
        )
        destinations.monitoring_accounts = AAZListType(
            serialized_name="monitoringAccounts",
        )
        destinations.storage_accounts = AAZListType(
            serialized_name="storageAccounts",
        )
        destinations.storage_blobs_direct = AAZListType(
            serialized_name="storageBlobsDirect",
        )
        destinations.storage_tables_direct = AAZListType(
            serialized_name="storageTablesDirect",
        )

        azure_data_explorer = _schema_data_collection_rule_resource_read.properties.destinations.azure_data_explorer
        azure_data_explorer.Element = AAZObjectType()

        _element = _schema_data_collection_rule_resource_read.properties.destinations.azure_data_explorer.Element
        _element.database_name = AAZStrType(
            serialized_name="databaseName",
        )
        _element.ingestion_uri = AAZStrType(
            serialized_name="ingestionUri",
            flags={"read_only": True},
        )
        _element.name = AAZStrType()
        _element.resource_id = AAZStrType(
            serialized_name="resourceId",
        )

        azure_monitor_metrics = _schema_data_collection_rule_resource_read.properties.destinations.azure_monitor_metrics
        azure_monitor_metrics.name = AAZStrType()

        event_hubs = _schema_data_collection_rule_resource_read.properties.destinations.event_hubs
        event_hubs.Element = AAZObjectType()

        _element = _schema_data_collection_rule_resource_read.properties.destinations.event_hubs.Element
        _element.event_hub_resource_id = AAZStrType(
            serialized_name="eventHubResourceId",
        )
        _element.name = AAZStrType()

        event_hubs_direct = _schema_data_collection_rule_resource_read.properties.destinations.event_hubs_direct
        event_hubs_direct.Element = AAZObjectType()

        _element = _schema_data_collection_rule_resource_read.properties.destinations.event_hubs_direct.Element
        _element.event_hub_resource_id = AAZStrType(
            serialized_name="eventHubResourceId",
        )
        _element.name = AAZStrType()

        log_analytics = _schema_data_collection_rule_resource_read.properties.destinations.log_analytics
        log_analytics.Element = AAZObjectType()

        _element = _schema_data_collection_rule_resource_read.properties.destinations.log_analytics.Element
        _element.name = AAZStrType()
        _element.workspace_id = AAZStrType(
            serialized_name="workspaceId",
            flags={"read_only": True},
        )
        _element.workspace_resource_id = AAZStrType(
            serialized_name="workspaceResourceId",
        )

        microsoft_fabric = _schema_data_collection_rule_resource_read.properties.destinations.microsoft_fabric
        microsoft_fabric.Element = AAZObjectType()

        _element = _schema_data_collection_rule_resource_read.properties.destinations.microsoft_fabric.Element
        _element.artifact_id = AAZStrType(
            serialized_name="artifactId",
        )
        _element.database_name = AAZStrType(
            serialized_name="databaseName",
        )
        _element.ingestion_uri = AAZStrType(
            serialized_name="ingestionUri",
        )
        _element.name = AAZStrType()
        _element.tenant_id = AAZStrType(
            serialized_name="tenantId",
        )

        monitoring_accounts = _schema_data_collection_rule_resource_read.properties.destinations.monitoring_accounts
        monitoring_accounts.Element = AAZObjectType()

        _element = _schema_data_collection_rule_resource_read.properties.destinations.monitoring_accounts.Element
        _element.account_id = AAZStrType(
            serialized_name="accountId",
            flags={"read_only": True},
        )
        _element.account_resource_id = AAZStrType(
            serialized_name="accountResourceId",
        )
        _element.name = AAZStrType()

        storage_accounts = _schema_data_collection_rule_resource_read.properties.destinations.storage_accounts
        storage_accounts.Element = AAZObjectType()
        cls._build_schema_storage_blob_destination_read(storage_accounts.Element)

        storage_blobs_direct = _schema_data_collection_rule_resource_read.properties.destinations.storage_blobs_direct
        storage_blobs_direct.Element = AAZObjectType()
        cls._build_schema_storage_blob_destination_read(storage_blobs_direct.Element)

        storage_tables_direct = _schema_data_collection_rule_resource_read.properties.destinations.storage_tables_direct
        storage_tables_direct.Element = AAZObjectType()

        _element = _schema_data_collection_rule_resource_read.properties.destinations.storage_tables_direct.Element
        _element.name = AAZStrType()
        _element.storage_account_resource_id = AAZStrType(
            serialized_name="storageAccountResourceId",
        )
        _element.table_name = AAZStrType(
            serialized_name="tableName",
        )

        endpoints = _schema_data_collection_rule_resource_read.properties.endpoints
        endpoints.logs_ingestion = AAZStrType(
            serialized_name="logsIngestion",
            flags={"read_only": True},
        )
        endpoints.metrics_ingestion = AAZStrType(
            serialized_name="metricsIngestion",
            flags={"read_only": True},
        )

        metadata = _schema_data_collection_rule_resource_read.properties.metadata
        metadata.provisioned_by = AAZStrType(
            serialized_name="provisionedBy",
            flags={"read_only": True},
        )
        metadata.provisioned_by_immutable_id = AAZStrType(
            serialized_name="provisionedByImmutableId",
            flags={"read_only": True},
        )
        metadata.provisioned_by_resource_id = AAZStrType(
            serialized_name="provisionedByResourceId",
            flags={"read_only": True},
        )

        references = _schema_data_collection_rule_resource_read.properties.references
        references.enrichment_data = AAZObjectType(
            serialized_name="enrichmentData",
        )

        enrichment_data = _schema_data_collection_rule_resource_read.properties.references.enrichment_data
        enrichment_data.storage_blobs = AAZListType(
            serialized_name="storageBlobs",
        )

        storage_blobs = _schema_data_collection_rule_resource_read.properties.references.enrichment_data.storage_blobs
        storage_blobs.Element = AAZObjectType()

        _element = _schema_data_collection_rule_resource_read.properties.references.enrichment_data.storage_blobs.Element
        _element.blob_url = AAZStrType(
            serialized_name="blobUrl",
        )
        _element.lookup_type = AAZStrType(
            serialized_name="lookupType",
        )
        _element.name = AAZStrType()
        _element.resource_id = AAZStrType(
            serialized_name="resourceId",
        )

        stream_declarations = _schema_data_collection_rule_resource_read.properties.stream_declarations
        stream_declarations.Element = AAZObjectType()

        _element = _schema_data_collection_rule_resource_read.properties.stream_declarations.Element
        _element.columns = AAZListType()

        columns = _schema_data_collection_rule_resource_read.properties.stream_declarations.Element.columns
        columns.Element = AAZObjectType()

        _element = _schema_data_collection_rule_resource_read.properties.stream_declarations.Element.columns.Element
        _element.name = AAZStrType()
        _element.type = AAZStrType()

        system_data = _schema_data_collection_rule_resource_read.system_data
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

        tags = _schema_data_collection_rule_resource_read.tags
        tags.Element = AAZStrType()

        _schema.etag = cls._schema_data_collection_rule_resource_read.etag
        _schema.id = cls._schema_data_collection_rule_resource_read.id
        _schema.identity = cls._schema_data_collection_rule_resource_read.identity
        _schema.kind = cls._schema_data_collection_rule_resource_read.kind
        _schema.location = cls._schema_data_collection_rule_resource_read.location
        _schema.name = cls._schema_data_collection_rule_resource_read.name
        _schema.properties = cls._schema_data_collection_rule_resource_read.properties
        _schema.system_data = cls._schema_data_collection_rule_resource_read.system_data
        _schema.tags = cls._schema_data_collection_rule_resource_read.tags
        _schema.type = cls._schema_data_collection_rule_resource_read.type

    _schema_storage_blob_destination_read = None

    @classmethod
    def _build_schema_storage_blob_destination_read(cls, _schema):
        if cls._schema_storage_blob_destination_read is not None:
            _schema.container_name = cls._schema_storage_blob_destination_read.container_name
            _schema.name = cls._schema_storage_blob_destination_read.name
            _schema.storage_account_resource_id = cls._schema_storage_blob_destination_read.storage_account_resource_id
            return

        cls._schema_storage_blob_destination_read = _schema_storage_blob_destination_read = AAZObjectType()

        storage_blob_destination_read = _schema_storage_blob_destination_read
        storage_blob_destination_read.container_name = AAZStrType(
            serialized_name="containerName",
        )
        storage_blob_destination_read.name = AAZStrType()
        storage_blob_destination_read.storage_account_resource_id = AAZStrType(
            serialized_name="storageAccountResourceId",
        )

        _schema.container_name = cls._schema_storage_blob_destination_read.container_name
        _schema.name = cls._schema_storage_blob_destination_read.name
        _schema.storage_account_resource_id = cls._schema_storage_blob_destination_read.storage_account_resource_id


__all__ = ["Add"]
