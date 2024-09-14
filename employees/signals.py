import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from employees.models import Employee


@receiver(post_delete, sender=Employee)
def delete_avatar_on_employee_delete(sender, instance, **kwargs):
    if instance.avatar:
        if os.path.isfile(instance.avatar.path):
            os.remove(instance.avatar.path)
