from django.contrib import admin

from .models import Employee, EmployeeSkill, Skill


class EmployeeSkillInline(admin.TabularInline):
    model = EmployeeSkill
    extra = 1


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("gender", "first_name", "last_name", "middle_name", "user")
    inlines = (EmployeeSkillInline,)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)
