import json
from .models import Usuario
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

# Create your views here.
class Mivista(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if id > 0:

            usuario= list(Usuario.objects.filter(id=id).values())
            
            if len(usuario) > 0:
                user= usuario[0]
                datos= {"Mensaje": "Success", 'Usuarios': user}

            else:
                datos= {"Mensaje": "No existen esta compania"}

            return JsonResponse(datos)  

        else:

            usuario= list(Usuario.objects.values())

            if len(usuario) > 0:
                datos= {"Mensaje": "Success", 'Usuarios': usuario}

            else:
                datos= {"Mensaje": "No existen companias"}

            return JsonResponse(datos)


    def post(self, request):
        jd= json.loads(request.body)
        print(jd)
        Usuario.objects.create(Nombre= jd['nombre'], url=jd['url'])
        datos= {"Mensaje": "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd= json.loads(request.body)
        usuario= list(Usuario.objects.filter(id=id).values())
            
        if len(usuario) > 0:
            user= Usuario.objects.get(id= id)
            user.Nombre= jd['nombre']
            user.url= jd['url']
            user.save()
            datos= {"Mensaje": "Success"}

        else:
            datos= {"Mensaje": "No existen esta compania"}

        return JsonResponse(datos)


    def delete(self, request, id):
        usuario= list(Usuario.objects.filter(id=id).values())
       
            
        if len(usuario) > 0:
            Usuario.objects.filter(id=id).delete()
            datos= {"Mensaje": "Success"}

        else:
            datos= {"Mensaje": "No existen esta compania"}

        return JsonResponse(datos)

