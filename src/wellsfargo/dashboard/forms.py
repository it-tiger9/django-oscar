from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from oscar.forms.widgets import DatePickerInput, DateTimePickerInput
from .widgets import FuzzyDurationWidget, BooleanSelect
from ..core.constants import (
    US, CA,
    INDIVIDUAL, JOINT,
    LOCALES,
    APP_TYPES, LANGUAGES, REGIONS
)
from ..models import (
    FinancingPlan,
    FinancingPlanBenefit,
    USCreditApp,
    USJointCreditApp,
    CACreditApp,
    CAJointCreditApp
)

WIDGETS = {
    'main_date_of_birth': DatePickerInput(),
    'joint_date_of_birth': DatePickerInput(),
    'main_photo_id_expiration': DatePickerInput(),
    'joint_photo_id_expiration': DatePickerInput(),
    'main_time_at_address': FuzzyDurationWidget(),
    'main_time_at_employer': FuzzyDurationWidget(),
    'joint_time_at_employer': FuzzyDurationWidget(),
    'insurance': BooleanSelect(),
}


class ApplicationSelectionForm(forms.Form):
    region = forms.ChoiceField(label=_("Region"), required=True, choices=REGIONS)
    language = forms.ChoiceField(label=_("Language"), required=True, choices=LANGUAGES)
    app_type = forms.ChoiceField(label=_('Application Type'), required=True, choices=APP_TYPES)

    def clean_language(self):
        region = self.cleaned_data['region']
        language = self.cleaned_data['language']
        locale = LOCALES.get(region, {}).get(language)
        if not locale:
            msg = _('Selected language is not valid for the selected region.')
            raise ValidationError(msg)
        return language


class BaseCreditAppFormMixin(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['region'].disabled = True
        self.fields['language'].disabled = True
        self.fields['app_type'].disabled = True


class USCreditAppForm(BaseCreditAppFormMixin, forms.ModelForm):
    dashboard_template = 'wfrs/dashboard/application_us_single.html'

    class Meta:
        model = USCreditApp
        widgets = WIDGETS
        fields = '__all__'


class USJointCreditAppForm(BaseCreditAppFormMixin, forms.ModelForm):
    dashboard_template = 'wfrs/dashboard/application_us_joint.html'

    class Meta:
        model = USJointCreditApp
        widgets = WIDGETS
        fields = '__all__'


class CACreditAppForm(BaseCreditAppFormMixin, forms.ModelForm):
    dashboard_template = 'wfrs/dashboard/application_ca_single.html'

    class Meta:
        model = CACreditApp
        widgets = WIDGETS
        fields = '__all__'


class CAJointCreditAppForm(BaseCreditAppFormMixin, forms.ModelForm):
    dashboard_template = 'wfrs/dashboard/application_ca_joint.html'

    class Meta:
        model = CAJointCreditApp
        widgets = WIDGETS
        fields = '__all__'


class FinancingPlanForm(forms.ModelForm):
    class Meta:
        model = FinancingPlan
        fields = ('plan_number', 'description', 'apr', 'term_months', 'is_default_plan', 'allow_credit_application')


class FinancingPlanBenefitForm(forms.ModelForm):
    CPATH = '%s.%s' % (FinancingPlanBenefit.__module__, FinancingPlanBenefit.__name__)
    proxy_class = forms.ChoiceField(
        choices=(
            (CPATH, _('Wells Fargo Financing Plan Group')),
        ),
        disabled=True,
        initial=CPATH,
        label=_('Benefit Type'))

    class Meta:
        model = FinancingPlanBenefit
        fields = ('proxy_class', 'group_name', 'plans')


class ApplicationSearchForm(forms.Form):
    # Basic Search
    search_text = forms.CharField(required=False, label="Search")

    # Advanced Search
    name = forms.CharField(required=False, label="Applicant Name")
    email = forms.CharField(required=False, label="Applicant Email Address")
    address = forms.CharField(required=False, label="Applicant Address")
    phone = forms.CharField(required=False, label="Applicant Phone Number")
    created_date_from = forms.DateTimeField(required=False, label=_("Submitted After"), widget=DateTimePickerInput)
    created_date_to = forms.DateTimeField(required=False, label=_("Submitted Before"), widget=DateTimePickerInput)
    submitted_by = forms.CharField(required=False, label="Submitted By")

    # Hidden filters linked to by other parts of the application
    user_id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    submitting_user_id = forms.IntegerField(required=False, widget=forms.HiddenInput())


def get_application_form_class(region, app_type):
    classes = {
        US: {
            INDIVIDUAL: USCreditAppForm,
            JOINT: USJointCreditAppForm,
        },
        CA: {
            INDIVIDUAL: CACreditAppForm,
            JOINT: CAJointCreditAppForm,
        },
    }
    return classes.get(region, {}).get(app_type)