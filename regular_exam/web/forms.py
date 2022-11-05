from django import forms

from regular_exam.web.models import Profile, Car


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'passwords')


class CreateProfileForm(BaseProfileForm):
    passwords = forms.CharField(widget=forms.PasswordInput)


class EditProfileForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(BaseProfileForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
            return self.instance


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CreateCarForm(BaseCarForm):
    pass


class EditCarForm(BaseCarForm):
    pass


class DeleteCarForm(BaseCarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            return self.instance
