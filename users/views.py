from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *


def logins(request):
    error = False
    massage= ""
    context ={ }

    if request.method== "POST":        
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)

        user = User.objects.filter(email = email).first()

        if user:
            auth_user =authenticate(username = user.username, password=password)
            if auth_user:
                login (request, auth_user)
                return redirect('homes')
            else:
                error = True 
                massage="the password is incorrect!"
        else:
            error=True 
            massage="user does not exist!"

        #print("=="*5 , "new post ", email, password, "=="*5)

    context ={
    'error':error,
    'message': massage
        }

    return render(request, "login.html", context)



#fonction qui gere la connection 
def signup(request):
    error = False
    massage= ""
    context ={ }

    langues = Langue.objects.all()

#icic on verifie si les données ont été bien envoyé et on les enregistre dans des variables 
    if request.method== "POST":
        noms = request.POST.get("nom", None)
        prenoms = request.POST.get("prenoms", None)
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        confirmPass = request.POST.get("confirmPass", None)
        lang = request.POST.get("lang")


# ici on verifie la validité de l'email
        try:
            validate_email(email)
        except:
            error =True
            massage = "entrer un email valide !"

#ici on verifie que les mots de passes sont identique
        if error != True:
            if password != confirmPass:
                error = True
                massage = "les deux mots de passes sont different; veillez entrer les memes mots de passe"

#ici on verifie la taille du mot de passe
            elif len(password) < 8:
                error = True
                massage = "mot de passe trop court ! Le mot de passe doit avoir au moins 8 caractères"

# ici on verifie si l'utilisateur existe deja         
        user = User.objects.filter(email=email).first()

        if user:
            error = True
            massage = f"Un compte existe deja avec l'email {email}!"

#ici on enregistre les données dans la bd
        if error ==False:
            user = User(
                username = noms,
                email=email,
                first_name= prenoms,
                last_name = noms,
                is_active = True,
            )


            user.save()
#on enregistre le mot de passe
            user.password= password
            user.set_password(user.password)
            user.save()

#on enregistre la langue
            usr= User.objects.filter(email=email).first()
            idU= usr.id
            
            print('teste', idU)
            userln = UserLangue(
                users_id = idU,
                langue_id = lang
            )
            userln.save()


        return redirect('homes')
            #print("=="*5 , "new post ", noms,email, password, confirmPass, "=="*5)
           
        
            
            
         

    return render(request,"signup.html",{'langues':langues,'error':error,'message': massage})


def logout_view (request):
    logout(request)
    return redirect("/")

@login_required(login_url='login')
def homeStud (request):
    langues = Langue.objects.all()
    return render(request, "dashboard_Apprenant.html", {'langues':langues})

# Create your views here.
