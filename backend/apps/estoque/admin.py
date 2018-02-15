from django.contrib import admin

# from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

from .models import PalletMarca, PalletOrigem, PelePele, Romaneo

class PalletMarcaAdmin(admin.ModelAdmin):
    pass

class PalletOrigemAdmin(admin.ModelAdmin):
	pass

class PelePeleAdmin(admin.ModelAdmin):
	pass

class RomaneoAdmin(admin.ModelAdmin):
	pass

admin.site.register(Romaneo, RomaneoAdmin)
admin.site.register(PelePele, PelePeleAdmin)
admin.site.register(PalletOrigem, PalletOrigemAdmin)
admin.site.register(PalletMarca, PalletMarcaAdmin)