from rest_framework import serializers


class ShortListSerializerMixin(object):
    def get_fields(self):
        use_list_fields = False
        if 'view' in self.context:
            use_list_fields = self.context.get('view').action == u'list'\
                and getattr(self.Meta, 'list_fields')
        if 'action' in self.context:
            use_list_fields = self.context.get('action') == u'list'\
                and getattr(self.Meta, 'list_fields')
        if use_list_fields:
            detail_fields = self.opts.fields
            self.opts.fields = self.Meta.list_fields

        fields = super(ShortListSerializerMixin, self).get_fields()

        if use_list_fields:
            self.opts.fields = detail_fields
        return fields


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields:
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)
