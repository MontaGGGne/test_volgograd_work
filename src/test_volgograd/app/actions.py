from objectpack.actions import ObjectPack, Action, ActionPack
from objectpack.ui import ModelEditWindow, BaseEditWindow, make_combo_box
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Group, Permission
from functools import partial
from objectpack.filters import ColumnFilterEngine, FilterByField
from .models import Person
import logging


logging.basicConfig(level=logging.INFO, filename="actions.log",filemode="w")

# ContentType
class ContentTypePack(ObjectPack):
    model = ContentType
    # add_to_desktop = True
    add_to_menu = True
    # add_window = edit_window = ModelEditWindow.fabricate(model=ContentType)

    

# User
class UserPack(ObjectPack):
    model = User
    add_to_desktop = True
    add_to_menu = True

# Group
class GroupPack(ObjectPack):
    model = Group
    add_to_desktop = True
    add_to_menu = True

# Permission
class PermissionPack(ObjectPack):
    model = Permission
    add_to_desktop = True
    add_to_menu = True


################################################################################


class PersonPack(ObjectPack):

    model = Person
    logging.info("Before ModelEditWindow")
    add_window = edit_window = ModelEditWindow.fabricate(model)
    logging.info("After ModelEditWindow")
    add_to_menu = True

    columns = [
        {
            'data_index': 'name',
            'header': u'Имя',
            'width': 2,
        },
        {
            'data_index': 'surname',
            'header': u'Фамилия',
            'width': 2,
        },
        {
            'data_index': 'gender',
            'header': u'Пол',
            'width': 1,
        },
        {
            'data_index': 'birthday',
            'header': u'Дата рождения',
            'width': 1,
        }
    ]