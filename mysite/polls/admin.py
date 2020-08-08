from django.contrib import admin

import polls.models as m

admin.site.register(m.Municipio)
admin.site.register(m.Capitan)
admin.site.register(m.Comuna)
admin.site.register(m.Lider)
admin.site.register(m.LiderRespBarrio)
admin.site.register(m.PuestosDeVotacion)
admin.site.register(m.Barrio)
admin.site.register(m.DatosDelVolante)
