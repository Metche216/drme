import json
from django.conf import settings

def schema_context(request):
    """
    Context processor to expose JSON-LD schema data to templates.
    Gracefully handles missing CLINIC_SCHEMA_DATA in settings.
    """
    schema_data = getattr(settings, 'CLINIC_SCHEMA_DATA', None)
    
    if schema_data:
        try:
            return {'schema_json': json.dumps(schema_data)}
        except (TypeError, ValueError):
            pass
            
    return {'schema_json': None}
