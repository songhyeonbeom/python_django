from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.urls import reverse


class UserManager(BaseUserManager):
    def create_user(self, username, email, realname, birth_date, gender, phone, gender2, password=None):
        if not username:
            raise ValueError("이름이 있어야된다!")
        if not email:
            raise ValueError("이메일이 있어야된다!")
        if not password:
            raise ValueError("비밀번호 안넣을꺼니!")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            realname=realname,
            birth_date=birth_date,
            gender=gender,
            phone=phone,
            gender2=gender2,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user2(self, username, email, password=None):
        if not username:
            raise ValueError("이름이 있어야된다!")
        if not email:
            raise ValueError("이메일이 있어야된다!")
        if not password:
            raise ValueError("비밀번호 안넣을꺼니!")

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user2(
            username,
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(verbose_name='username', max_length=20, unique=True, )
    email = models.EmailField(verbose_name='email', max_length=255, )
    realname = models.CharField(verbose_name='realname', max_length=20, null=True,)
    birth_date = models.DateField(verbose_name='birth_date', blank=True, null=True, )
    phone = models.CharField(verbose_name='phone', max_length=11, null=True,)
    gender = models.IntegerField(verbose_name='gender', null=True,)
    gender2 = models.CharField(verbose_name="gender2", max_length=5, null=True,)


    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_absolute_url(self):
        return reverse('insta:photo_detail', args = [self.id])


    @property
    def is_staff(self):
        return self.is_admin

