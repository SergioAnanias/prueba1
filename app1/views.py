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
                'nombre':'Robot',
                'precio':'45990',
                'descripcion':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit nobis ex sed repudiandae neque asperiores nesciunt, dolore unde nam ut, harum, nostrum labore eos modi ipsam debitis maiores tempore rerum?',
                'uri':'img/juguete1.webp'
            },
            {
                'nombre':'Restaurant',
                'precio':'30990',
                'descripcion':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit nobis ex sed repudiandae neque asperiores nesciunt, dolore unde nam ut, harum, nostrum labore eos modi ipsam debitis maiores tempore rerum?',
                'uri':'img/juguete2.webp'
            },
            {
                'nombre':'Castillo',
                'precio':'10990',
                'descripcion':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit nobis ex sed repudiandae neque asperiores nesciunt, dolore unde nam ut, harum, nostrum labore eos modi ipsam debitis maiores tempore rerum?',
                'uri':'img/juguete3.webp'
            }
        ]
    }
    return render(request, 'products.html',context)

def clothes(request):
    context={
        'titulo':'Ropa',
        'productos':[
            {
                'nombre':'Poleron Standard',
                'precio':'10990',
                'descripcion':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit nobis ex sed repudiandae neque asperiores nesciunt, dolore unde nam ut, harum, nostrum labore eos modi ipsam debitis maiores tempore rerum?',
                'uri':'img/ropa1.jfif'
            },
            {
                'nombre':'Poleron Friends',
                'precio':'15990',
                'descripcion':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit nobis ex sed repudiandae neque asperiores nesciunt, dolore unde nam ut, harum, nostrum labore eos modi ipsam debitis maiores tempore rerum?',
                'uri':'img/ropa2.jfif'
            },
            {
                'nombre':'Poleron Tommy Hilfigel',
                'precio':'14990',
                'descripcion':'Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit nobis ex sed repudiandae neque asperiores nesciunt, dolore unde nam ut, harum, nostrum labore eos modi ipsam debitis maiores tempore rerum?',
                'uri':'img/ropa3.jfif'
            }
        ]
    }
    return render(request, 'products.html',context)