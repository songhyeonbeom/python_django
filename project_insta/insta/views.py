import requests
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

import insta.models
from insta.forms import PhotoInlineFormSet
from django.shortcuts import render, get_object_or_404
from insta.models import Album, Photo
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from common.models import User











class PhotoCV(LoginRequiredMixin, CreateView, ):
    model = Photo

    login_url = '/common/login/'
    redirect_field_name = 'login'

    fields = ('album', 'image', 'description',)

    success_url = reverse_lazy('insta:allPhotoAB')


    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['album'].queryset = Album.objects.filter(owner=self.request.user)
        return context




class AlbumPhotoCV(LoginRequiredMixin, CreateView, ):
    model = Album

    login_url = '/common/login/'
    redirect_field_name = 'login'

    fields = ('name', 'slug',)
    success_url = reverse_lazy('insta:allPhotoAB')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = PhotoInlineFormSet()
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        context = self.get_context_data()
        formset = context['formset']
        for photoform in formset:
            photoform.instance.owner = self.request.user
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))






# # #(안되는거 지금 이리저리 만지는중인거)
# def myPhotoAB(request, c_slug=None):
#     c_page = None
#     allphoto = request.user.id
#     photos_list = Photo.objects.filter(owner_id=allphoto)
#     if c_slug != None:
#         print(c_slug, "444444444444444444")
#         c_page = get_object_or_404(Album, slug = c_slug)
#         photos_list = Photo.objects.filter(album = c_page).order_by('-upload_dt')
#
#     else:
#         print(c_slug, "333333333333333333")
#         photos_list = Photo.objects.order_by('-upload_dt')
#     paginator = Paginator(photos_list, 12)
#
#     try:
#         page = int(request.GET.get('page', 1))
#     except:
#         page = 1
#
#     try:
#         photos = paginator.page(page)
#     except(EmptyPage, InvalidPage):
#         photos = paginator.page(paginator.num_pages)
#
#     return render(request, 'insta/myalbum.html', {'album': c_page, 'photos': photos})



# (일단은 되긴한데 좀 이상한거)
def myPhotoAB(request, c_slug=None):
    c_page = None
    photos_list = None
    if c_slug != None:
        print(c_slug, "444444444444444444")
        c_page = get_object_or_404(Album, slug = c_slug)
        photos_list = Photo.objects.filter(album = c_page).order_by('-upload_dt')

    else:
        print(c_slug, "333333333333333333")
        photos_list = Photo.objects.order_by('-upload_dt')
    paginator = Paginator(photos_list, 12)

    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1

    try:
        photos = paginator.page(page)
    except(EmptyPage, InvalidPage):
        photos = paginator.page(paginator.num_pages)

    return render(request, 'insta/myalbum.html', {'album': c_page, 'photos': photos})



def allPhotoAB(request, c_slug=None):
    c_page = None
    photos_list = None
    if c_slug != None:
        print(request.GET)
        print(c_slug, "22222222222222")
        c_page = get_object_or_404(Album, slug = c_slug)
        photos_list = Photo.objects.filter(album = c_page).order_by('-upload_dt')

    else :
        print(c_slug, "111111111111111111")
        photos_list = Photo.objects.order_by('-upload_dt')
    paginator = Paginator(photos_list, 12)

    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1

    try:
        photos = paginator.page(page)
    except(EmptyPage, InvalidPage):
        photos = paginator.page(paginator.num_pages)

    return render(request, 'insta/album.html', {'album': c_page, 'photos': photos})









# def PhotoABDetail(request, c_slug, photo_slug):
#     try:
#         photo = Photo.objects.get(album__slug = c_slug, slug = photo_slug)
#     except Exception as e :
#         raise e
#
#     return render(request, 'insta/insta.html', {'insta' : photo})










class AlbumLV(ListView):
    model = Album


class AlbumDV(DetailView):
    model = Album

class PhotoDV(DetailView):
    model = Photo



class PhotoChangeLV(LoginRequiredMixin, ListView):
    model = Photo
    template_name = 'insta/photo_change_list.html'
    #매니져가 지정이 안되면 object_list

    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user)






# class PhotoUV(OwnerOnlyMixin, UpdateView):
#     model = Photo
#     fields = ('album', 'title', 'image', 'description')
#     success_url = reverse_lazy('insta:index')
#
#
# class PhotoDelV(OwnerOnlyMixin, DeleteView):
#     model = Photo
#     success_url = reverse_lazy('insta:index')




# #--- Change-list/Delete for Album
# class AlbumChangeLV(LoginRequiredMixin, ListView):
#     model = Album
#     template_name = 'insta/album_change_list.html'
#
#     def get_queryset(self):
#         return Album.objects.filter(owner=self.request.user)


# class AlbumPhotoUV(OwnerOnlyMixin, UpdateView):
#     model = Album
#     fields = ('name', 'description')
#     success_url = reverse_lazy('insta:index')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.request.POST:
#             context['formset'] = PhotoInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
#         else:
#             context['formset'] = PhotoInlineFormSet(instance=self.object)
#         return context
#
#     def form_valid(self, form):
#         context = self.get_context_data()
#         formset = context['formset']
#         if formset.is_valid():
#             self.object = form.save()
#             formset.instance = self.object
#             formset.save()
#             return redirect(self.get_success_url())
#         else:
#             return self.render_to_response(self.get_context_data(form=form))


# class AlbumDelV(OwnerOnlyMixin, DeleteView):
#     model = Album
#     success_url = reverse_lazy('insta:index')
























