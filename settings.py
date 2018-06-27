import os


REPO_NAME = 'blog'
DEBUG = True
APP_DIR = os.path.dirname(os.path.abspath(__file__))

FLATPAGES_MARKDOWN_EXTENSIONS = []
FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages')
FLATPAGES_EXTENSION = '.md'
