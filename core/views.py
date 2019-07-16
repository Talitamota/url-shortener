from django.shortcuts import render, redirect

from .models import Url

from .forms import UrlForm

def index(request):
	url = Url()
	form = UrlForm()
	if request.method == 'POST':
		form = UrlForm(request.POST)
		if form.is_valid():
			url = form.save()

	contexto = {
		'url':url,
		'form': form,
		'url_hash':url.gera_url_encurtada()
	}	
	return render(request, 'core/index.html', contexto)


def redireciona_url(request, hash):
	url = Url.objects.get(url_hash=hash)
	return redirect(url.url_original)



