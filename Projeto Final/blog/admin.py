from django.contrib import admin
from blog.models import Post, Comentario

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'date']
    search_fields = ['titulo', 'autor', 'date' ]
    list_filter = ['date']
    
    class Meta: 
        verbose_name= 'Posts'
        ordering = ['-date']


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'data2']
    search_fields = ['usuario', 'data2' ]
    list_filter = ['data2']
    
    class Meta: 
        verbose_name= 'Comentários'
        ordering = ['-data2']
    