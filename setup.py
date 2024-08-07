# Импорт недавно установленного пакета setuptools.
import setuptools
import os


print(os.listdir(os.path.join(os.path.dirname(__file__))))

# Открытие README.md и присвоение его LONG_DESCRIPTION.
with open("README.md", "r") as fh:
	LONG_DESCRIPTION = fh.read()

# Отркытие requirements-dev.txt и присвоение его REQUIREMENTS.
# with open('requires.txt', "r") as req_file:
#     REQUIREMENTS = req_file.read().split('\n')
REQUIREMENTS = ['django==2.2.2',
                'm3-django-compat==1.9.2',
                'm3-objectpack==2.2.47',
                'wheel==0.44.0']

# Дериктория с пакетами
PACKAGE_DIR = {"": "src"}

PACKAGE_DATA = {"src": ["LICENSE"]}
# Поиск пакетов
PACKAGES = setuptools.find_packages('src', include=['test_volgograd*'])

# Функция, которая принимает несколько аргументов. Она присваивает эти значения пакету.
setuptools.setup(
	# Имя дистрибутива пакета. Оно должно быть уникальным, поэтому добавление вашего имени пользователя в конце является обычным делом.
	name="test_volgograd",
	# Номер версии вашего пакета. Обычно используется семантическое управление версиями.
	version="0.0.1",
	# Имя автора.
	author="MontaGGGne",
	# Его почта.
	author_email="fredom871@gmail.com",
	# Краткое описание, которое будет показано на странице PyPi.
	description="Test work",
	# Длинное описание, которое будет отображаться на странице PyPi. Использует README.md репозитория для заполнения.
	long_description=LONG_DESCRIPTION,
	# Определяет тип контента, используемый в long_description.
	long_description_content_type="text/markdown",
	# URL-адрес, представляющий домашнюю страницу проекта. Большинство проектов ссылаются на репозиторий.
	url="https://github.com/MontaGGGne/test_volgograd_work",
 
	package_data=PACKAGE_DATA,
	# Находит все пакеты внутри проекта и объединяет их в дистрибутив.
	packages=PACKAGES,
 	# Дериктория с пакетами
 	package_dir=PACKAGE_DIR,
	# requirements или dependencies, которые будут установлены вместе с пакетом, когда пользователь установит его через pip.
	install_requires=REQUIREMENTS,
	# Предоставляет pip некоторые метаданные о пакете. Также отображается на странице PyPi.
	classifiers=[
		"Programming Language :: Python :: 3.9",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	# Требуемая версия Python.
	python_requires='>=3.9',
)