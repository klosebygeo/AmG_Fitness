from django.contrib import admin

from authapp.models import Enrollment, MembershipPlan, Trainer


# Register your models here.
admin.site.register(MembershipPlan)
admin.site.register(Enrollment)
admin.site.register(Trainer)

