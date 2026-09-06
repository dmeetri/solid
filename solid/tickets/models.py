from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class TicketModel(models.Model):
    creator = models.CharField(max_length=100)
    desceiption = models.TextField()
    ticket_number = models.CharField(
        max_length=20,
        unique=True,
        editable=False
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )

    class Status(models.TextChoices):
        NEW = 'new', 'Ожидает принятия'
        ACCEPTED = 'accepted', 'Принята'
        IN_PROGRESS = 'in_progress', 'Выполняется'
        COMPLETED = 'completed', 'Завершена'
        REJECTED = 'rejected', 'Отклонена'

    status = models.CharField(
        choices=Status.choices,
        default=Status.NEW,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    accepted_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.ticket_number:
            last = TicketModel.objects.all().order_by('id').last()

            if last:
                num = int(last.ticket_number[-6:]) + 1
            else:
                num = 1

            self.ticket_number = f"{timezone.now().year}{num:06d}"
        super().save(*args, **kwargs)


class FeedbackModel(models.Model):
    ticket = models.ForeignKey(
        TicketModel,
        on_delete=models.CASCADE,
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class AdminTaskModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class AssignmentCounterModel(models.Model):
    last_user = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, blank=True,
    )
