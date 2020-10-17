from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

# Register your models here.
from .models import WorkExperience, Education, Thesis, Award, Language, Skill, Hobby

admin.site.register(WorkExperience)

class ThesisInline(SortableInlineAdminMixin, admin.StackedInline):
    model = Thesis
    extra = 1

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    inlines = [ ThesisInline ]
    ordering = ['-end_date']

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