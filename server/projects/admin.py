from django.contrib import admin

from projects.models import Project, Tag, Image

class ProjectAdmin(admin.ModelAdmin):
	list_display = ['title', 'students', 'date_created']
	list_filter = ['date_created']
	search_fields = ['title', 'tags', 'date_created', 'students', 'classroom']
	save_on_top = True
	prepopulated_fields = {"slug" : ("title",)}

admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)
admin.site.register(Image)