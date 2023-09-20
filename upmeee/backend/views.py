from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import FAQ, FAQCategory, Review, Portfolio, PortfolioCategory, TeamMember, Client,Blog
from django.core.mail import send_mail
from contact.models import ContactFormSubmission, LeadSubmission
#from blog.models import Blog




def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        project_summary = request.POST['project_summary']
        budget = request.POST['budget']

        # Create and save a new ContactFormSubmission object
        submission = ContactFormSubmission(
            name=name,
            email=email,
            phone_number=phone_number,
            project_summary=project_summary,
            budget=budget,
            submission_date=timezone.now()  # Use the current date and time
        )
        submission.save()

        subject = 'New Contact Form Submission'
        message = f'''
                Name: {name}
                Email: {email}
                Phone Number: {phone_number}
                Project Summary: {project_summary}
                Budget: {budget}
                Submission Date: {submission.submission_date}
                '''
        from_email = 'whatznotall@gmail.com'  # Use the same email address as in your settings
        recipient_list = ['whatznotall@gmail.com']  # Replace with your recipient email address
        send_mail(subject, message, from_email, recipient_list)

        # Redirect to a thank you page or any other page as needed
        return redirect('thankyou')
    teamMember = TeamMember.objects.all()
    client = Client.objects.all()
    review = Review.objects.all()
    blogs = Blog.objects.all()
    blogs = [blog for blog in blogs][:3]
    portfolio = Portfolio.objects.filter(is_featured=True)

    context = {
        'teamMember': teamMember,
        'client': client,
        'review': review,
        'blogs': blogs,
        'portfolio': portfolio,

    }
    return render(request, 'backend/index.html', context)


def about(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        project_summary = request.POST['project_summary']
        budget = request.POST['budget']

        # Create and save a new ContactFormSubmission object
        submission = ContactFormSubmission(
            name=name,
            email=email,
            phone_number=phone_number,
            project_summary=project_summary,
            budget=budget,
            submission_date=timezone.now()  # Use the current date and time
        )
        submission.save()

        subject = 'New Contact Form Submission'
        message = f'''
                Name: {name}
                Email: {email}
                Phone Number: {phone_number}
                Project Summary: {project_summary}
                Budget: {budget}
                Submission Date: {submission.submission_date}
                '''
        from_email = 'whatznotall@gmail.com'  # Use the same email address as in your settings
        recipient_list = ['whatznotall@gmail.com']  # Replace with your recipient email address
        send_mail(subject, message, from_email, recipient_list)

        # Redirect to a thank you page or any other page as needed
        return redirect('thankyou')
    current_page = 'about'
    teamMember = TeamMember.objects.all()
    client = Client.objects.all()
    review = Review.objects.all()[4:]
    context = {
        'teamMember': teamMember,
        'current_page': current_page,
        'client': client,
        'review': review,

    }

    return render(request, 'backend/about-us.html', context)


def why(request):
    client = Client.objects.all()
    current_page = 'why'
    review = Review.objects.all()[7:]
    featured_reviews = Review.objects.filter(has_features=True)
    context = {
        'current_page': current_page,
        'client': client,
        'review': review,
        'freviews': featured_reviews,

    }
    return render(request, 'backend/why-choice-us.html', context)


def reviews(request):
    current_page = 'reviews'
    reviews = Review.objects.all()  # Fetch all reviews from the database
    featured_reviews = Review.objects.filter(has_features=True)
    client = Client.objects.all()
    review = Review.objects.all()[6:]
    context = {
        'reviews': reviews,
        'current_page': current_page,  # Add the current_page to the context here
        'freviews': featured_reviews,
        'client': client,
        'review': review,
    }
    return render(request, 'backend/reviews.html', context)


def faqs(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        project_summary = request.POST['project_summary']
        budget = request.POST['budget']

        # Create and save a new ContactFormSubmission object
        submission = ContactFormSubmission(
            name=name,
            email=email,
            phone_number=phone_number,
            project_summary=project_summary,
            budget=budget,
            submission_date=timezone.now()  # Use the current date and time
        )
        submission.save()

        subject = 'New Contact Form Submission'
        message = f'''
                Name: {name}
                Email: {email}
                Phone Number: {phone_number}
                Project Summary: {project_summary}
                Budget: {budget}
                Submission Date: {submission.submission_date}
                '''
        from_email = 'whatznotall@gmail.com'  # Use the same email address as in your settings
        recipient_list = ['whatznotall@gmail.com']  # Replace with your recipient email address
        send_mail(subject, message, from_email, recipient_list)

        # Redirect to a thank you page or any other page as needed
        return redirect('thankyou')
    current_page = 'faqs'
    categories = FAQCategory.objects.all()
    faqs = FAQ.objects.all()
    blogs = Blog.objects.all()
    blogs = [blog for blog in blogs][:3]
    context = {
        'categories': categories,
        'faqs': faqs,
        'blogs': blogs,
        'current_page': current_page,  # Add the current_page to the context here
    }
    return render(request, 'backend/faq.html', context)


def services(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        project_summary = request.POST['project_summary']
        budget = request.POST['budget']

        # Create and save a new ContactFormSubmission object
        submission = ContactFormSubmission(
            name=name,
            email=email,
            phone_number=phone_number,
            project_summary=project_summary,
            budget=budget,
            submission_date=timezone.now()  # Use the current date and time
        )
        submission.save()

        subject = 'New Contact Form Submission'
        message = f'''
                Name: {name}
                Email: {email}
                Phone Number: {phone_number}
                Project Summary: {project_summary}
                Budget: {budget}
                Submission Date: {submission.submission_date}
                '''
        from_email = 'whatznotall@gmail.com'  # Use the same email address as in your settings
        recipient_list = ['whatznotall@gmail.com']  # Replace with your recipient email address
        send_mail(subject, message, from_email, recipient_list)

        # Redirect to a thank you page or any other page as needed
        return redirect('thankyou')
    current_page = 'services'
    client = Client.objects.all()
    review = Review.objects.all()
    portfolio = Portfolio.objects.filter(is_featured=True)

    context = {
        'current_page': current_page,
        'client': client,
        'review': review,
        'portfolio': portfolio,

    }
    return render(request, 'backend/services.html', context)


def webservices(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']

        budget = request.POST['budget']

        # Create and save a new ContactFormSubmission object
        submission = LeadSubmission(

            phone_number=phone_number,

            budget=budget,
            submission_date=timezone.now()  # Use the current date and time
        )
        submission.save()

        subject = 'New Contact Form Submission'
        message = f'''

                Phone Number: {phone_number}

                Budget: {budget}
                Submission Date: {submission.submission_date}
                '''
        from_email = 'whatznotall@gmail.com'  # Use the same email address as in your settings
        recipient_list = ['whatznotall@gmail.com']  # Replace with your recipient email address
        send_mail(subject, message, from_email, recipient_list)

        # Redirect to a thank you page or any other page as needed
        return redirect('thankyou')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        project_summary = request.POST['project_summary']
        budget = request.POST['budget']

        # Create and save a new ContactFormSubmission object
        submission = ContactFormSubmission(
            name=name,
            email=email,
            phone_number=phone_number,
            project_summary=project_summary,
            budget=budget,
            submission_date=timezone.now()  # Use the current date and time
        )
        submission.save()

        subject = 'New Contact Form Submission'
        message = f'''
                Name: {name}
                Email: {email}
                Phone Number: {phone_number}
                Project Summary: {project_summary}
                Budget: {budget}
                Submission Date: {submission.submission_date}
                '''
        from_email = 'whatznotall@gmail.com'  # Use the same email address as in your settings
        recipient_list = ['whatznotall@gmail.com']  # Replace with your recipient email address
        send_mail(subject, message, from_email, recipient_list)

        # Redirect to a thank you page or any other page as needed
        return redirect('thankyou')

    current_page = 'webservices'
    client = Client.objects.all()
    teamMember = TeamMember.objects.all()
    review = Review.objects.all()
    blogs = Blog.objects.all()
    blogs = [blog for blog in blogs][:3]
    desired_categories = ['Website ' ,]

    # Filter the Portfolio objects based on the desired categories
    filtered_portfolio = Portfolio.objects.filter(category__name__in=desired_categories, is_featured=True)
    context = {
        'teamMember': teamMember,
        'current_page': current_page,
        'review': review,
        'client': client,
        'blogs': blogs,
        'portfolio': filtered_portfolio,

    }
    return render(request, 'backend/webservicesdetails.html', context)


def mobileservices(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']

        budget = request.POST['budget']

        # Create and save a new ContactFormSubmission object
        submission = LeadSubmission(

            phone_number=phone_number,

            budget=budget,
            submission_date=timezone.now()  # Use the current date and time
        )
        submission.save()

        subject = 'New Contact Form Submission'
        message = f'''

                Phone Number: {phone_number}

                Budget: {budget}
                Submission Date: {submission.submission_date}
                '''
        from_email = 'whatznotall@gmail.com'  # Use the same email address as in your settings
        recipient_list = ['whatznotall@gmail.com']  # Replace with your recipient email address
        send_mail(subject, message, from_email, recipient_list)

        # Redirect to a thank you page or any other page as needed
        return redirect('thankyou')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        project_summary = request.POST['project_summary']
        budget = request.POST['budget']

        # Create and save a new ContactFormSubmission object
        submission = ContactFormSubmission(
            name=name,
            email=email,
            phone_number=phone_number,
            project_summary=project_summary,
            budget=budget,
            submission_date=timezone.now()  # Use the current date and time
        )
        submission.save()

        subject = 'New Contact Form Submission'
        message = f'''
                Name: {name}
                Email: {email}
                Phone Number: {phone_number}
                Project Summary: {project_summary}
                Budget: {budget}
                Submission Date: {submission.submission_date}
                '''
        from_email = 'whatznotall@gmail.com'  # Use the same email address as in your settings
        recipient_list = ['whatznotall@gmail.com']  # Replace with your recipient email address
        send_mail(subject, message, from_email, recipient_list)

        # Redirect to a thank you page or any other page as needed
        return redirect('thankyou')
    current_page = 'mobileservices'
    teamMember = TeamMember.objects.all()
    client = Client.objects.all()
    review = Review.objects.all()
    blogs = Blog.objects.all()
    blogs = [blog for blog in blogs][:3]

    desired_categories = ['Mobile App',]

    # Filter the Portfolio objects based on the desired categories
    filtered_portfolio = Portfolio.objects.filter(category__name__in=desired_categories, is_featured=True)
    context = {
        'teamMember': teamMember,
        'current_page': current_page,
        'review': review,
        'client': client,
        'blogs': blogs,
        'portfolio': filtered_portfolio,

    }

    return render(request, 'backend/mobileservicesdetails.html', context)


def UIUX(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']

        budget = request.POST['budget']

        # Create and save a new ContactFormSubmission object
        submission = LeadSubmission(

            phone_number=phone_number,

            budget=budget,
            submission_date=timezone.now()  # Use the current date and time
        )
        submission.save()

        subject = 'New Contact Form Submission'
        message = f'''

                Phone Number: {phone_number}

                Budget: {budget}
                Submission Date: {submission.submission_date}
                '''
        from_email = 'whatznotall@gmail.com'  # Use the same email address as in your settings
        recipient_list = ['whatznotall@gmail.com']  # Replace with your recipient email address
        send_mail(subject, message, from_email, recipient_list)

        # Redirect to a thank you page or any other page as needed
        return redirect('thankyou')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        project_summary = request.POST['project_summary']
        budget = request.POST['budget']

        # Create and save a new ContactFormSubmission object
        submission = ContactFormSubmission(
            name=name,
            email=email,
            phone_number=phone_number,
            project_summary=project_summary,
            budget=budget,
            submission_date=timezone.now()  # Use the current date and time
        )
        submission.save()

        subject = 'New Contact Form Submission'
        message = f'''
                Name: {name}
                Email: {email}
                Phone Number: {phone_number}
                Project Summary: {project_summary}
                Budget: {budget}
                Submission Date: {submission.submission_date}
                '''
        from_email = 'whatznotall@gmail.com'  # Use the same email address as in your settings
        recipient_list = ['whatznotall@gmail.com']  # Replace with your recipient email address
        send_mail(subject, message, from_email, recipient_list)

        # Redirect to a thank you page or any other page as needed
        return redirect('thankyou')
    current_page = 'UIUX'
    teamMember = TeamMember.objects.all()
    client = Client.objects.all()
    review = Review.objects.all()
    blogs = Blog.objects.all()
    blogs = [blog for blog in blogs][:3]

    desired_categories = ['Graphic',]

    # Filter the Portfolio objects based on the desired categories
    filtered_portfolio = Portfolio.objects.filter(category__name__in=desired_categories, is_featured=True)
    context = {
        'teamMember': teamMember,
        'current_page': current_page,
        'review': review,
        'client': client,
        'blogs': blogs,
        'portfolio': filtered_portfolio,

    }

    return render(request, 'backend/UIUXdetails.html', context)


def all_portfolios(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        project_summary = request.POST['project_summary']
        budget = request.POST['budget']

        # Create and save a new ContactFormSubmission object
        submission = ContactFormSubmission(
            name=name,
            email=email,
            phone_number=phone_number,
            project_summary=project_summary,
            budget=budget,
            submission_date=timezone.now()  # Use the current date and time
        )
        submission.save()

        subject = 'New Contact Form Submission'
        message = f'''
                Name: {name}
                Email: {email}
                Phone Number: {phone_number}
                Project Summary: {project_summary}
                Budget: {budget}
                Submission Date: {submission.submission_date}
                '''
        from_email = 'whatznotall@gmail.com'  # Use the same email address as in your settings
        recipient_list = ['whatznotall@gmail.com']  # Replace with your recipient email address
        send_mail(subject, message, from_email, recipient_list)

        # Redirect to a thank you page or any other page as needed
        return redirect('thankyou')
    current_page = 'portfolios'
    # Fetch all portfolio categories from the database
    portfolio_categories = PortfolioCategory.objects.all()
    portfolio = Portfolio.objects.all()
    client = Client.objects.all()
    review = Review.objects.all()

    context = {
        'portfolio_categories': portfolio_categories,
        'portfolio': portfolio,
        'current_page': current_page,
        'client': client,
        'review': review,
    }

    return render(request, 'backend/portfolios.html', context)


def portfolio_detail(request, slug):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        project_summary = request.POST['project_summary']
        budget = request.POST['budget']

        # Create and save a new ContactFormSubmission object
        submission = ContactFormSubmission(
            name=name,
            email=email,
            phone_number=phone_number,
            project_summary=project_summary,
            budget=budget,
            submission_date=timezone.now()  # Use the current date and time
        )
        submission.save()

        subject = 'New Contact Form Submission'
        message = f'''
                Name: {name}
                Email: {email}
                Phone Number: {phone_number}
                Project Summary: {project_summary}
                Budget: {budget}
                Submission Date: {submission.submission_date}
                '''
        from_email = 'whatznotall@gmail.com'  # Use the same email address as in your settings
        recipient_list = ['whatznotall@gmail.com']  # Replace with your recipient email address
        send_mail(subject, message, from_email, recipient_list)

        # Redirect to a thank you page or any other page as needed
        return redirect('thankyou')
    current_page = 'portfolios'
    # Retrieve the portfolio based on the slug or return a 404 error if not found
    portfolio = get_object_or_404(Portfolio, slug=slug)
    related_portfolios = Portfolio.objects.filter(
        category__in=portfolio.category.all()  # Assuming the category field is a ManyToMany relationship
    ).exclude(slug=slug)[:3]  # Exclude the current portfolio and limit to 3 related portfolios
    next_portfolio = Portfolio.objects.filter(
        id__gt=portfolio.id  # Get portfolios with IDs greater than the current portfolio's ID
    ).order_by('id').first()  # Order them by ID and get the first one

    review = Review.objects.all()  # Fetch all reviews from the database
    client = Client.objects.all()
    fportfolio = Portfolio.objects.filter(is_featured=True)
    context = {
        'portfolio': portfolio,
        'review': review,
        'related_portfolios': related_portfolios,
        'current_page': current_page,
        'client': client,
        'next_portfolio': next_portfolio,
        'fportfolio': fportfolio,
    }

    return render(request, 'backend/portfolio-details.html', context)


def terms(request):
    return render(request, 'backend/terms-and-conditions.html')


def privacy(request):
    return render(request, 'backend/privacy-policy.html')


def refund(request):
    return render(request, 'backend/refund-policy.html')
