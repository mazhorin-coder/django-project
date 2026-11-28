from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Skill(models.Model):
    name = models.CharField("Название навыка", max_length=100, unique=True)

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.name


class Employee(models.Model):
    class Gender(models.TextChoices):
        MALE = "M", "Мужской"
        FEMALE = "F", "Женский"

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="employee_profile",
        verbose_name="Пользователь",
    )
    gender = models.CharField("Пол", max_length=1, choices=Gender.choices)
    first_name = models.CharField("Имя", max_length=150)
    last_name = models.CharField("Фамилия", max_length=150)
    middle_name = models.CharField("Отчество(при наличии)", max_length=150, blank=True)
    skills = models.ManyToManyField(
        Skill, through="EmployeeSkill", verbose_name="Навыки"
    )
    description = models.TextField("Описание", blank=True)

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}".strip()


class EmployeeSkill(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name="Сотрудник",
    )
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        verbose_name="Навык",
    )
    level = models.PositiveSmallIntegerField(
        "Уровень освоения",
        validators=[MinValueValidator(1), MaxValueValidator(10)],
    )

    class Meta:
        verbose_name = "Навык сотрудника"
        verbose_name_plural = "Навыки сотрудников"
        unique_together = ("employee", "skill")

    def __str__(self):
        return f"{self.employee} - {self.skill} ({self.level}/10)"

class EmployeeImage(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Сотрудник"
    )
    image = models.ImageField("Изображение", upload_to="employees/")
    order = models.PositiveIntegerField("Порядковый номер", default=1, validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = "Изображение сотрудника"
        verbose_name_plural = "Изображения сотрудников"
        ordering = ["order"]

    def __str__(self):
        return f"Фото {self.employee} (№{self.order})"
