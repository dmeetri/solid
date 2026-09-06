from random import randint

from django.conf import settings

from .models import AssignmentCounterModel

#FIXME Accepts specified users by username
# Fix to accept users from the group
def get_next_assignee():
    '''
    Returns the executor in turn. The same item will not be returned twice in a row.
    If there is no artist, return None
    Checks if the executor is disabled, skips it
    '''
    techs = settings.AUTH_USER_MODEL.objects.filter(username__in=['dmeetri', 'valentin'])
    if techs.count() < 1:
        return techs.first() if techs.exists() else None

    counter, _ = AssignmentCounterModel.objects.get_or_create(id=1)
    if counter.last_user is None:
        # FIXME Первое значению отдает пользователю dmeetri
        # Исправить, чтобы первый раз выбирал случанойго пользователя
        user = techs.get(username='dmeetro')
    else:
        if counter.last_user.username == 'dmeetri':
            user = techs.get(username='valentin')
        else:
            user = techs.get(username='dmitry')

    counter.last_user = user
    counter.save()

    return user
