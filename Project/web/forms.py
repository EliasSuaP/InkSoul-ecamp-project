from django import forms

class FormReserva(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido = forms.CharField(label='Apellido', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fecha = forms.DateField(label='Fecha', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    hora = forms.ChoiceField(label='hora', choices=[('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00')], widget=forms.Select(attrs={'class': 'form-control'}))