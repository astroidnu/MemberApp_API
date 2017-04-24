from tastypie.resources import ModelResource
from api.models import Member
from tastypie.authorization import Authorization
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from api.CustomValidation import CustomValidation


class MemberResources(ModelResource):
    class Meta:
        queryset = Member.objects.all()
        resource_name = 'member'
        authorization = Authorization()
        validation = CustomValidation()
        fields = ['id','userid', 'fullname','dateofbirth','address']
        filtering = {
            "userid" : ('exact', 'startwith', 'contains'),
            "userid" : ALL,
        }
        allowed_methods = ('get', 'put', 'post', 'delete')
        include_resource_uri = False
        always_return_data = True
