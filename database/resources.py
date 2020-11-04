from import_export import resources
from .models import Mandate
class JobResources(resources.ModelResource):
    class meta:
        model = Mandate
