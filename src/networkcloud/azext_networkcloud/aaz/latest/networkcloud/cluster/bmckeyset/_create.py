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
    "networkcloud cluster bmckeyset create",
    is_preview=True,
)
class Create(AAZCommand):
    """Create a new baseboard management controller key set or update the existing one for the provided cluster.

    :example: Create or update baseboard management controller key set of cluster
        az networkcloud cluster bmckeyset create --name "bmcKeySetName" --extended-location name="/subscriptions/subscriptionId/resourceGroups/resourceGroupName/providers/Microsoft.ExtendedLocation/customLocations/clusterExtendedLocationName" type="CustomLocation" --location "location" --azure-group-id "f110271b-XXXX-4163-9b99-214d91660f0e" --expiration "2022-12-31T23:59:59.008Z" --privilege-level "Administrator" --user-list "[{description:'User description',azureUserName:userABC,sshPublicKey:{keyData:'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDWtG2RiEGfXs+RK19HU/G8EdEnbTlkl8Kkb5xv6nm+ttTb9FrW/dc9RQvai24VEFJmG4Fmi6Ow/yjxq+jTDuWOSs+Lo= admin@vm'}}]" --tags key1="myvalue1" key2="myvalue2" --cluster-name "clusterName" --resource-group "resourceGroupName"
    """

    _aaz_info = {
        "version": "2023-07-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.networkcloud/clusters/{}/bmckeysets/{}", "2023-07-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

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
        _args_schema.bmc_key_set_name = AAZStrArg(
            options=["-n", "--name", "--bmc-key-set-name"],
            help="The name of the baseboard management controller key set.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^([a-zA-Z0-9][a-zA-Z0-9-_]{0,28}[a-zA-Z0-9])$",
            ),
        )
        _args_schema.cluster_name = AAZStrArg(
            options=["--cluster-name"],
            help="The name of the cluster.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^([a-zA-Z0-9][a-zA-Z0-9-_]{0,28}[a-zA-Z0-9])$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "BmcKeySetParameters"

        _args_schema = cls._args_schema
        _args_schema.extended_location = AAZObjectArg(
            options=["--extended-location"],
            arg_group="BmcKeySetParameters",
            help="The extended location of the cluster associated with the resource.",
            required=True,
        )
        _args_schema.location = AAZResourceLocationArg(
            arg_group="BmcKeySetParameters",
            help="The geo-location where the resource lives",
            required=True,
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="BmcKeySetParameters",
            help="Resource tags.",
        )

        extended_location = cls._args_schema.extended_location
        extended_location.name = AAZStrArg(
            options=["name"],
            help="The resource ID of the extended location on which the resource will be created.",
            required=True,
        )
        extended_location.type = AAZStrArg(
            options=["type"],
            help="The extended location type, for example, CustomLocation.",
            required=True,
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.azure_group_id = AAZStrArg(
            options=["--azure-group-id"],
            arg_group="Properties",
            help="The object ID of Azure Active Directory group that all users in the list must be in for access to be granted. Users that are not in the group will not have access.",
            required=True,
        )
        _args_schema.expiration = AAZDateTimeArg(
            options=["--expiration"],
            arg_group="Properties",
            help="The date and time after which the users in this key set will be removed from the baseboard management controllers.",
            required=True,
        )
        _args_schema.privilege_level = AAZStrArg(
            options=["--privilege-level"],
            arg_group="Properties",
            help="The access level allowed for the users in this key set.",
            required=True,
            enum={"Administrator": "Administrator", "ReadOnly": "ReadOnly"},
        )
        _args_schema.user_list = AAZListArg(
            options=["--user-list"],
            arg_group="Properties",
            help="The unique list of permitted users.",
            required=True,
        )

        user_list = cls._args_schema.user_list
        user_list.Element = AAZObjectArg()

        _element = cls._args_schema.user_list.Element
        _element.azure_user_name = AAZStrArg(
            options=["azure-user-name"],
            help="The user name that will be used for access.",
            required=True,
        )
        _element.description = AAZStrArg(
            options=["description"],
            help="The free-form description for this user.",
            fmt=AAZStrArgFormat(
                max_length=256,
            ),
        )
        _element.ssh_public_key = AAZObjectArg(
            options=["ssh-public-key"],
            help="The SSH public key for this user.",
            required=True,
        )

        ssh_public_key = cls._args_schema.user_list.Element.ssh_public_key
        ssh_public_key.key_data = AAZStrArg(
            options=["key-data"],
            help="The public ssh key of the user.",
            required=True,
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.BmcKeySetsCreateOrUpdate(ctx=self.ctx)()
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

    class BmcKeySetsCreateOrUpdate(AAZHttpOperation):
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
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/clusters/{clusterName}/bmcKeySets/{bmcKeySetName}",
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
                    "bmcKeySetName", self.ctx.args.bmc_key_set_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "clusterName", self.ctx.args.cluster_name,
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
                    "api-version", "2023-07-01",
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
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("extendedLocation", AAZObjectType, ".extended_location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            extended_location = _builder.get(".extendedLocation")
            if extended_location is not None:
                extended_location.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})
                extended_location.set_prop("type", AAZStrType, ".type", typ_kwargs={"flags": {"required": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("azureGroupId", AAZStrType, ".azure_group_id", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("expiration", AAZStrType, ".expiration", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("privilegeLevel", AAZStrType, ".privilege_level", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("userList", AAZListType, ".user_list", typ_kwargs={"flags": {"required": True}})

            user_list = _builder.get(".properties.userList")
            if user_list is not None:
                user_list.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.userList[]")
            if _elements is not None:
                _elements.set_prop("azureUserName", AAZStrType, ".azure_user_name", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("description", AAZStrType, ".description")
                _elements.set_prop("sshPublicKey", AAZObjectType, ".ssh_public_key", typ_kwargs={"flags": {"required": True}})

            ssh_public_key = _builder.get(".properties.userList[].sshPublicKey")
            if ssh_public_key is not None:
                ssh_public_key.set_prop("keyData", AAZStrType, ".key_data", typ_kwargs={"flags": {"required": True}})

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

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

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.extended_location = AAZObjectType(
                serialized_name="extendedLocation",
                flags={"required": True},
            )
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200_201.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            extended_location = cls._schema_on_200_201.extended_location
            extended_location.name = AAZStrType(
                flags={"required": True},
            )
            extended_location.type = AAZStrType(
                flags={"required": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.azure_group_id = AAZStrType(
                serialized_name="azureGroupId",
                flags={"required": True},
            )
            properties.detailed_status = AAZStrType(
                serialized_name="detailedStatus",
                flags={"read_only": True},
            )
            properties.detailed_status_message = AAZStrType(
                serialized_name="detailedStatusMessage",
                flags={"read_only": True},
            )
            properties.expiration = AAZStrType(
                flags={"required": True},
            )
            properties.last_validation = AAZStrType(
                serialized_name="lastValidation",
                flags={"read_only": True},
            )
            properties.privilege_level = AAZStrType(
                serialized_name="privilegeLevel",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.user_list = AAZListType(
                serialized_name="userList",
                flags={"required": True},
            )
            properties.user_list_status = AAZListType(
                serialized_name="userListStatus",
                flags={"read_only": True},
            )

            user_list = cls._schema_on_200_201.properties.user_list
            user_list.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.user_list.Element
            _element.azure_user_name = AAZStrType(
                serialized_name="azureUserName",
                flags={"required": True},
            )
            _element.description = AAZStrType()
            _element.ssh_public_key = AAZObjectType(
                serialized_name="sshPublicKey",
                flags={"required": True},
            )

            ssh_public_key = cls._schema_on_200_201.properties.user_list.Element.ssh_public_key
            ssh_public_key.key_data = AAZStrType(
                serialized_name="keyData",
                flags={"required": True},
            )

            user_list_status = cls._schema_on_200_201.properties.user_list_status
            user_list_status.Element = AAZObjectType()

            _element = cls._schema_on_200_201.properties.user_list_status.Element
            _element.azure_user_name = AAZStrType(
                serialized_name="azureUserName",
                flags={"read_only": True},
            )
            _element.status = AAZStrType(
                flags={"read_only": True},
            )
            _element.status_message = AAZStrType(
                serialized_name="statusMessage",
                flags={"read_only": True},
            )

            system_data = cls._schema_on_200_201.system_data
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

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
