from django import forms
from .models import Profile, Experiment

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'bio', 'avatar')

class ExperimentModelForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = ('title', 'image', 'description', 'likes')