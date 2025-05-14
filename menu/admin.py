from django.contrib import admin

from menu.models import Menu


class ChildTabularInline(admin.TabularInline):
	model = Menu
	fields = ['title', 'slug']
	prepopulated_fields = {'slug': ['title']}


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ['title']}
	list_display = ['title', 'parent']
	inlines = [ChildTabularInline]

	@staticmethod
	def parent(obj):
		return obj.parent
