from django.apps import AppConfig


class OurcompanyConfig(AppConfig):
    name = 'ourcompany'
    
    def ready(self):
        import ourcompany.signals