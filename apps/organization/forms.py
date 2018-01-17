# -*- coding:utf-8 -*-
__author__ = 'tgw'
__date__ = '2017/11/20 9:08'

import re
from django import forms

from operation.models import UserAsk


# 与ModelForm对比，（ModelForm好用）
# class UserAskForm(forms.Form):
#     # required=Ture 表示必须填不为空。
#     name = forms.CharField(required=True,)
#     phone = forms.CharField(required=True,max_length=11, min_length=11)
#     course_name = forms.CharField(required=True,max_length=50, min_length=5)


class UserAskForm(forms.ModelForm):
    # ModelForm可以继承UserAsk还可以定义自己的字段：
    # my_field = forms.CharField()
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        """
        验证手机号码是否合法
        """
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法", code="mobile_invalid")
