from .models import Meating

def update_status_of_meating():
    for meating in Meating.objects.all():
        now = meating.now()
        if now:
            meating.status = "now"
        elif meating.status == 'now' and now is False:
            meating.status = "end"
        else:
            ...