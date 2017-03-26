from django.contrib.auth.forms import AuthenticationForm

class MyAuthenticationForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super(MyAuthenticationForm, self).__init__(*args, **kwargs)

		self.base_fields['username'].widget.attrs['class']='form-control'
		self.base_fields['password'].widget.attrs['class']='form-control'
