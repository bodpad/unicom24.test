from django.db import models


class CustomerProfile(models.Model):
    """ Анкета клиента """
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    name = models.CharField(max_length=255, verbose_name='Имя')
    patronymic = models.CharField(max_length=255, verbose_name='Отчество')
    passport_no = models.CharField(max_length=10, verbose_name='Номер паспорта')
    phone_number = models.CharField(max_length=10, verbose_name='Номер телефона')
    birth_date = models.DateField(verbose_name='Дата рождения')
    credit_score = models.IntegerField(verbose_name='Скоринговый балл')
    create_date = models.DateTimeField(auto_now=True, verbose_name='Дата и время создания')
    modify_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время изменения')

    def __str__(self):
        return "{0} {1} {2}".format(self.surname, self.name, self.patronymic)

    class Meta:
        verbose_name = 'Анкета клиента'
        verbose_name_plural = 'Анкеты клиентов'


class Offer(models.Model):
    """ Предложение """
    CHOICES_TYPE = (
        (1, 'Потреб'),
        (2, 'Ипотека'),
        (3, 'Аавтокредит'),
        (4, 'КМСБ'),
    )
    name = models.CharField(max_length=255, verbose_name='Название	предложения')
    type = models.PositiveSmallIntegerField(choices=CHOICES_TYPE, verbose_name='Тип предложения')
    min_credit_score = models.IntegerField(verbose_name='Минимальный скоринговый балл', default=0)
    max_credit_score = models.IntegerField(verbose_name='Максимальный скоринговый балл', default=1000)
    create_date = models.DateTimeField(auto_now=True)
    modify_date = models.DateTimeField(auto_now_add=True)
    rotation_start = models.DateTimeField(verbose_name='Дата и время начала ротации')
    rotation_end = models.DateTimeField(verbose_name='Дата и время окончания ротации')
    credit_org = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        verbose_name='Кредитная организация',
        limit_choices_to={'groups__name': 'credit_organization'} # Ограничиваем выбор только пользователями
                                                                 # из группы "Кредитные оранизации"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'


class Request2co(models.Model):
    """
    Заявка	в	кредитную	организацию
    (Request2co - request to the credit organization)
    """
    CHOICES_STATUS = (
        (1, 'NEW'),
        (2, 'SENT'),
        (3, 'RECEIVED')
    )
    create_date = models.DateTimeField(auto_now=True, verbose_name='Дата и время создания')
    sent_date = models.DateTimeField(auto_now=True, verbose_name='Дата и время отправки')
    status = models.PositiveSmallIntegerField(choices=CHOICES_STATUS, default=1, verbose_name='Статус')
    customer_profile = models.ForeignKey('CustomerProfile', on_delete=models.CASCADE, verbose_name='Анкета клиента')
    offer = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name='Предложение')

    class Meta:
        verbose_name = 'Заявка в кредитную организацию'
        verbose_name_plural = 'Заявки в кредитные организации'