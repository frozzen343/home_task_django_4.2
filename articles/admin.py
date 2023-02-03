from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Scope


class ArticleInLineFormset(BaseInlineFormSet):
    def clean(self):
        main_tags = 0

        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_tags += 1

        if main_tags > 1: raise ValidationError('Основным может быть только один раздел')
        elif not main_tags: raise ValidationError('Укажите основной раздел') 

        return super().clean()


class ArticleInLine(admin.TabularInline):
    model = Scope
    formset = ArticleInLineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [ArticleInLine]
