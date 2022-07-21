from django.apps import AppConfig


class TweetterappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Tweetterapp'
    
    def ready(self):
        import Tweetterapp.signals