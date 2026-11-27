from django.db import models

from employees.models import Employee


class Workplace(models.Model):
    table_number = models.PositiveIntegerField("Номер стола", unique=True)
    description = models.TextField("Дополнительная информация", blank=True)
    employee = models.OneToOneField(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="workplace",
        verbose_name="Сотрудник",
    )

    class Meta:
        verbose_name = "Рабочее место"
        verbose_name_plural = "Рабочие места"

    def __str__(self):
        return f"Стол №{self.table_number}"
