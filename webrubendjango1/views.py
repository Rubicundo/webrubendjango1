from django.http import HttpResponse
from django.template import Template, Context


def saludo(request):

    nombre = "Manolo"
    apellido = "Pérez"

    doc_externo=open("/home/ruben/proyectosdjango/proyectodjango2/webrubendjango1/webrubendjango1/templates/template1.html")
    templ = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre_persona": nombre, "apellido": apellido})
    documento = templ.render(ctx)
    return HttpResponse(documento)
