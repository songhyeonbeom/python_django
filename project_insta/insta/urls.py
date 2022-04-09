from django.urls import path
from insta import views, vote_views





app_name = 'insta'
urlpatterns = [


    path('', views.allPhotoAB, name='allPhotoAB'),

    path('myPhotoAB/', views.myPhotoAB, name='myPhotoAB'),
    # path('<slug:c_slug>/', views.myPhotoAB, name='myPhotoAB'),

    path('<slug:c_slug>/', views.allPhotoAB, name='album_detail'),

    path('photo/<int:pk>/', views.PhotoDV.as_view(), name='photo_detail'),

    path('vote/photo/<int:photo_id>/', vote_views.vote_photo, name='vote_photo'),

    path('answer/create/<int:photo_id>/', vote_views.answer_create, name='answer_create'),

    path('photo/modify/<int:photo_id>/', vote_views.photo_modify, name='photo_modify'),
    path('photo/delete/<int:photo_id>/', vote_views.photo_delete, name='photo_delete'),

    path('answer/modify/<int:answer_id>/', vote_views.answer_modify, name='answer_modify'),

    path('answer/delete/<int:answer_id>/', vote_views.answer_delete, name='answer_delete'),

    path('photo/add/', views.PhotoCV.as_view(), name='photo_add'),

    path('album/add/', views.AlbumPhotoCV.as_view(), name='album_add'),




    # path('<int:photo_id>/', views.detail, name='detail'),
    # # Example: /insta/album/add/
    # path('album/add/', views.AlbumPhotoCV.as_view(), name='album_add'),
    #
    # # Example: /insta/album/change/
    # path('album/change/', views.AlbumChangeLV.as_view(), name='album_change'),
    #
    # # Example: /insta/album/99/update/
    # path('album/<int:pk>/update/', views.AlbumPhotoUV.as_view(), name='album_update'),
    #
    # # Example: /insta/album/99/delete/
    # path('album/<int:pk>/delete/', views.AlbumDelV.as_view(), name='album_delete'),
    #
    # # Example: /insta/insta/add/
    # path('insta/add/', views.PhotoCV.as_view(), name='photo_add'),
    #
    # # Example: /insta/insta/change/
    # path('insta/change/', views.PhotoChangeLV.as_view(), name='photo_change'),
    #
    # # Example: /insta/insta/99/update/
    # path('insta/<int:pk>/update/', views.PhotoUV.as_view(), name='photo_update'),
    #
    # # Example: /insta/insta/99/delete/
    # path('insta/<int:pk>/delete/', views.PhotoDelV.as_view(), name='photo_delete'),

    # path('photo/<int:pk>/', views.PhotoDV, name='photo_detail'),

    # path('id:c_slug/id:photo_slug', views.PhotoABDetail, name = 'PhotoABDetail'),

    # path('vote/photo/<int:photo_id>/', vote_views.vote_photo, name='vote_photo'),
]



