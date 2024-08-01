from objectpack.actions import ObjectPack, Action, ActionPack
from objectpack.ui import ModelEditWindow, BaseEditWindow, make_combo_box
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Group, Permission


# ContentType
class ContentTypePack(ActionPack):

    model = ContentType
    add_to_desktop = True
    add_window = edit_window = ModelEditWindow.fabricate(ContentType)

# User
class UserPack(ObjectPack):

    model = User
    add_to_menu = True

# Group
class GroupPack(ObjectPack):

    model = Group
    add_to_menu = True

# Permission
class PermissionPack(ObjectPack):

    model = Permission
    add_to_menu = True