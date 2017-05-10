

class SuperuserAccessor(object):

    def allow_access(self, request):
        return request.user.is_superuser
