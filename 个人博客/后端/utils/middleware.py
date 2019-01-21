import re

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from blogback.models import User


class AuthMiddlewareLogin(MiddlewareMixin):
    def process_request(self, request):
        user_id = request.session.get('user_id')
        if user_id:
            user = User.objects.filter(pk=user_id).first()
            request.user = user
        path = request.path
        if path == '/':
            return None
        not_need_check = ['/blogback/index/', '/blogback/register/', '/blogback/login/']
        for check_path in not_need_check:
            if re.match(check_path, path):
                return None
        if not user_id:
            return HttpResponseRedirect(reverse('blogback:login'))
