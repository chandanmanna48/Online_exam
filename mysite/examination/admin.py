from django.contrib import admin
from .models import Aptitude,Reasogning,GeneralKnowledge,Add_Aptitude_sample,Add_Reasogning_sample,Add_GeneralKnowledge_sample

# Register your models here.
admin.site.register(Aptitude)
admin.site.register(Reasogning)
admin.site.register(GeneralKnowledge)
admin.site.register(Add_Aptitude_sample)
admin.site.register(Add_Reasogning_sample)
admin.site.register(Add_GeneralKnowledge_sample)
