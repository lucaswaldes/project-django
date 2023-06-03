from django.contrib.auth.backends import BaseBackend

from .models import DiscordUser

class AuthenticationBackend(BaseBackend):
    def authenticate(self, request, user) -> DiscordUser:
        # print(request.user)
        find_user = DiscordUser.objects.filter(discord_id=user['id'])
        if len(find_user) == 0:
            print('User was not found. Saving...')
            new_user = DiscordUser.objects.create_new_discord_user(user)
            # print(new_user)
            return new_user
        
        existing_user = find_user[0]
        # Atualizar informações no banco de dados, se necessário
   
        if existing_user.avatar != user['avatar']:
            existing_user.avatar = user['avatar']
        if existing_user.username != user['username']:
            existing_user.username = user['username']
        if existing_user.email != user['email']:
            existing_user.email = user['email']
        if existing_user.discord_tag != '%s#%s' % (user['username'], user['discriminator']):
            existing_user.discord_tag = '%s#%s' % (user['username'], user['discriminator'])
        existing_user.save() 
        
        return existing_user

    def get_user(self, user_id):
        try:
            return DiscordUser.objects.get(pk=user_id)

        except DiscordUser.DoesNotExist:
            return None
            