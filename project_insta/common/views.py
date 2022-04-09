from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserChangeForm, UserCreationForm

from django.urls import reverse


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()


            username = form.cleaned_data.get('username')

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인

            return redirect(reverse('insta:allPhotoAB'))
    else:
        form = UserChangeForm()


    return render(request, 'common/signup.html', {'form': form})









# from django.contrib.auth import get_user_model
#
# def authenticate(self, request, username=None, password=None, **kwargs):
#     UserModel = get_user_model()
#     user_field = UserModel.USERNAME_FIELD
#     if username is None:
#         username = kwargs.get(UserModel.USERNAME_FIELD)
#
#     try:
#         case_insensitive_username_field = '{}__iexact'.format(UserModel.USERNAME_FIELD)
#         user = UserModel._default_manager.get(
#             Q((f'{user_field}__iexact', username)) | Q(username__iexact=username)
#         )
#     except UserModel.DoesNotExist:
#         UserModel().set_password(password)
#
#     else:
#
#         if user.check_password(password) and self.user_can_authenticate(user):
#             return user
#
#
#
