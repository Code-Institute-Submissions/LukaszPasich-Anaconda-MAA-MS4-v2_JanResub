from django import forms
from .models import Discipline, Membership


class MembershipForm(forms.ModelForm):

    class Meta:
        model = Membership
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        disciplines = Discipline.objects.all()
        friendly_names = [(d.id, d.get_friendly_name()) for d in disciplines]

        self.fields['discipline'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-light rounded'
