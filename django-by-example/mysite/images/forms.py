from urllib import request
from django import forms
from .models import Image
from django.core.files.base import ContentFile
from django.utils.text import slugify


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        # new 知识点
        widget = {
                'url':forms.HiddenInput,
                }


    def clean_url(self):
        url = self.cleaned_data['url']
        vaild_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in vaild_extensions:
            raise forms.ValidationError('url错误！')
        return url

    def save(self, force_insert=False, force_ipdate=False, commit=True):
        image = super(ImageCreateForm, self).save(commit=False)
        image_url = self.cleaned_data['url']
        image_name = '{}.{}'.format(slugify(image.title), image_url.rsplit('.',1)[1].lower())

        response = request.urlopen(image_url)
        image.image.save(image_name, ContentFile(response.read()), save=False)
        if commit:
            image.save();
        return image
