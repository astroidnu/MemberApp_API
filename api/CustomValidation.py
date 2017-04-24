from tastypie.validation import Validation
from api.models import Member

class CustomValidation(Validation):
     def is_valid(self, bundle, request=None):
        if not bundle.data:
            return {'__all__': 'Missing data, please include CompanyName, CompanyId, Contact, Email, and Phone.'}

        errors = {}
        company_id=bundle.data.get('userid', None)

        # manager method, returns true if the company exists, false otherwise
        if Member.objects.filter(userid=company_id):
            errors['userid']='Duplicate CompanyId, CompanyId %s already exists.' % company_id
        return errors
