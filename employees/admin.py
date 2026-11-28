from django.contrib import admin
from .models import Employee, Skill, EmployeeSkill, EmployeeImage 

class EmployeeSkillInline(admin.TabularInline):
    model = EmployeeSkill
    extra = 1

class EmployeeImageInline(admin.TabularInline):
    model = EmployeeImage
    extra = 1

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "middle_name", "gender", "user")
    list_display_links = ("last_name", "first_name")
    inlines = (EmployeeSkillInline, EmployeeImageInline)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)
