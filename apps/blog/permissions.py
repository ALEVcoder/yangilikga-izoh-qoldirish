from django.contrib.auth.mixins import AccessMixin

class FriendRequiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.is_friend==False:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)