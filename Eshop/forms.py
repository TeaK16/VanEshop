from django import forms

from Eshop.models import Van, MakeReservation, RentVan

class VanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VanForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Van
        exclude = ("user","van")


class MakeReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MakeReservationForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta: 
        model = MakeReservation
        exclude = ("user","van")

class RentVanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RentVanForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta: 
        model = RentVan
        exclude = ("user","van")
    
