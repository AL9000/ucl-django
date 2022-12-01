from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from inscriptions.models import InscriptionRequest, User, AcademicTraining


@admin.register(InscriptionRequest)
class InscriptionRequestAdmin(admin.ModelAdmin):
    list_display = (
        "candidat",
        "accepted",
    )


admin.site.register(User, UserAdmin)
admin.site.register(AcademicTraining)
