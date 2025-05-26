from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import BlogEntry

class BlogEntryCreateView(CreateView):
    model = BlogEntry
    fields = ['title', 'content', 'is_published', 'image']
    template_name = 'blog/blogentry_form.html'
    success_url = reverse_lazy('blog:blog_list')

class BlogListView(ListView):
    model = BlogEntry
    template_name = 'blog/blogentry_list.html'

    def get_queryset(self):
        # Возвращаем только те статьи, где is_published=True
        return BlogEntry.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    model = BlogEntry

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.viewed += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = BlogEntry
    fields = ('title', 'content', 'is_published', 'image')
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])

class BlogDeleteView(DeleteView):
    model = BlogEntry
    success_url = reverse_lazy('blog:blog_list')
