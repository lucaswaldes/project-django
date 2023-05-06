from django.contrib.auth import models

class UserAuthManager(models.UserManager):
    def create_new_discord_user(self, user):
        print('Inside Discord User Manager')
        discord_tag = '%s#%s' % (user['username'], user['discriminator'])
        new_user = self.create(
            discord_id=user['id'],
            avatar=user['avatar'],
            email=user['email'],
            public_flags=user['public_flags'],
            flags=user['flags'],
            locale=user['locale'], 
            mfa_enabled=user['mfa_enabled'],
            discord_tag=discord_tag
        )
        return new_user
