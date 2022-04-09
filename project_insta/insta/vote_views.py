from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from .forms import PhotoForm, AnswerForm
from .models import Photo, Answer



def answer_create(request, photo_id):
    """
    insta photo 답변등록
    """
    photo = get_object_or_404(Photo, pk=photo_id)
    answer_list = None
    if request.method == "POST":

        form = AnswerForm(request.POST)
        if form.is_valid():


            answer = form.save(commit=False)
            answer.owner = request.user  # author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.photo = photo
            answer.save()

            return redirect('{}#answer_{}'.format(
                resolve_url('insta:photo_detail', pk=photo.id), answer.id))

    else:
        form = AnswerForm()

    context = {'photo': photo, 'form': form}
    return render(request, 'insta/photo_detail.html', context)


def vote_photo(request, photo_id):
    """
    insta 사진추천등록
    """
    photo = get_object_or_404(Photo, pk=photo_id)
    if request.user == photo.owner:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        photo.voter.add(request.user)
    return redirect('insta:photo_detail', pk=photo.id)






@login_required(login_url='common:login')
def photo_modify(request, photo_id):
    """
    photo 게시물 수정
    """
    photo = get_object_or_404(Photo, pk=photo_id)
    if request.user != photo.owner:
        messages.error(request, '수정권한이 없습니다')
        return redirect('insta:photo_detail', pk=photo.id)

    if request.method == "POST":
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.modify_date = timezone.now()  # 수정일시 저장
            photo.save()
            return redirect('insta:photo_detail', pk=photo.id)
    else:
        form = PhotoForm(instance=photo)
    context = {'form': form}
    return render(request, 'insta/photo_form.html', context)


@login_required(login_url='common:login')
def photo_delete(request, photo_id):
    """
    photo 게시물 삭제
    """
    photo = get_object_or_404(Photo, pk=photo_id)
    if request.user != photo.owner:
        messages.error(request, '삭제권한이 없습니다.')
        return redirect('insta:photo_detail', pk=photo.id)
    photo.delete()
    return redirect('insta:allPhotoAB')



@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    """
    photo 댓글수정
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.owner:
        messages.error(request, '수정권한이 없습니다')
        return redirect('insta:photo_detail', photo_id=answer.photo.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('insta:photo_detail', pk=answer.photo.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'insta/answer_form.html', context)


def answer_delete(request, answer_id):
    """
    photo 댓글 삭제
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.owner:
        messages.error(request, '삭제권한이 없습니다.')
    else:
        answer.delete()
    return redirect('insta:photo_detail', photo_id=answer.photo.id)








# def detail(request, photo_id):
#     """
#     insta 내용 출력
#     """
#     photo = get_object_or_404(Photo, pk=photo_id)
#     context = {'photo': photo}
#     return render(request, 'insta/answer_detail.html', context)