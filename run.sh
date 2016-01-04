source $(which virtualenvwrapper.sh)

rm -R $WORKON_HOME/deployer
mkvirtualenv $WORKON_HOME/deployer
workon deployer

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

git -C $DIR pull origin master

pip install -r $DIR/requirements.txt

gunicorn -w 1 --bind $ADDRESS:$PORT wsgi:app

deactivate
