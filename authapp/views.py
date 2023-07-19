import sendgrid as sendgrid
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.template.backends.django import Template
from sendgrid import Email, To, Mail, Content
from django.template.loader import get_template
# from AmGFitness.settings import SENDGRID_API_KEY
from authapp.models import MembershipPlan, Trainer, Enrollment


# Create your views here.

def Home(request):
    return render(request, "index.html")


def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login and Try Again")
        return redirect('/login')
    user = request.user
    posts = Enrollment.objects.filter(user=user)
    context = {"posts": posts}
    return render(request, "profile.html", context)


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 != pass2:
            messages.info(request, "Password is not Matching")
            return redirect('/signup')
        try:
            if User.objects.get(username=username):
                messages.warning(request, "Username is Taken")
                return redirect('/signup')

        except Exception as identifier:
            pass

        try:
            if User.objects.get(email=email):
                messages.warning(request, "Email is Taken")
                return redirect('/signup')

        except Exception as identifier:
            pass

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        # sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
        # from_email = Email("beautywebdjango@gmail.com")
        # to_email = To(myuser.email)
        # subject = 'Felicitari! Ai un cont nou in aplicatie!'
        #
        # # Genereaza continutul e-mailului din template
        # content = Template.render(
        #     {'first_name': myuser.first_name, 'last_name': myuser.last_name, 'username': myuser.username})

        # Construieste obiectul Mail si adauga continutul
        # mail = Mail(from_email, to_email, subject)
        # mail.add_content(Content("text/html", "Helllooo!!!!"))

        # Trimite e-mailul
        # sg.client.mail.send.post(request_body=mail.get())

    # return redirect('/login')

    # Incarca template-ul e-mailului
    # context = {'user': myuser}
    # content = render_to_string('mail.html', context)

    # messages.success(request, "User is Created Please Login")
    # return redirect('/login')

    return render(request, "signup.html")


def handlelogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        myuser = authenticate(username=username, password=pass1)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Successful")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/login')

    return render(request, "hendlelogin.html")


def handleLogout(request):
    logout(request)
    messages.success(request, "Logout Success")
    return redirect('/login')


def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please Login and Try Again")
        return redirect('/login')

    Membership = MembershipPlan.objects.all()
    SelectTrainer = Trainer.objects.all()
    context = {"Membership": Membership, "SelectTrainer": SelectTrainer}
    if request.method == "POST":
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        member = request.POST.get('member')
        trainer = request.POST.get('trainer')
        address = request.POST.get('address')
        query = Enrollment(user=request.user, Email=email, Gender=gender,
                           SelectMembershipplan=member, SelectTrainer=trainer, Address=address,
                           )
        query.save()
        messages.success(request, "Thanks for enrollment")
        return redirect('/join')

    return render(request, "enroll.html", context)
