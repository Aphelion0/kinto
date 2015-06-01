from cliquet import resource, schema


class RecordSchema(schema.ResourceSchema):
    class Options():
        preserve_unknown = True


@resource.register(
    record_path="/collections/{{collection_id}}/records/{{id}}",
    collection_path="/collections/{{collection_id}}/records",
    name="collection")
class Collection(resource.BaseResource):

    mapping = RecordSchema()

    @property
    def name(self):
        return self.request.matchdict['collection_id']

    def is_known_field(self, field_name):
        """Without schema, any field is considered as known."""
        return True
