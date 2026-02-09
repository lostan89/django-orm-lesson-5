from django.contrib import admin

from .models import Flat, Complaint, Owner


class AdminInline(admin.TabularInline):
    model = Flat.flat_owner.through
    raw_id_fields = ['owner']

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('owner','town','address')
    readonly_fields = ['created_at']
    list_display = ['address', 'price','new_building','construction_year','town']
    list_editable = ['new_building']
    list_filter = ['new_building','has_balcony','rooms_number']
    raw_id_fields = ['likes']
    inlines = [AdminInline]

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['user', 'flat','text']
    raw_id_fields = ['flat']

class OwnerAdmin(admin.ModelAdmin):
    list_display = ['owner', 'owners_phonenumber', 'owner_pure_phone']
    raw_id_fields = ['flat']



admin.site.register(Flat, AuthorAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)

