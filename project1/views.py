import os
from http import client
from django.views.generic.base import TemplateView

from butter_cms import ButterCMS

auth_token = os.getenv("BUTTERCMS_API_TOKEN", None)
client = ButterCMS(auth_token)


class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['home'] = 'Home Content'
        context['auth_token'] = auth_token
        return context


class BlogPageView(TemplateView):

    template_name = "blog_list.html"

    def get_context_data(self, **kwargs):
        context = super(BlogPageView, self).get_context_data(**kwargs)
        response = client.posts.all()
        context['latest_posts'] = response['data']
        return context


class BlogPostView(TemplateView):

    template_name = "blog_detail.html"

    def get_context_data(self, **kwargs):
        context = super(BlogPostView, self).get_context_data(**kwargs)
        response = client.posts.get(context['slug'])
        context['post'] = response['data']
        return context
