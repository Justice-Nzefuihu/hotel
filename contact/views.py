from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':

        fname = request.POST['firstName']
        lname = request.POST['lastName']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['message']

        if fname == '':
            messages.error(request, 'Please enter your first name')
            return redirect('contact')
        
        saveContact = Contact(firstname=fname, lastname=lname, email=email, phone=phone, message=msg)
        saveContact.save()
        messages.success(request, 'Your message has been received')
        return redirect('contact')
    else:
        return render(request, 'contact/contact.html')