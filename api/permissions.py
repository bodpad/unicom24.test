from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class CustomerProfilePermission(permissions.BasePermission):
    """
    Разграничение прав доступа пользователей к анкетам клиентов.
    """
    def has_permission(self, request, view):

        if request.user.group == 'superuser':
            # Разрешаем любые методы запросов пользователям
            # из групыы "Суперпользователи"
            return True

        if request.user.group == 'partner':
            # Разграничиваем доступ пользователям из группы "Партнеры"
            if request.method in permissions.SAFE_METHODS or request.method == 'POST':
                return True

        raise PermissionDenied  # Для всех остальных

    def has_object_permission(self, request, view, obj):

        if request.user.group == 'superuser':
            # Для пользователям из групыы "Суперпользователи",
            # разрешаем любые методы запросов.
            return True

        if request.user.group == 'partner':
            # Для пользователей из группы "Партнеры", разрешаем только "безопасные" методы.
            return True if request.method in permissions.SAFE_METHODS else False

        raise PermissionDenied  # Для всех остальных


class Request2coPermission(permissions.BasePermission):
    """
    Разграничение прав доступа пользователей к заявкам в кредитные организации.
    """
    def has_permission(self, request, view):

        if request.user.group == 'superuser':
            # Для пользователям из групыы "Суперпользователи",
            # разрешаем любые методы запросов.
            return True

        if request.user.group == 'partner':
            # Для пользователям из групыы "Партнеры",
            # разрешаем операции вставки.
            return True if request.method == 'POST' else False

        if request.user.group == 'credit_organization':
            # Для пользователей из группы "Кредитные организации",
            # разрешаем только "безопасные" методы.
            return True if request.method in permissions.SAFE_METHODS else False

        raise PermissionDenied  # Для всех остальных

    def has_object_permission(self, request, view, obj):

        if request.user.group == 'superuser':
            # Для пользователям из групыы "Суперпользователи",
            # разрешаем любые методы запросов.
            return True

        if request.user.group == 'credit_organization':
            # Для пользователей из группы "Кредитные организации",
            # разрешаем только "безопасные" методы.
            return True if request.method in permissions.SAFE_METHODS else False

        raise PermissionDenied  # Для всех остальных