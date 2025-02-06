from django import forms

class code_form(forms.Form):
    def __init__(self, *args, **kwargs):
        super(code_form, self).__init__(*args, **kwargs)
        for item in self.visible_fields():
            item.field.widget.attrs['class'] = 'form-control'
    code = forms.CharField(widget=forms.Textarea())
    
    
class UploadFileForm(forms.Form):
    file = forms.FileField(label='Select a file', widget=forms.FileInput(attrs={'class': 'form-control  w-100', 'type':'file'}))

    