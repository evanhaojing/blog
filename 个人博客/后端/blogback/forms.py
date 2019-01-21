from django import forms
from django.contrib.auth.hashers import check_password

from blogback.models import User


class RegisterForm(forms.Form):
    """注册验证"""
    username = forms.CharField(max_length=10, min_length=2, required=True,
                               error_messages={'required': '用户名不能为空！', 'max_length': '用户名不能超过10字符',
                                               'min_length': '用户名不能低于2字符'})
    userpwd = forms.CharField(max_length=18, min_length=6, required=True,
                              error_messages={'required': '密码不能为空！', 'max_length': '密码不能超过18字符',
                                              'min_length': '密码不能低于6字符'})
    usercpwd = forms.CharField(max_length=18, min_length=6, required=True,
                               error_messages={'required': '密码不能为空！', 'max_length': '密码不能超过18字符',
                                               'min_length': '密码不能低于6字符'})

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).first()
        if user:
            raise forms.ValidationError('该账号也存在')
        return self.cleaned_data['username']

    def clean(self):
        userpwd = self.cleaned_data['userpwd']
        usercpwd = self.cleaned_data['usercpwd']
        if userpwd != usercpwd:
            raise forms.ValidationError({'usercpwd': '密码不一致'})
        return self.cleaned_data


class LoginForm(forms.Form):
    """登陆验证"""
    username = forms.CharField(max_length=10, min_length=2, required=True,
                               error_messages={'required': '用户名不能为空！', 'max_length': '用户名不能超过10字符',
                                               'min_length': '用户名不能低于2字符'})
    userpwd = forms.CharField(max_length=18, min_length=6, required=True,
                              error_messages={'required': '密码不能为空！', 'max_length': '密码不能超过18字符',
                                              'min_length': '密码不能低于6字符'})

    def clean(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username=username).first()
        if not user:
            raise forms.ValidationError({'username': '该账号未注册'})
        password = self.cleaned_data.get('userpwd')
        if not check_password(password, user.password):
            raise forms.ValidationError({'userpwd': '密码或账号错误'})
        return self.cleaned_data


class CategoryForm(forms.Form):
    """栏目验证"""
    name = forms.CharField(max_length=20,required=True,
                           error_messages={'required': '栏目名不能为空！', 'max_length': '栏目名不能超过20字符'})
    alias = forms.CharField(max_length=20, required=False,
                            error_messages={'max_length': '栏目别名不能超过20字符'})
    keywords = forms.CharField(max_length=10, required=True,
                               error_messages={'required': '关键字不能为空！', 'max_length': '关键字不能超过10字符'})
    describe = forms.CharField(max_length=255, required=True,
                               error_messages={'required': '描述名不能为空！', 'max_length': '描述不能超过255字符'})
    fid = forms.IntegerField(required=False)


class ArticleForm(forms.Form):
    """文章验证"""
    title = forms.CharField(max_length=20,required=True,
                           error_messages={'required': '题目不能为空！', 'max_length': '题目不能超过20字符'})
    content = forms.CharField(required=True)
    keywords = forms.CharField(max_length=10, required=True,
                               error_messages={'required': '关键字不能为空！', 'max_length': '关键字不能超过10字符'})
    describe = forms.CharField(max_length=255, required=True,
                               error_messages={'required': '描述名不能为空！', 'max_length': '描述不能超过255字符'})
    category = forms.IntegerField(required=False)
