from .models import Profile, Connection

def profile_pic(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        pic = profile_obj.avatar
        return {'picture':pic}
    return {}

def invatations_received_num(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        qs_count = Connection.objects.invatations_received(profile_obj).count()
        return {'invites_num':qs_count}
    return {}