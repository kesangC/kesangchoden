from django.contrib import admin

from .models import RoomAllocation
admin.site.register(RoomAllocation)

from .models import login
admin.site.register(login)

from .models import maintenance
admin.site.register(maintenance)

from myapp.models import Guideline
admin.site.register(Guideline)

from myapp.models import Notification
admin.site.register(Notification)