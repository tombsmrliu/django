from django import forms
from .models import Topic, Comment
from django.utils.text import slugify

class TopicCreateForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'category', 'description', 'files',]


    # def save(self, commit=True):
        # topic = super(TopicCreateForm, self).save(commit=False)
        # topic.slug = slugify(topic.title)
        # if commit:
            # topic.save()
        # return topic



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
