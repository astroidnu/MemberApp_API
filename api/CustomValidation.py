from tastypie.validation import Validation
from api.models import Member

class CustomValidation(Validation):
     def is_valid(self, bundle, request=None):
        if not bundle.data:
            return {'__all__': 'Missing data, please include CompanyName, CompanyId, Contact, Email, and Phone.'}

        errors = {}
        user_id=bundle.data.get('userid', None)
        # manager method, returns true if the company exists, false otherwise
        if Member.objects.filter(userid=user_id):
            errors['error_message']='Duplicate UserID, UserID %s already exists.' % user_id
            errors['error_code']=1
        return errors
