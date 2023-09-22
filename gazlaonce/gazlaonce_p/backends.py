from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class MyCustomBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Özel kimlik doğrulama mantığınızı burada uygulayın
        User = get_user_model()
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
