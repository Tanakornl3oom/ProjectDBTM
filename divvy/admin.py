from django.contrib import admin

from divvy.models import Member,Promotion,Interest

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Member._meta.fields]
	list_editable = ('user',)

class PromotionAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Promotion._meta.fields]

class InterestAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Interest._meta.fields]



admin.site.register(Member,MemberAdmin)
admin.site.register(Promotion,PromotionAdmin)
admin.site.register(Interest,InterestAdmin)

