from django.conf.urls import url
from objectpack import desktop
from .controller import controller
from .actions import ContentTypePack, UserPack, GroupPack, PermissionPack


def register_urlpatterns():
	"""
	Регистрация конфигурации урлов для приложения
	"""
	return [url(*controller.urlpattern)]

def controller_view(request):
    """ Вьюшка контроллера """
    return controller.process_request(request)

def register_actions():
	"""
	Регистрация экшен-паков
	"""
	return controller.packs.extend([
    	ContentTypePack,
	])

def register_desktop_menu():
	"""
	регистрация элементов рабочего стола
	"""
	desktop.uificate_the_controller(
    	    controller,
    	    menu_root=desktop.MainMenu.SubMenu('Demo')
	)
