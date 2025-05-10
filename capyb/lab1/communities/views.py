from django.views import View
from django.shortcuts import render, redirect
from .forms import CreateCommunity
from .models import Community
from django.contrib.auth.mixins import LoginRequiredMixin

def communities_list(request):
    communities = Community.objects.all().order_by('-id')
    return render(request, 'communities/communities_list.html', {'communities': communities})

def community_page(request, slug):
    community = Community.objects.get(slug=slug)
    return render(request, 'communities/community_page.html', {'community': community})

class CommunityCreateView(LoginRequiredMixin, View):  
    login_url = '/users/login/'  

    def get(self, request):
        form = CreateCommunity()
        return render(request, 'communities/community_new.html', {'form': form})

    def post(self, request):
        form = CreateCommunity(request.POST, request.FILES)
        if form.is_valid():
            new_community = form.save(commit=False)
            new_community.save()
            return redirect('communities:list') 

        return render(request, 'communities/community_new.html', {'form': form})
