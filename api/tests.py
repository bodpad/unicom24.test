import requests
from django.test import TestCase
from django.contrib.auth.models import User
from .models import *


class TestPartnerAPI(TestCase):
    """
    Тестирование API для пользователей из группы "Партнеры"
    """
    CP_API_URL = 'http://127.0.0.1:8000/api/U:%s/customerProfile/'
    R2CO_API_URL = 'http://127.0.0.1:8000/api/U:%s/customerProfile/'
    TOKEN = '7974b74525131c43a2e610da7a31e880e746b0be'  # Тестовый токен пользователя из группы "Партнеры"

    def test_customer_profile_GET(self):
        """ Получение списка анкет """
        r = requests.get(self.CP_API_URL % self.TOKEN)
        self.assertEqual(r.status_code, 200)

    def test_customer_profile_POST(self):
        """ Добавление анкеты """
        data = {
            'surname': 'Иванов',
            'name': 'Иван',
            'patronymic': 'Иванович',
            'credit_score': '300',
            'phone_number': '9881234567',
            'passport_no': '1234555555',
            'birth_date': '1993-02-01',
        }
        r = requests.post(self.CP_API_URL % self.TOKEN, data=data)
        self.assertEqual(r.status_code, 201)


class TestSuperuserAPI(TestCase):
    # TODO: Реализовать
    pass


class TestCreditOrganizationAPI(TestCase):
    # TODO: Реализовать
    pass