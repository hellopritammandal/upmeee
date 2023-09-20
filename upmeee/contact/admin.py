from django.contrib import admin
from .models import ContactFormSubmission, LeadSubmission


class ContactFormSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'budget', 'submission_date')
    search_fields = ('name', 'phone_number', 'email')
    list_filter = ('budget', 'submission_date')
    list_per_page = 100

admin.site.register(ContactFormSubmission, ContactFormSubmissionAdmin)


class LeadSubmissionAdmin(admin.ModelAdmin):
    list_display = ('phone_number',  'budget','submission_date',)
    search_fields = ('phone_number',)
    list_filter = ('budget','submission_date',)
    list_per_page = 100


admin.site.register(LeadSubmission,LeadSubmissionAdmin )



