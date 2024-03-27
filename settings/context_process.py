from .models import Settings

def get_context_process(request):
    data=Settings.objects.last()
    return {'setting_data':data}