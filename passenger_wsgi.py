import sys, os

INTERP = "/home/CPANEL_ACCOUNT_NAME/FOLDER_NAME_PATH/venv/bin/python"
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

from index import app as application
