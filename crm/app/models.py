from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.urls import reverse


# Create your models here.
class User(AbstractUser):
    ROLES = (
        ('ADMIN', 'Administrator'),
        ('OPERATOR', 'Operator'),
        ('MARKETER', 'Marketer'),
        ('MANAGER', 'Manager'),
    )
    role = models.CharField(max_length=20, choices=ROLES)

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="custom_user_groups",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_permissions",
        related_query_name="user",
    )

    class Meta:
        swappable = 'AUTH_USER_MODEL'


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=100)
    services = models.ManyToManyField(Service)
    channel = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Lead(models.Model):
    STATUS = (
        ('POTENTIAL', 'Potential'),
        ('ACTIVE', 'Active'),
    )
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS, default='POTENTIAL')

    def __str__(self):
        return self.full_name


class Contract(models.Model):
    name = models.CharField(max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    document = models.FileField(upload_to='contracts/')
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    lead = models.OneToOneField(Lead, on_delete=models.CASCADE)


    @property
    def is_active(self):
        from django.utils import timezone
        return self.end_date >= timezone.now().date()

    def __str__(self):
        return self.name


class ActiveClient(models.Model):
    name = models.CharField('Название', max_length=100, unique=True)
    lead = models.ForeignKey(Lead, on_delete=models.PROTECT, verbose_name='Потенциальный клиент')
    contract = models.ForeignKey(Contract, on_delete=models.PROTECT, verbose_name='Контракт')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    description = models.TextField('Описание', blank=True)

    class Meta:
        verbose_name = 'Активный клиент'
        verbose_name_plural = 'Активные клиенты'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('activeclient_detail', kwargs={'pk': self.pk})





