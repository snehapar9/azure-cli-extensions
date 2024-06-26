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
    "providerhub sku nested-resource-type-second create",
)
class Create(AAZCommand):
    """Create the resource type skus in the given resource type.

    :example: sku nested-resource-type-second create
        az providerhub sku nested-resource-type-second create --nested-resource-type-first "nestedResourceTypeFirst" --nested-resource-type-second "nestedResourceTypeSecond" --sku-settings [{"name":"freeSku","kind":"Standard","tier":"Tier1"},{"name":"premiumSku","costs":[{"meterId":"xxx"}],"kind":"Premium","tier":"Tier2"}] --provider-namespace "{providerNamespace}" --resource-type "{resourceType}" --sku "{skuName}"
    """

    _aaz_info = {
        "version": "2024-04-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.providerhub/providerregistrations/{}/resourcetyperegistrations/{}/resourcetyperegistrations/{}/resourcetyperegistrations/{}/skus/{}", "2024-04-01-preview"],
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
        _args_schema.nested_resource_type_first = AAZStrArg(
            options=["--nested-first", "--nested-resource-type-first"],
            help="The first child resource type.",
            required=True,
        )
        _args_schema.nested_resource_type_second = AAZStrArg(
            options=["--nested-second", "--nested-resource-type-second"],
            help="The second child resource type.",
            required=True,
        )
        _args_schema.provider_namespace = AAZStrArg(
            options=["--provider-namespace"],
            help="The name of the resource provider hosted within ProviderHub.",
            required=True,
        )
        _args_schema.resource_type = AAZStrArg(
            options=["--resource-type"],
            help="The resource type.",
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--sku", "--name"],
            help="The SKU.",
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.sku_settings = AAZListArg(
            options=["--sku-settings"],
            arg_group="Properties",
        )

        sku_settings = cls._args_schema.sku_settings
        sku_settings.Element = AAZObjectArg()

        _element = cls._args_schema.sku_settings.Element
        _element.capabilities = AAZListArg(
            options=["capabilities"],
        )
        _element.capacity = AAZObjectArg(
            options=["capacity"],
        )
        _element.costs = AAZListArg(
            options=["costs"],
        )
        _element.family = AAZStrArg(
            options=["family"],
        )
        _element.kind = AAZStrArg(
            options=["kind"],
        )
        _element.location_info = AAZListArg(
            options=["location-info"],
        )
        _element.locations = AAZListArg(
            options=["locations"],
        )
        _element.name = AAZStrArg(
            options=["name"],
            required=True,
        )
        _element.required_features = AAZListArg(
            options=["required-features"],
        )
        _element.required_quota_ids = AAZListArg(
            options=["required-quota-ids"],
        )
        _element.size = AAZStrArg(
            options=["size"],
        )
        _element.tier = AAZStrArg(
            options=["tier"],
        )

        capabilities = cls._args_schema.sku_settings.Element.capabilities
        capabilities.Element = AAZObjectArg()
        cls._build_args_sku_capability_create(capabilities.Element)

        capacity = cls._args_schema.sku_settings.Element.capacity
        capacity.default = AAZIntArg(
            options=["default"],
        )
        capacity.maximum = AAZIntArg(
            options=["maximum"],
        )
        capacity.minimum = AAZIntArg(
            options=["minimum"],
            required=True,
        )
        capacity.scale_type = AAZStrArg(
            options=["scale-type"],
            enum={"Automatic": "Automatic", "Manual": "Manual", "None": "None"},
        )

        costs = cls._args_schema.sku_settings.Element.costs
        costs.Element = AAZObjectArg()

        _element = cls._args_schema.sku_settings.Element.costs.Element
        _element.extended_unit = AAZStrArg(
            options=["extended-unit"],
        )
        _element.meter_id = AAZStrArg(
            options=["meter-id"],
            required=True,
        )
        _element.quantity = AAZIntArg(
            options=["quantity"],
        )

        location_info = cls._args_schema.sku_settings.Element.location_info
        location_info.Element = AAZObjectArg()

        _element = cls._args_schema.sku_settings.Element.location_info.Element
        _element.extended_locations = AAZListArg(
            options=["extended-locations"],
        )
        _element.location = AAZStrArg(
            options=["location"],
            required=True,
        )
        _element.type = AAZStrArg(
            options=["type"],
            enum={"ArcZone": "ArcZone", "EdgeZone": "EdgeZone", "NotSpecified": "NotSpecified"},
        )
        _element.zone_details = AAZListArg(
            options=["zone-details"],
        )
        _element.zones = AAZListArg(
            options=["zones"],
        )

        extended_locations = cls._args_schema.sku_settings.Element.location_info.Element.extended_locations
        extended_locations.Element = AAZStrArg()

        zone_details = cls._args_schema.sku_settings.Element.location_info.Element.zone_details
        zone_details.Element = AAZObjectArg()

        _element = cls._args_schema.sku_settings.Element.location_info.Element.zone_details.Element
        _element.capabilities = AAZListArg(
            options=["capabilities"],
        )
        _element.name = AAZListArg(
            options=["name"],
        )

        capabilities = cls._args_schema.sku_settings.Element.location_info.Element.zone_details.Element.capabilities
        capabilities.Element = AAZObjectArg()
        cls._build_args_sku_capability_create(capabilities.Element)

        name = cls._args_schema.sku_settings.Element.location_info.Element.zone_details.Element.name
        name.Element = AAZStrArg()

        zones = cls._args_schema.sku_settings.Element.location_info.Element.zones
        zones.Element = AAZStrArg()

        locations = cls._args_schema.sku_settings.Element.locations
        locations.Element = AAZStrArg()

        required_features = cls._args_schema.sku_settings.Element.required_features
        required_features.Element = AAZStrArg()

        required_quota_ids = cls._args_schema.sku_settings.Element.required_quota_ids
        required_quota_ids.Element = AAZStrArg()
        return cls._args_schema

    _args_sku_capability_create = None

    @classmethod
    def _build_args_sku_capability_create(cls, _schema):
        if cls._args_sku_capability_create is not None:
            _schema.name = cls._args_sku_capability_create.name
            _schema.value = cls._args_sku_capability_create.value
            return

        cls._args_sku_capability_create = AAZObjectArg()

        sku_capability_create = cls._args_sku_capability_create
        sku_capability_create.name = AAZStrArg(
            options=["name"],
            required=True,
        )
        sku_capability_create.value = AAZStrArg(
            options=["value"],
            required=True,
        )

        _schema.name = cls._args_sku_capability_create.name
        _schema.value = cls._args_sku_capability_create.value

    def _execute_operations(self):
        self.pre_operations()
        self.SkusCreateOrUpdateNestedResourceTypeSecond(ctx=self.ctx)()
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

    class SkusCreateOrUpdateNestedResourceTypeSecond(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/providers/Microsoft.ProviderHub/providerRegistrations/{providerNamespace}/resourcetypeRegistrations/{resourceType}/resourcetypeRegistrations/{nestedResourceTypeFirst}/resourcetypeRegistrations/{nestedResourceTypeSecond}/skus/{sku}",
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
                    "nestedResourceTypeFirst", self.ctx.args.nested_resource_type_first,
                    required=True,
                ),
                **self.serialize_url_param(
                    "nestedResourceTypeSecond", self.ctx.args.nested_resource_type_second,
                    required=True,
                ),
                **self.serialize_url_param(
                    "providerNamespace", self.ctx.args.provider_namespace,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceType", self.ctx.args.resource_type,
                    required=True,
                ),
                **self.serialize_url_param(
                    "sku", self.ctx.args.name,
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
                    "api-version", "2024-04-01-preview",
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
            _builder.set_prop("properties", AAZObjectType)

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("skuSettings", AAZListType, ".sku_settings", typ_kwargs={"flags": {"required": True}})

            sku_settings = _builder.get(".properties.skuSettings")
            if sku_settings is not None:
                sku_settings.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.skuSettings[]")
            if _elements is not None:
                _elements.set_prop("capabilities", AAZListType, ".capabilities")
                _elements.set_prop("capacity", AAZObjectType, ".capacity")
                _elements.set_prop("costs", AAZListType, ".costs")
                _elements.set_prop("family", AAZStrType, ".family")
                _elements.set_prop("kind", AAZStrType, ".kind")
                _elements.set_prop("locationInfo", AAZListType, ".location_info")
                _elements.set_prop("locations", AAZListType, ".locations")
                _elements.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("requiredFeatures", AAZListType, ".required_features")
                _elements.set_prop("requiredQuotaIds", AAZListType, ".required_quota_ids")
                _elements.set_prop("size", AAZStrType, ".size")
                _elements.set_prop("tier", AAZStrType, ".tier")

            capabilities = _builder.get(".properties.skuSettings[].capabilities")
            if capabilities is not None:
                _CreateHelper._build_schema_sku_capability_create(capabilities.set_elements(AAZObjectType, "."))

            capacity = _builder.get(".properties.skuSettings[].capacity")
            if capacity is not None:
                capacity.set_prop("default", AAZIntType, ".default")
                capacity.set_prop("maximum", AAZIntType, ".maximum")
                capacity.set_prop("minimum", AAZIntType, ".minimum", typ_kwargs={"flags": {"required": True}})
                capacity.set_prop("scaleType", AAZStrType, ".scale_type")

            costs = _builder.get(".properties.skuSettings[].costs")
            if costs is not None:
                costs.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.skuSettings[].costs[]")
            if _elements is not None:
                _elements.set_prop("extendedUnit", AAZStrType, ".extended_unit")
                _elements.set_prop("meterId", AAZStrType, ".meter_id", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("quantity", AAZIntType, ".quantity")

            location_info = _builder.get(".properties.skuSettings[].locationInfo")
            if location_info is not None:
                location_info.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.skuSettings[].locationInfo[]")
            if _elements is not None:
                _elements.set_prop("extendedLocations", AAZListType, ".extended_locations")
                _elements.set_prop("location", AAZStrType, ".location", typ_kwargs={"flags": {"required": True}})
                _elements.set_prop("type", AAZStrType, ".type")
                _elements.set_prop("zoneDetails", AAZListType, ".zone_details")
                _elements.set_prop("zones", AAZListType, ".zones")

            extended_locations = _builder.get(".properties.skuSettings[].locationInfo[].extendedLocations")
            if extended_locations is not None:
                extended_locations.set_elements(AAZStrType, ".")

            zone_details = _builder.get(".properties.skuSettings[].locationInfo[].zoneDetails")
            if zone_details is not None:
                zone_details.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".properties.skuSettings[].locationInfo[].zoneDetails[]")
            if _elements is not None:
                _elements.set_prop("capabilities", AAZListType, ".capabilities")
                _elements.set_prop("name", AAZListType, ".name")

            capabilities = _builder.get(".properties.skuSettings[].locationInfo[].zoneDetails[].capabilities")
            if capabilities is not None:
                _CreateHelper._build_schema_sku_capability_create(capabilities.set_elements(AAZObjectType, "."))

            name = _builder.get(".properties.skuSettings[].locationInfo[].zoneDetails[].name")
            if name is not None:
                name.set_elements(AAZStrType, ".")

            zones = _builder.get(".properties.skuSettings[].locationInfo[].zones")
            if zones is not None:
                zones.set_elements(AAZStrType, ".")

            locations = _builder.get(".properties.skuSettings[].locations")
            if locations is not None:
                locations.set_elements(AAZStrType, ".")

            required_features = _builder.get(".properties.skuSettings[].requiredFeatures")
            if required_features is not None:
                required_features.set_elements(AAZStrType, ".")

            required_quota_ids = _builder.get(".properties.skuSettings[].requiredQuotaIds")
            if required_quota_ids is not None:
                required_quota_ids.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

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
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType()
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.sku_settings = AAZListType(
                serialized_name="skuSettings",
                flags={"required": True},
            )

            sku_settings = cls._schema_on_200.properties.sku_settings
            sku_settings.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.sku_settings.Element
            _element.capabilities = AAZListType()
            _element.capacity = AAZObjectType()
            _element.costs = AAZListType()
            _element.family = AAZStrType()
            _element.kind = AAZStrType()
            _element.location_info = AAZListType(
                serialized_name="locationInfo",
            )
            _element.locations = AAZListType()
            _element.name = AAZStrType(
                flags={"required": True},
            )
            _element.required_features = AAZListType(
                serialized_name="requiredFeatures",
            )
            _element.required_quota_ids = AAZListType(
                serialized_name="requiredQuotaIds",
            )
            _element.size = AAZStrType()
            _element.tier = AAZStrType()

            capabilities = cls._schema_on_200.properties.sku_settings.Element.capabilities
            capabilities.Element = AAZObjectType()
            _CreateHelper._build_schema_sku_capability_read(capabilities.Element)

            capacity = cls._schema_on_200.properties.sku_settings.Element.capacity
            capacity.default = AAZIntType()
            capacity.maximum = AAZIntType()
            capacity.minimum = AAZIntType(
                flags={"required": True},
            )
            capacity.scale_type = AAZStrType(
                serialized_name="scaleType",
            )

            costs = cls._schema_on_200.properties.sku_settings.Element.costs
            costs.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.sku_settings.Element.costs.Element
            _element.extended_unit = AAZStrType(
                serialized_name="extendedUnit",
            )
            _element.meter_id = AAZStrType(
                serialized_name="meterId",
                flags={"required": True},
            )
            _element.quantity = AAZIntType()

            location_info = cls._schema_on_200.properties.sku_settings.Element.location_info
            location_info.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.sku_settings.Element.location_info.Element
            _element.extended_locations = AAZListType(
                serialized_name="extendedLocations",
            )
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.type = AAZStrType()
            _element.zone_details = AAZListType(
                serialized_name="zoneDetails",
            )
            _element.zones = AAZListType()

            extended_locations = cls._schema_on_200.properties.sku_settings.Element.location_info.Element.extended_locations
            extended_locations.Element = AAZStrType()

            zone_details = cls._schema_on_200.properties.sku_settings.Element.location_info.Element.zone_details
            zone_details.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.sku_settings.Element.location_info.Element.zone_details.Element
            _element.capabilities = AAZListType()
            _element.name = AAZListType()

            capabilities = cls._schema_on_200.properties.sku_settings.Element.location_info.Element.zone_details.Element.capabilities
            capabilities.Element = AAZObjectType()
            _CreateHelper._build_schema_sku_capability_read(capabilities.Element)

            name = cls._schema_on_200.properties.sku_settings.Element.location_info.Element.zone_details.Element.name
            name.Element = AAZStrType()

            zones = cls._schema_on_200.properties.sku_settings.Element.location_info.Element.zones
            zones.Element = AAZStrType()

            locations = cls._schema_on_200.properties.sku_settings.Element.locations
            locations.Element = AAZStrType()

            required_features = cls._schema_on_200.properties.sku_settings.Element.required_features
            required_features.Element = AAZStrType()

            required_quota_ids = cls._schema_on_200.properties.sku_settings.Element.required_quota_ids
            required_quota_ids.Element = AAZStrType()

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

            return cls._schema_on_200


class _CreateHelper:
    """Helper class for Create"""

    @classmethod
    def _build_schema_sku_capability_create(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})
        _builder.set_prop("value", AAZStrType, ".value", typ_kwargs={"flags": {"required": True}})

    _schema_sku_capability_read = None

    @classmethod
    def _build_schema_sku_capability_read(cls, _schema):
        if cls._schema_sku_capability_read is not None:
            _schema.name = cls._schema_sku_capability_read.name
            _schema.value = cls._schema_sku_capability_read.value
            return

        cls._schema_sku_capability_read = _schema_sku_capability_read = AAZObjectType()

        sku_capability_read = _schema_sku_capability_read
        sku_capability_read.name = AAZStrType(
            flags={"required": True},
        )
        sku_capability_read.value = AAZStrType(
            flags={"required": True},
        )

        _schema.name = cls._schema_sku_capability_read.name
        _schema.value = cls._schema_sku_capability_read.value


__all__ = ["Create"]
