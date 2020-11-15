from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Contact
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        realtor_email = request.POST['realtor_email']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        user_id = request.POST['user_id']

        #check if user has made inquiry for this post
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have inquired about this listing already')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing_id=listing_id, listing=listing, realtor_email=realtor_email, name=name, phone=phone,email=email, user_id=user_id,message=message)
        contact.save()

        #send mail
        send_mail(
            'Property Inquiry',
            'Listing Inquiry for property ' + listing + '. Please login to the Admin area.',
            'TEST.BTRE.JON@gmail.com',
            [realtor_email, 'test.btre.jon@gmail.com'],
            fail_silently = False
        )

        messages.success(request, 'Your inquiry has been saved and passed along to our realtors')
        return redirect('/listings/'+listing_id)