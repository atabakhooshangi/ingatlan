from django.contrib.admin.views import autocomplete

from dotenv import load_dotenv

load_dotenv()


class MyAutocompleteJsonView(
    autocomplete.AutocompleteJsonView
):

    def get_queryset(self):
        # Patch get_limit_choices_to for non-foreign key field
        self.source_field.get_limit_choices_to = lambda: {}
        return super().get_queryset()

    def process_request(self, request):
        term, model_admin, source_field, to_field_name = super().process_request(request)
        # Store to_field_name for use in get_context_data
        self.to_field_name = to_field_name
        return term, model_admin, source_field, to_field_name

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(object_list=object_list, **kwargs)
        # Patch __str__ to use to_field_name for `str(obj)` in AutocompleteJsonView.get
        for obj in context_data['object_list']:
            obj_type = type(obj)
            new_obj_type = type(obj_type.__name__, (obj_type,),
                                {'__str__': lambda _self: getattr(_self, self.to_field_name),
                                 '__module__': obj_type.__module__})
            obj.__class__ = new_obj_type
        return context_data
