from django.shortcuts import render
from django.views import View
from .models import Company
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class CompanyView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        companies = list(Company.objects.values())
        if len(companies) > 0:
            # Diccionario de datos
            datos = {'message': "Succes", 'companies': companies}
        else:
            datos = {'message': "Compañias no encontradas"}
        return JsonResponse(datos)
    def post(self, request):
        datos = {'message': "Succes"}
        return JsonResponse(datos)
    def put():
        pass
    def delete():
        pass