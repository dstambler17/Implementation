from django.shortcuts import render
from django.views import generic
from .models import Post, Category, Podcast
from django.contrib.auth.models import User
import calendar

# Create your views here.
def index(request):
    posts =  Post.objects.order_by('date_posted')[:5]
    podcasts = Podcast.objects.order_by('date_posted')[:5]
    return render(request, 'blog/index.html', {'posts' : posts, 'podcasts' : podcasts})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def year(request, year = None):
    post_list = Post.objects.filter(date_posted__year=year)
    podcast_list = Podcast.objects.filter(date_posted__year=year)
    return render(request,'blog/date.html',{'post_list': post_list, 'podcast_list' : podcast_list, 'year' : year})

def month(request, year = None, month= None):
    post_list = Post.objects.filter(date_posted__year=year, date_posted__month = month)
    podcast_list = Podcast.objects.filter(date_posted__year=year, date_posted__month = month)
    full_month = calendar.month_name[month]
    return render(request,'blog/date.html',{'post_list': post_list, 'podcast_list' : podcast_list, 'year' : year, 'month' : full_month})


class PostList(generic.ListView):
    template_name = 'blog/PostList.html'
    context_object_name = 'entry_list'

    def get_queryset(self):
        return Post.objects.order_by('date_posted')

class CategoryView(generic.DetailView):
    model = Category
    template_name = 'blog/category.html'

class Contributor(generic.ListView):
    template_name = 'blog/contributor.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(author=self.kwargs['user_id'])

class UniquePost(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'

class UniqueEpisode(generic.DetailView):
    model = Podcast
    template_name = 'blog/podcast.html'

class EpisodeList(generic.ListView):
    template_name = 'blog/episodes.html'
    context_object_name = 'entry_list'

    def get_queryset(self):
        return Podcast.objects.order_by('date_posted')
