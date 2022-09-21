from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def userinfo(request):
    context = {
        'nombre':'Sergio Antonio',
        'apellidos':'Ananias Ortega',
        'email':'sergio.ananias.o@gmail.com',
        'telefono':'941370977',
        'laboral':'Trabajando',
        'profesion':'Desarrollador'
    }
    return render(request,'user.html',context)

def toys(request):
    context={
        'titulo':'Juguetes',
        'productos':[
            {
                'nombre':'nombre',
                'precio':'precio',
                'descripcion':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit nobis ex sed repudiandae neque asperiores nesciunt, dolore unde nam ut, harum, nostrum labore eos modi ipsam debitis maiores tempore rerum?',
                'precio':'precio',
                'uri':'uri'
            },
            {
                'nombre':'nombre',
                'precio':'precio',
                'descripcion':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit nobis ex sed repudiandae neque asperiores nesciunt, dolore unde nam ut, harum, nostrum labore eos modi ipsam debitis maiores tempore rerum?',
                'precio':'precio',
                'uri':'uri'
            },
            {
                'nombre':'nombre',
                'precio':'precio',
                'descripcion':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit nobis ex sed repudiandae neque asperiores nesciunt, dolore unde nam ut, harum, nostrum labore eos modi ipsam debitis maiores tempore rerum?',
                'precio':'precio',
                'uri':'uri'
            }
        ]
    }
    return render(request, 'products.html',context)

def clothes(request):
    context={
        'titulo':'Ropa',
        'productos':[
            {
                'nombre':'nombre',
                'precio':'precio',
                'descripcion':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit nobis ex sed repudiandae neque asperiores nesciunt, dolore unde nam ut, harum, nostrum labore eos modi ipsam debitis maiores tempore rerum?',
                'precio':'precio',
                'uri':'uri'
            },
            {
                'nombre':'nombre',
                'precio':'precio',
                'descripcion':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit nobis ex sed repudiandae neque asperiores nesciunt, dolore unde nam ut, harum, nostrum labore eos modi ipsam debitis maiores tempore rerum?',
                'precio':'precio',
                'uri':'uri'
            },
            {
                'nombre':'nombre',
                'precio':'precio',
                'descripcion':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit nobis ex sed repudiandae neque asperiores nesciunt, dolore unde nam ut, harum, nostrum labore eos modi ipsam debitis maiores tempore rerum?',
                'precio':'precio',
                'uri':'uri'
            }
        ]
    }
    return render(request, 'products.html',context)