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
    "redisenterprise database update",
)
class Update(AAZCommand):
    """Update a database
    """

    _aaz_info = {
        "version": "2023-03-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.cache/redisenterprise/{}/databases/{}", "2023-03-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.cluster_name = AAZStrArg(
            options=["--cluster-name"],
            help="The name of the RedisEnterprise cluster.",
            required=True,
            id_part="name",
        )
        _args_schema.database_name = AAZStrArg(
            options=["-n", "--name", "--database-name"],
            help="The name of the database.",
            required=True,
            id_part="child_name_1",
            default="default",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.client_protocol = AAZStrArg(
            options=["--client-protocol"],
            arg_group="Properties",
            help="Specifies whether redis clients can connect using TLS-encrypted or plaintext redis protocols. Default is TLS-encrypted.",
            nullable=True,
            enum={"Encrypted": "Encrypted", "Plaintext": "Plaintext"},
        )
        _args_schema.eviction_policy = AAZStrArg(
            options=["--eviction-policy"],
            arg_group="Properties",
            help="Redis eviction policy - default is VolatileLRU",
            nullable=True,
            enum={"AllKeysLFU": "AllKeysLFU", "AllKeysLRU": "AllKeysLRU", "AllKeysRandom": "AllKeysRandom", "NoEviction": "NoEviction", "VolatileLFU": "VolatileLFU", "VolatileLRU": "VolatileLRU", "VolatileRandom": "VolatileRandom", "VolatileTTL": "VolatileTTL"},
        )
        _args_schema.persistence = AAZObjectArg(
            options=["--persistence"],
            arg_group="Properties",
            help="Persistence settings",
            nullable=True,
        )

        persistence = cls._args_schema.persistence
        persistence.aof_enabled = AAZBoolArg(
            options=["aof-enabled"],
            help="Sets whether AOF is enabled.",
            nullable=True,
        )
        persistence.aof_frequency = AAZStrArg(
            options=["aof-frequency"],
            help="Sets the frequency at which data is written to disk.",
            nullable=True,
            enum={"1s": "1s", "always": "always"},
        )
        persistence.rdb_enabled = AAZBoolArg(
            options=["rdb-enabled"],
            help="Sets whether RDB is enabled.",
            nullable=True,
        )
        persistence.rdb_frequency = AAZStrArg(
            options=["rdb-frequency"],
            help="Sets the frequency at which a snapshot of the database is created.",
            nullable=True,
            enum={"12h": "12h", "1h": "1h", "6h": "6h"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.DatabasesGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.DatabasesCreate(ctx=self.ctx)()
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

    class DatabasesGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/redisEnterprise/{clusterName}/databases/{databaseName}",
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
                    "clusterName", self.ctx.args.cluster_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "databaseName", self.ctx.args.database_name,
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
                    "api-version", "2023-03-01-preview",
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
            _UpdateHelper._build_schema_database_read(cls._schema_on_200)

            return cls._schema_on_200

    class DatabasesCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "original-uri"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "original-uri"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Cache/redisEnterprise/{clusterName}/databases/{databaseName}",
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
                    "clusterName", self.ctx.args.cluster_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "databaseName", self.ctx.args.database_name,
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
                    "api-version", "2023-03-01-preview",
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
            _UpdateHelper._build_schema_database_read(cls._schema_on_200_201)

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
                properties.set_prop("clientProtocol", AAZStrType, ".client_protocol")
                properties.set_prop("evictionPolicy", AAZStrType, ".eviction_policy")
                properties.set_prop("persistence", AAZObjectType, ".persistence")

            persistence = _builder.get(".properties.persistence")
            if persistence is not None:
                persistence.set_prop("aofEnabled", AAZBoolType, ".aof_enabled")
                persistence.set_prop("aofFrequency", AAZStrType, ".aof_frequency")
                persistence.set_prop("rdbEnabled", AAZBoolType, ".rdb_enabled")
                persistence.set_prop("rdbFrequency", AAZStrType, ".rdb_frequency")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    _schema_database_read = None

    @classmethod
    def _build_schema_database_read(cls, _schema):
        if cls._schema_database_read is not None:
            _schema.id = cls._schema_database_read.id
            _schema.name = cls._schema_database_read.name
            _schema.properties = cls._schema_database_read.properties
            _schema.system_data = cls._schema_database_read.system_data
            _schema.type = cls._schema_database_read.type
            return

        cls._schema_database_read = _schema_database_read = AAZObjectType()

        database_read = _schema_database_read
        database_read.id = AAZStrType(
            flags={"read_only": True},
        )
        database_read.name = AAZStrType(
            flags={"read_only": True},
        )
        database_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        database_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        database_read.type = AAZStrType(
            flags={"read_only": True},
        )

        properties = _schema_database_read.properties
        properties.client_protocol = AAZStrType(
            serialized_name="clientProtocol",
        )
        properties.clustering_policy = AAZStrType(
            serialized_name="clusteringPolicy",
        )
        properties.eviction_policy = AAZStrType(
            serialized_name="evictionPolicy",
        )
        properties.geo_replication = AAZObjectType(
            serialized_name="geoReplication",
        )
        properties.modules = AAZListType()
        properties.persistence = AAZObjectType()
        properties.port = AAZIntType()
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.resource_state = AAZStrType(
            serialized_name="resourceState",
            flags={"read_only": True},
        )

        geo_replication = _schema_database_read.properties.geo_replication
        geo_replication.group_nickname = AAZStrType(
            serialized_name="groupNickname",
        )
        geo_replication.linked_databases = AAZListType(
            serialized_name="linkedDatabases",
        )

        linked_databases = _schema_database_read.properties.geo_replication.linked_databases
        linked_databases.Element = AAZObjectType()

        _element = _schema_database_read.properties.geo_replication.linked_databases.Element
        _element.id = AAZStrType()
        _element.state = AAZStrType(
            flags={"read_only": True},
        )

        modules = _schema_database_read.properties.modules
        modules.Element = AAZObjectType()

        _element = _schema_database_read.properties.modules.Element
        _element.args = AAZStrType()
        _element.name = AAZStrType(
            flags={"required": True},
        )
        _element.version = AAZStrType(
            flags={"read_only": True},
        )

        persistence = _schema_database_read.properties.persistence
        persistence.aof_enabled = AAZBoolType(
            serialized_name="aofEnabled",
        )
        persistence.aof_frequency = AAZStrType(
            serialized_name="aofFrequency",
        )
        persistence.rdb_enabled = AAZBoolType(
            serialized_name="rdbEnabled",
        )
        persistence.rdb_frequency = AAZStrType(
            serialized_name="rdbFrequency",
        )

        system_data = _schema_database_read.system_data
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

        _schema.id = cls._schema_database_read.id
        _schema.name = cls._schema_database_read.name
        _schema.properties = cls._schema_database_read.properties
        _schema.system_data = cls._schema_database_read.system_data
        _schema.type = cls._schema_database_read.type


__all__ = ["Update"]
