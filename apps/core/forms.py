from django import forms
from .models import ContactMessage

INPUT_CLASS = (
    "w-full px-4 py-3 rounded-xl border border-gray-200 dark:border-gray-700 "
    "bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 "
    "focus:ring-2 focus:ring-teal-500 focus:border-transparent outline-none "
    "transition-all duration-200"
)


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your full name", "class": INPUT_CLASS}),
            "email": forms.EmailInput(attrs={"placeholder": "your@email.com", "class": INPUT_CLASS}),
            "subject": forms.TextInput(attrs={"placeholder": "What's this about?", "class": INPUT_CLASS}),
            "message": forms.Textarea(attrs={
                "rows": 6,
                "placeholder": "Tell us how we can help you...",
                "class": INPUT_CLASS + " resize-none",
            }),
        }
