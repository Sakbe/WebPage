from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

# Register your models here.
from .models import WorkExperience, Education, Award, Language, Skill, Hobby

admin.site.register(WorkExperience)
admin.site.register(Education)

@admin.register(Award)
class AwardAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass

@admin.register(Language)
class LanguageAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass

@admin.register(Skill)
class SkillAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass

@admin.register(Hobby)
class HobbyAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass