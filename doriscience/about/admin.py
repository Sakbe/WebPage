from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

# Register your models here.
from .models import WorkExperience, Education, Award, Skill, Language

@admin.register(Skill)
class SkillAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(WorkExperience)
admin.site.register(Education)
admin.site.register(Award)
admin.site.register(Language)