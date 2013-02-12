from django.shortcuts import render_to_response
from scorecenter.JuegoApp.models import Juego
from scorecenter.PrediccionApp.models import Prediccion
from scorecenter.PrediccionApp.models import TipoResultado
from scorecenter.PrediccionApp.models import AuthUser

def juegosguardar(request, pagina="1", idgame=1, resa=0, resb=1):
	print >> sys.stderr, 'Goodbye, cruel world!'
	game = Juego.objects.filter(id=idgame).get
	temporal = Prediccion(idusario=2, idjuego=idgame, equipoa=resa, equipob=resb, resultado=1)
	temporal.save()
	pag = int(pagina)
	pag = pag-1
	lista = Juego.objects.order_by('-fecha')[pag*4:pag*4+4]
	template_name = 'juegos_semana.html'
	return render_to_response(template_name,{'lista':lista})

def juegos(request, pagina="1"):
	pag = int(pagina)
	pag = pag-1
	lista = Juego.objects.order_by('fecha')[pag*4:pag*4+4]
	template_name = 'resultados.html'
	return render_to_response(template_name,{'lista':lista})

def juegosap(request, pagina="1", idgame=-1, resa=-1, resb=-1):
	if(idgame==-1 and resa==-1 and resb==-1):
		pag = int(pagina)
		pag = pag-1
		lista = Juego.objects.order_by('-fecha', '-id')[pag*4:pag*4+4]
		template_name = 'juegos_semana.html'
		return render_to_response(template_name,{'lista':lista})
	else:
		game = Juego.objects.get(id=int(idgame))
		resul = TipoResultado.objects.get(id=1)
		print(game)
		print(resul)
		user = AuthUser.objects.get(username=request.user)
		print(user)
		temporal = Prediccion(equipoa=int(resa), equipob=int(resb))
		temporal.idusario = user
		#temporal.Juego = game
		temporal.idjuego = Juego.objects.get(id=int(idgame))
		temporal.resultado = resul
		temporal.save()
		pag = int(pagina)
		pag = pag-1
		lista = Juego.objects.order_by('-fecha')[pag*4:pag*4+4]
		template_name = 'juegos_semana.html'
		return render_to_response(template_name,{'lista':lista})
