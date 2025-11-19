from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Message, MessageHistory
from django.http import HttpResponse


@login_required
def send_message(request):
    if request.method == "POST":
        receiver_id = request.POST.get("receiver")
        content = request.POST.get("content")
        receiver = get_object_or_404(User, id=receiver_id)

        Message.objects.create(
            sender=request.user,
            receiver=receiver,
            content=content
        )
        return HttpResponse("Message sent")

    users = User.objects.exclude(id=request.user.id)
    return render(request, "messaging/send_message.html", {"users": users})


@login_required
def edit_message(request, message_id):
    msg = get_object_or_404(Message, id=message_id, sender=request.user)

    if request.method == "POST":
        msg.content = request.POST.get("content")
        msg.save()
        return HttpResponse("Message edited")

    return render(request, "messaging/edit_message.html", {"message": msg})


@login_required
def delete_user(request):
    """
    When the user deletes their account → Signal cleans messages + history
    """
    user = request.user
    user.delete()
    return HttpResponse("Your account and all related data were deleted successfully")


@login_required
def message_history(request, message_id):
    msg = get_object_or_404(Message, id=message_id, sender=request.user)
    history = msg.history.all()

    return render(request, "messaging/history.html", {"message": msg, "history": history})
